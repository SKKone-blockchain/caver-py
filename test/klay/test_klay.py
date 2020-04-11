from caver.caver import Caver

caver = Caver("https://api.baobab.klaytn.net:8651")

def test_getBlockTest():
  blockNum = caver.klay.getBlockNumber()
  print('current block number:', blockNum)
  '''
  getBlockByNumber와 getBlockByHash는 서로 다른 데이터를 가져오므로 사용에 유의
  '''
  block = caver.klay.getBlock(int(blockNum, 16))
  print('current block:', block.number)
  nblock = caver.klay.getBlock(block.hash)
  print('get block by hash({})\n'.format(block.hash), nblock.number)

  assert block.transactions_root == nblock.transactions_root, '다른 블록입니다.'

def test_getBlockReceipts():
  blockNum = caver.klay.getBlockNumber()
  block = caver.klay.getBlock(int(blockNum, 16))
  try:
    receipt = caver.klay.getBlockReceipts(block.hash)
  except:
    assert 0

def test_getTransactionCount():
  blockNum = caver.klay.getBlockNumber()
  block = caver.klay.getBlock(int(blockNum, 16))
  assert caver.klay.getBlockTransactionCount(block.hash) == caver.klay.getBlockTransactionCount(block.number)
