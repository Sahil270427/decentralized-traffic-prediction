// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ReputationSystem {
    mapping(address => uint256) public reputation;

    event ContributorRewarded(address contributor, uint256 points);

    function rewardContributor(address contributor, uint256 points) public {
        reputation[contributor] += points;
        emit ContributorRewarded(contributor, points);
    }

    function getReputation(address contributor) public view returns (uint256) {
        return reputation[contributor];
    }
}
