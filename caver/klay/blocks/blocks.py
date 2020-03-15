
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
        "params": [number, True],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])
  
  def getBlockByHash(self, hash='0x', onlyTxHash=False):
    payload = {
        "method": "klay_getBlockByHash",
        "params": [hash, onlyTxHash],
        "jsonrpc": "2.0",
        "id":1
    }
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])