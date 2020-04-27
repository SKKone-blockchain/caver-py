
from .block.block import Block
import requests
import json

HASH_LENGTH = 257
BLOCK_SPECIAL_NUMBER = ("genesis", "latest", "pending")

class Blocks:
  def __init__(self, provider):
    self.provider = provider

  def __hashCheck(self, hash):
    if not(type(hash) == str and hash[:2] == '0x' and len(hash) <= HASH_LENGTH):
      raise ValueError("hash is None or not a (bytes) string")

  def __numberCheck(self, number):
    if not(number in BLOCK_SPECIAL_NUMBER or number <= int(self.getCurrentBlockNumber(),16)):
      raise ValueError("Invalid number, number is bigger than the recent block number or is None")
  
  def getCurrentBlockNumber(self): # return number is hex string
    payload = {
      "method": "klay_blockNumber",
      "params": [],
      "jsonrpc": "2.0",
      "id": 0,
    }
    response = requests.post(self.provider, json=payload).json()
    return response["result"]

  def getBlock(self, inputs):
    # if input's type is int, then get block by number.
    # or is string, then get block by hash
    payload = {
      "method": "klay_getBlockBy",
      "params": [],
      "jsonrpc": "2.0",
      "id": 0,
    }
    if type(inputs) == int or inputs in "latest":
      self.__numberCheck(inputs)
      payload['method'] = payload['method'] + 'Number'
      payload['params'] = [hex(inputs), True]
    elif type(inputs) == str:
      self.__hashCheck(inputs)
      payload['method'] = payload['method'] + 'Hash'
      payload['params'] = [inputs, True]
    else:
      raise ValueError("Invalid input's type")
    response = requests.post(self.provider, json=payload).json()
    # print(response)
    return Block(response["result"])

  def getBlockReceipts(self, hash=None):
    self.__hashCheck(hash)
    print(hash)
    payload = {
        "method": "klay_getBlockReceipts",
        "params": [hash],
        "jsonrpc": "2.0",
        "id": 73,
    }
    response = requests.post(self.provider, json=payload).json()
    return list(response["result"])

  def getBlockTransactionCount(self, inputs):
    # if input's type is int, then get block by number.
    # or is string, then get block by hash
    payload = {
      "method": "klay_getBlockTransactionCountBy",
      "params": [inputs],
      "jsonrpc": "2.0",
      "id": 0,
    }
    if type(inputs) == int:
      self.__numberCheck(inputs)
      payload['method'] = payload['method'] + 'Number'
    elif type(inputs) == str:
      self.__hashCheck(inputs)
      payload['method'] = payload['method'] + 'Hash'
    else:
      raise ValueError("Invalid input's type")

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