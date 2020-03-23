
from .block.block import Block
import requests
import json


class Blocks:
  def __init__(self, provider):
    self.provider = provider

  def getCurrentBlockNumber(self):
    payload = {
      "method": "klay_blockNumber",
      "params": [],
      "jsonrpc": "2.0",
      "id": 0,
    }
    response = requests.post(self.provider, json=payload).json()
    return response["result"]

  def getBlockByNumber(self, number="latest"):
    payload = {
        "method": "klay_getBlockByNumber",
        "params": [number, true],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])

  def getBlockByHash(self, hash):
    payload = {
        "jsonrpc":"2.0",
        "method":"klay_getBlockByHash",
        "params":[hash, true],
        "id":1
    }
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])

  def getBlockReceipts(self, hash):
    payload = {
        "jsonrpc":"2.0", 
        "method":"klay_getBlockReceipts", 
        "params":[hash],
        "id":73
    }
    
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])


  def getBlockTransactionCountByNumber(self, number=latest):
    payload = {
        "jsonrpc":"2.0",
        "method":"klay_getBlockTransactionCountByNumber",
        "params":[number],
        "id":1
    }
    
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])

  def getBlockTransactionCountByHash(self, hash):
    payload = {
      "jsonrpc":"2.0",
      "method":"klay_getBlockTransactionCountByHash",
      "params":[hash],
      "id":1
    }
    
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])


  def getBlockWithConsensusInfoByHash(self, hash):
    payload = {
        "jsonrpc":"2.0", 
        "method":"klay_getBlockWithConsensusInfoByHash", 
        "params":[hash],
        "id":73
    }
    
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])

  def getBlockWithConsensusInfoByNumber(self, number=latest):
    payload = {
        "jsonrpc":"2.0", 
        "method":"klay_getBlockWithConsensusInfoByNumber", 
        "params":[number],
        "id":73
    }
    
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])
