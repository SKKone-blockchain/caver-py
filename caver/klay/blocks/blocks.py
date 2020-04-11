
from .block.block import Block
import requests
import json



class Blocks:
  def __init__(self, provider):
    self.provider = provider

  def __hashCheck(self, hash):
    if not(type(hash) == str and hash[:2] == '0x'):
      raise ValueError("hash is None or not a (bytes) string")

  def __numberCheck(self, number):
    if not(number=="latest" or int(number,16)<=int(self.getCurrentBlockNumber(),16)):
      raise ValueError("Invalid number, number is bigger than the recent block number or is None")
  
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


  def getBlockTransactionCountByNumber(self, number=None):
    self.__numberCheck(number)
    payload = {
        "method": "klay_getBlockTransactionCountByNumber",
        "params": [number],
        "jsonrpc": "2.0",
        "id": 1,
    }
    response = requests.post(self.provider, json=payload).json()
    return response["result"]

  def getBlockTransactionCountByHash(self, hash=None):
    self.__hashCheck(hash)
    payload = {
        "method": "klay_getBlockTransactionCountByHash",
        "params": [hash],
        "jsonrpc": "2.0",
        "id": 1,
    }
    response = requests.post(self.provider, json=payload).json()
    return response["result"]

  def getBlockWithConsensusInfoByHash(self, hash=None):
    self.__hashCheck(hash)

    payload = {
      "method": "klay_getBlockWithConsensusInfoByHash",
      "params": [hash],
      "jsonrpc": "2.0",
      "id": 73,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])

  def getBlockWithConsensusInfoByNumber(self, number=None):
    self.__numberCheck(number)

    payload = {
      "method": "klay_getBlockWithConsensusInfoByNumber",
      "params": [number],
      "jsonrpc": "2.0",
      "id": 73,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])

  def getCommittee(self, defaultBlock="latest"):
    self.__numberCheck(defaultBlock)
    
    payload = {
      "method": "klay_getCommittee",
      "params": [defaultBlock],
      "jsonrpc": "2.0",
      "id": 73,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])
  
  def getCommitteeSize(self, defaultBlock="latest"):
    self.__numberCheck(defaultBlock)

    payload = {
      "method": "klay_getCommitteeSize",
      "params": [defaultBlock],
      "jsonrpc": "2.0",
      "id": 73,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])

  def getCouncil(self, defaultBlock="latest"):
    self.__numberCheck(defaultBlock)

    payload = {
      "method": "klay_getCouncil",
      "params": [defaultBlock],
      "jsonrpc": "2.0",
      "id": 73,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])

  def getCouncilSize(self, defaultBlock="latest"):
    self.__numberCheck(defaultBlock)

    payload = {
      "method": "klay_getCouncilSize",
      "params": [defaultBlock],
      "jsonrpc": "2.0",
      "id": 73,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])

  def getStorageAt(self, address, position, defaultBlock="latest"):
    self.__hashCheck(address)
    self.__numberCheck(defaultBlock)

    payload = {
      "method": "klay_getStorageAt",
      "params": [address, hex(position), defaultBlock],
      "jsonrpc": "2.0",
      "id": 1,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])

  def isMining(self):
    payload = {
      "method": "klay_mining",
      "params": [],
      "jsonrpc": "2.0",
      "id": 1,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])

  def isSyncing(self):
    payload = {
      "method": "klay_syncing",
      "params": [],
      "jsonrpc": "2.0",
      "id": 1,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])