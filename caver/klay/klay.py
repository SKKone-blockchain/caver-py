from .accounts.accounts import Accounts
from .blocks.blocks import Blocks

class Klay:
  def __init__(self, provider):
    self.provider = provider
    self.accounts = Accounts()
    self.blocks = Blocks(provider)
    self.defaultBlock = 'latest'

  def getBlockWithConsensusInfo(self, inputs):
    if type(inputs) == str:
      return self.blocks.getBlockWithConsensusInfoByHash(inputs)

    else:
      return self.blocks.getBlockWithConsensusInfoByNumber(hex(inputs))

  def getCommittee(self, defaultBlock="latest"):
    return self.blocks.getCommittee(defaultBlock)

  def getCommitteeSize(self, defaultBlock="latest"):
    return self.blocks.getCommitteeSize(defaultBlock)

  def getCouncil(self, defaultBlock="latest"):
    return self.blocks.getCouncil(defaultBlock)

  def getCouncilSize(self, defaultBlock="latest"):
    return self.blocks.getCouncilSize(defaultBlock)

  def getStorageAt(self, address, position, defaultBlock="latest"):
    return self.blocks.getStorageAt(address, position, defaultBlock)

  def isMining(self):
    return self.blocks.isMining()

  def isSyncing(self):
    return self.blocks.isSyncing()