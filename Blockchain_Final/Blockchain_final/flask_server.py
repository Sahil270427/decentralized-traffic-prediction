import pickle
import numpy as np
import pandas as pd
import requests
import json
from flask import Flask, request, jsonify
from web3 import Web3
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import logging
import gzip

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Connect to Ganache
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
web3.eth.defaultAccount = web3.eth.accounts[0]

# Load Contracts
def load_contract(abi_path, contract_address):
    with open(abi_path) as f:
        contract_abi = json.load(f)['abi']
    return web3.eth.contract(address=contract_address, abi=contract_abi)

local_model_registry_address = "0x9B11B8849a31294CD5A9db7E4B46811dFd2F8456"
aggregated_model_registry_address = "0x75b60B2D62896303964Df2b47c02B9040704C8aF"
reputation_system_address = "0xcCD9689ef6F94ceda5bC2676725878E69dFeEB0A"
file_metadata_registry_address = "0x6cC129463dC19b2A83AaDFC9a430B409835acef1"

local_model_registry = load_contract('build/contracts/LocalModelRegistry.json', local_model_registry_address)
aggregated_model_registry = load_contract('build/contracts/AggregatedModelRegistry.json', aggregated_model_registry_address)
reputation_system = load_contract('build/contracts/ReputationSystem.json', reputation_system_address)
file_metadata_registry = load_contract('build/contracts/FileMetadataRegistry.json', file_metadata_registry_address)

# Pinata API credentials
PINATA_BASE_URL = "https://api.pinata.cloud/"
PINATA_API_KEY = '41447cb8e9c4ac5f0c37'
PINATA_SECRET_API_KEY = 'a5033aa1f0e41a6ddd151e479100548920780a21b9c0ad0e9d196d52c0676a44'
endpoint = "pinning/pinFileToIPFS"
headers = {
    "pinata_api_key": PINATA_API_KEY,
    "pinata_secret_api_key": PINATA_SECRET_API_KEY
}

def upload_file_to_ipfs(filepath):
    with open(filepath, "rb") as f:
        response = requests.post(PINATA_BASE_URL + endpoint, files={"file": f}, headers=headers)
        return response.json()["IpfsHash"]

def train_register_local_model(contributor, dataset_path, target_column, description):
    # Load dataset
    data = pd.read_csv(dataset_path, nrows=1000)

    # Preprocessing
    X = data.drop(target_column, axis=1)
    y = data[target_column]

    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
     # Save model with gzip compression
    model_path = f'model_{contributor}.pkl.gz'
    with gzip.open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    # Upload model to IPFS
    model_hash = upload_file_to_ipfs(model_path)
    
    # Register model on the blockchain
    tx_hash = local_model_registry.functions.registerLocalModel(model_hash, contributor).transact({'from': contributor})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Local model registered with IPFS hash: {model_hash}")
    
    # Add metadata
    tx_hash = file_metadata_registry.functions.addFileMetadata(model_hash, f"Local Model by {contributor}", description, 'Local Model').transact({'from': contributor})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Metadata added for file hash: {model_hash}")
    
    # Calculate MSE for the model
    preds = model.predict(X_test)
    mse = mean_squared_error(y_test, preds)
    print(f"Contributor {contributor} - Model MSE: {mse}")

    # Reward contributor
    points = int(100 / mse)
    tx_hash = reputation_system.functions.rewardContributor(contributor, points).transact({'from': contributor})
    web3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Contributor {contributor} rewarded with {points} points")

    return local_model_registry.functions.getLocalModelCount().call()

@app.route('/register_local_model', methods=['POST'])
def register_local_model_endpoint():
    try:
        data = request.json
        contributor = data.get('contributor')
        dataset_path = data.get('dataset_path')
        target_column = data.get('target_column')
        description = data.get('description')
        model_id = train_register_local_model(contributor, dataset_path, target_column, description)
        if model_id is None:
            return jsonify({"error": "Failed to register local model"}), 500
        return jsonify({"local_model_id": model_id})
    except Exception as e:
        logger.error(f"Error in /register_local_model endpoint: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(port=5000)
