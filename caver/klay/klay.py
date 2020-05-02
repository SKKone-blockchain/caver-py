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
