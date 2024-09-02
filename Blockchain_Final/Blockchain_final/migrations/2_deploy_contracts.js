const LocalModelRegistry = artifacts.require("LocalModelRegistry");
const AggregatedModelRegistry = artifacts.require("AggregatedModelRegistry");
const ReputationSystem = artifacts.require("ReputationSystem");
const FileMetadataRegistry = artifacts.require("FileMetadataRegistry");

module.exports = function (deployer) {
  deployer.deploy(LocalModelRegistry);
  deployer.deploy(AggregatedModelRegistry);
  deployer.deploy(ReputationSystem);
  deployer.deploy(FileMetadataRegistry);
};
