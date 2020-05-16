from .transaction.transaction import Transaction, TransactionReceipt
import requests
import json
from ..blocks.blocks import Blocks

class Transactions:
  HASH_LENGTH = 257
  BLOCK_SPECIAL_NUMBER = ("genesis", "latest", "pending")

  def __init__(self, provider):
    self.provider = provider
    self.blocks = Blocks(provider)

  def __hashCheck(self, hash):
    if not(type(hash) == str and hash[:2] == '0x' and len(hash) <= self.HASH_LENGTH):
      raise ValueError("hash is None or not a (bytes) string")

  def __numberCheck(self, number):
    if not(number in self.BLOCK_SPECIAL_NUMBER or number <= int(self.blocks.getCurrentBlockNumber(),16)):
      raise ValueError("Invalid number, number is bigger than the recent block number or is None")

  def call(self, callObject, blockNumber):
    self.__numberCheck(blockNumber)
    if type(callObject) != dict:
      raise TypeError("callObject must be a dictionary")

    try:
      callObject["to"]
    except:
      raise ValueError("callObject must have a 'to' value")

    payload = {
      "method": "klay_call",
      "params": [],
      "jsonrpc": "2.0",
      "id": 1,
    }
    payload["params"] = [callObject, blockNumber]
    response = requests.post(self.provider, json=payload).json()
    return response["result"]

  def estimateGas(self, callObject, blockNumber):
    self.__numberCheck(blockNumber)
    if type(callObject) != dict:
      raise TypeError("callObject must be a dictionary")

    try:
      callObject["to"]
    except:
      raise ValueError("callObject must have a 'to' value")

    payload = {
      "method": "klay_estimateGas",
      "params": [],
      "jsonrpc": "2.0",
      "id": 1,
    }
    payload["params"] = [callObject, blockNumber]
    response = requests.post(self.provider, json=payload).json()
    return int(response["result"])

  def estimateComputationCost(self, callObject, blockNumber):
    self.__numberCheck(blockNumber)
    if type(callObject) != dict:
      raise TypeError("callObject must be a dictionary")

    try:
      callObject["to"]
    except:
      raise ValueError("callObject must have a 'to' value")

    payload = {
      "method": "klay_estimateComputationCost",
      "params": [],
      "jsonrpc": "2.0",
      "id": 1,
    }
    payload["params"] = [callObject, blockNumber]
    response = requests.post(self.provider, json=payload).json()
    return response["result"]

  def getTransactionByBlockHashAndIndex(self, blockHash, index):
    self.__hashCheck(blockHash)
    payload = {
      "method": "klay_getTransactionByBlockHashAndIndex",
      "params": [],
      "jsonrpc": "2.0",
      "id": 1,
    }
    payload["params"] = [blockHash, index]
    response = requests.post(self.provider, json=payload).json()
    return Transaction(response["result"])

  def getTransactionByBlockNumberAndIndex(self, blockNumber, index):
    self.__numberCheck(blockNumber)
    payload = {
      "method": "klay_getTransactionByBlockHashAndIndex",
      "params": [],
      "jsonrpc": "2.0",
      "id": 1,
    }
    payload["params"] = [blockNumber, index]
    response = requests.post(self.provider, json=payload).json()
    return Transaction(response["result"])