from .accounts.accounts import Accounts
from .blocks.blocks import Blocks

class Klay:
  def __init__(self, provider):
    self.provider = provider
    self.accounts = Accounts()
    self.blocks = Blocks(provider)
    self.defaultBlock = 'latest'

  def getBlockNumber():
    pass

  def getBlock():
    pass

  def getBlockReceipts():
    pass

  def getBlockTransactionCount():
    pass

  def getBlockWithConsensusInfo():
    pass

  def getCommittee():
    pass

  def getCommitteeSize():
    pass

  def getCouncil():
    pass

  def getCouncilSize():
    pass

  def getStorageAt():
    pass

  def isMining():
    pass

  def isSyncing():
    pass