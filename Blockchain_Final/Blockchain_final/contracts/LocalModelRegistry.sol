// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract LocalModelRegistry {
    struct LocalModel {
        string ipfsHash;
        address contributor;
        uint256 timestamp;
    }

    mapping(uint256 => LocalModel) public localModels;
    uint256 public modelCount;

    event LocalModelRegistered(uint256 modelId, string ipfsHash, address contributor, uint256 timestamp);

    function registerLocalModel(string memory ipfsHash, address contributor) public {
        modelCount++;
        localModels[modelCount] = LocalModel(ipfsHash, contributor, block.timestamp);
        emit LocalModelRegistered(modelCount, ipfsHash, contributor, block.timestamp);
    }

    function getLocalModel(uint256 modelId) public view returns (string memory, address, uint256) {
        LocalModel memory model = localModels[modelId];
        return (model.ipfsHash, model.contributor, model.timestamp);
    }

    function getLocalModelCount() public view returns (uint256) {
        return modelCount;
    }

    function getLatestModelHash(address contributor) public view returns (string memory) {
        for (uint256 i = modelCount; i > 0; i--) {
            if (localModels[i].contributor == contributor) {
                return localModels[i].ipfsHash;
            }
        }
        return "";
    }
}
