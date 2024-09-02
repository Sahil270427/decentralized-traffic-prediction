from locust import HttpUser, task, between
import json
from web3 import Web3
import requests

class BlockchainUser(HttpUser):
    wait_time = between(1, 5)
    host = "http://127.0.0.1:5000"  # Add the host attribute pointing to your Flask server

    def on_start(self):
        # Setup parameters for registering a local model
        self.contributor = "0xE83be71bc2f873Ea381Ff11D8c41d5B0923814E9"
        self.dataset_path = "contributor_1_dataset.csv"
        self.target_column = "Severity"
        self.description = "A local model for testing scalability"
    @task
    def register_local_model(self):
        payload = {
            "contributor": self.contributor,
            "dataset_path": self.dataset_path,
            "target_column": self.target_column,
            "description": self.description
        }
        response = self.client.post("/register_local_model", json=payload)
        try:
            response.raise_for_status()  # Raise HTTPError for bad responses
            response_json = response.json()
            print(response_json)
        except requests.exceptions.HTTPError as e:
            print(f"HTTPError: {e}")
        except requests.exceptions.JSONDecodeError:
            print(f"Failed to decode JSON, status code: {response.status_code}, response text: {response.text}")
# To run Locust, save this script and run: locust -f locustfile.py
  