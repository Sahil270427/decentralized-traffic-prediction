// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract FileMetadataRegistry {
    struct FileMetadata {
        string ipfsHash;
        string name;
        string description;
        string tags;
        uint256 timestamp;
    }

    mapping(string => FileMetadata) public fileMetadata;
    string[] public fileHashes;

    event FileMetadataAdded(string ipfsHash, string name, string description, string tags, uint256 timestamp);

    function addFileMetadata(string memory ipfsHash, string memory name, string memory description, string memory tags) public {
        fileMetadata[ipfsHash] = FileMetadata(ipfsHash, name, description, tags, block.timestamp);
        fileHashes.push(ipfsHash);
        emit FileMetadataAdded(ipfsHash, name, description, tags, block.timestamp);
    }

    function searchFilesByTag(string memory tag) public view returns (string[] memory) {
        uint256 count = 0;
        for (uint i = 0; i < fileHashes.length; i++) {
            if (keccak256(abi.encodePacked(fileMetadata[fileHashes[i]].tags)) == keccak256(abi.encodePacked(tag))) {
                count++;
            }
        }

        string[] memory results = new string[](count);
        uint256 index = 0;
        for (uint i = 0; i < fileHashes.length; i++) {
            if (keccak256(abi.encodePacked(fileMetadata[fileHashes[i]].tags)) == keccak256(abi.encodePacked(tag))) {
                results[index] = fileHashes[i];
                index++;
            }
        }
        return results;
    }

    function getFileMetadata(string memory ipfsHash) public view returns (string memory, string memory, string memory, uint256) {
        FileMetadata memory metadata = fileMetadata[ipfsHash];
        return (metadata.name, metadata.description, metadata.tags, metadata.timestamp);
    }
}
