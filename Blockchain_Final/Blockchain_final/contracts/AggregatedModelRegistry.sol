// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AggregatedModelRegistry {
    struct AggregatedModel {
        string ipfsHash;
        uint256 version;
        uint256 timestamp;
        uint256 lastLocalModelId;
    }

    mapping(uint256 => AggregatedModel) public aggregatedModels;
    uint256 public aggregatedModelCount;

    event AggregatedModelRegistered(uint256 modelId, string ipfsHash, uint256 version, uint256 timestamp, uint256 lastLocalModelId);

    function registerAggregatedModel(string memory ipfsHash, uint256 version, uint256 lastLocalModelId) public {
        aggregatedModelCount++;
        aggregatedModels[aggregatedModelCount] = AggregatedModel(ipfsHash, version, block.timestamp, lastLocalModelId);
        emit AggregatedModelRegistered(aggregatedModelCount, ipfsHash, version, block.timestamp, lastLocalModelId);
    }

    function getAggregatedModel(uint256 modelId) public view returns (string memory, uint256, uint256, uint256) {
        AggregatedModel memory aggregatedModel = aggregatedModels[modelId];
        return (aggregatedModel.ipfsHash, aggregatedModel.version, aggregatedModel.timestamp, aggregatedModel.lastLocalModelId);
    }

    function getLastLocalModelId(uint256 modelId) public view returns (uint256) {
        AggregatedModel memory aggregatedModel = aggregatedModels[modelId];
        return aggregatedModel.lastLocalModelId;
    }
}
