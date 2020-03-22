
from .block.block import Block
import requests
import json



class Blocks:
  def __init__(self, provider):
    self.provider = provider

  def __hashCheck(self, hash):
    assert type(hash) == str and hash[:2] == '0x', "hash is None or not a (bytes) string"

  def __numberCheck(self, number):
    assert number=="latest" or int(number,16)<=int(self.getCurrentBlockNumber(),16), "Invalid number, number is bigger than the recent block number or is None"
  
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
    self.__numberCheck(number)
    payload = {
        "method": "klay_getBlockByNumber",
        "params": [number, True],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])

  def getBlockByHash(self, hash=None):
    self.__hashCheck(hash)
    payload = {
        "method": "klay_getBlockByHash",
        "params": [hash, True],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(self.provider, json=payload).json()
    return Block(response["result"])

  def getBlockReceipts(self, hash=None):
    self.__hashCheck(hash)
    payload = {
        "method": "klay_getBlockReceipts",
        "params": [hash],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])