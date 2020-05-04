from caver.caver import Caver

caver = Caver("https://api.baobab.klaytn.net:8651")

def test_getBlockNumber_and_HashTest():
  blockNum = int(caver.klay.blocks.getCurrentBlockNumber(), 16)
  print('current block number:', blockNum)
  '''
  getBlockByNumber와 getBlockByHash는 서로 다른 데이터를 가져오므로 사용에 유의
  '''
  block = caver.klay.blocks.getBlock(blockNum)
  print('current block:', block.number)
  nblock = caver.klay.blocks.getBlock(block.hash)
  print('get block by hash({})\n'.format(block.hash), nblock.number)

  assert block.transactions_root == nblock.transactions_root, '다른 블록입니다.'

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
  assert caver.klay.blocks.getCommittee() == caver.klay.blocks.getCommittee(blockNum)

# def test_getCommitteeSize():

# def test_getCouncil():

# def test_getStorageAt():

# def test_isMining():

# def test_isSyncing():

