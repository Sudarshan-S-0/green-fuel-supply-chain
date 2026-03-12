// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract GreenFuel {

    struct Batch {
        string batchId;
        string status;
    }

    mapping(string => Batch) public batches;

    function addBatch(string memory _batchId) public {
        batches[_batchId] = Batch(_batchId, "Producer");
    }

    function updateStage(string memory _batchId, string memory _stage) public {
        batches[_batchId].status = _stage;
    }

    function getBatch(string memory _batchId) public view returns (string memory) {
        return batches[_batchId].status;
    }
}