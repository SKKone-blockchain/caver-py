from caver.caver import Caver

caver = Caver("https://api.baobab.klaytn.net:8651")

def test_getBlockNumber_and_HashTest():
  blockNum = int(caver.klay.blocks.getCurrentBlockNumber(), 16)
  print('current block number:', blockNum)
  # '''
  # NOTE: getBlockByNumber and getBlockByHash take different data
  # '''
  block = caver.klay.blocks.getBlock(blockNum)
  print('current block:', block.number)
  nblock = caver.klay.blocks.getBlock(block.hash)
  print('get block by hash({})\n'.format(block.hash), nblock.number)

  assert block.transactions_root == nblock.transactions_root, 'Different block'

def test_getBlockReceipts():
  blockNum = caver.klay.blocks.getCurrentBlockNumber()
  block = caver.klay.blocks.getBlock(26441033)
  try:
    receipt = caver.klay.blocks.getBlockReceipts(block.hash)
    assert '0x3c90aa6e96c28ad790df46177bd69cae1f26b186490b364bce56155f773ac5ec' == receipt[0]['blockHash']
  except:
    assert 0

def test_getTransactionCount():
  blockNum = caver.klay.blocks.getCurrentBlockNumber()
  block = caver.klay.blocks.getBlock(int(blockNum, 16))
  assert caver.klay.blocks.getBlockTransactionCount(block.hash) == caver.klay.blocks.getBlockTransactionCount(block.number)


def test_getBlockWithConsensusInfo():
  blockNum = caver.klay.blocks.getCurrentBlockNumber()
  block = caver.klay.blocks.getBlock(int(blockNum, 16))
  assert caver.klay.blocks.getBlockWithConsensusInfo(block.hash) == caver.klay.blocks.getBlockWithConsensusInfo(block.number)


def test_getCommittee():
  blockNum = caver.klay.blocks.getCurrentBlockNumber()
  print(type(blockNum))
  assert caver.klay.blocks.getCommittee() == caver.klay.blocks.getCommittee(blockNum)

def test_getCommitteeSize():
  blockNum = caver.klay.blocks.getCurrentBlockNumber()
  print(type(blockNum))
  assert caver.klay.blocks.getCommitteeSize() == caver.klay.blocks.getCommitteeSize(blockNum)

# def test_getCouncil():

# def test_getStorageAt():

# def test_isMining():

# def test_isSyncing():

