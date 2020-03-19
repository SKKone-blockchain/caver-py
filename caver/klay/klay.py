from .accounts.accounts import Accounts
from .blocks.blocks import Blocks

class Klay:
  def __init__(self, provider):
    self.provider = provider
    self.accounts = Accounts()
    self.blocks = Blocks(provider)
    self.defaultBlock = 'latest'

  def getBlockNumber(self):
    return self.blocks.getCurrentBlockNumber()

  def getBlock(self):
    pass

  def getBlockReceipts(self):
    pass

  def getBlockTransactionCount(self):
    pass

  def getBlockWithConsensusInfo(self):
    pass

  def getCommittee(self):
    pass

  def getCommitteeSize(self):
    pass

  def getCouncil(self):
    pass

  def getCouncilSize(self):
    pass

  def getStorageAt(self):
    pass

  def isMining(self):
    pass

  def isSyncing(self):
    pass