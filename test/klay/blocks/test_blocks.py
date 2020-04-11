from caver.caver import Caver

caver = Caver("https://api.baobab.klaytn.net:8651")

def test_getBlockNumber_and_HashTest():
  blockNum = caver.klay.blocks.getCurrentBlockNumber()
  print('current block number:', blockNum)
  '''
  getBlockByNumber와 getBlockByHash는 서로 다른 데이터를 가져오므로 사용에 유의
  '''
  block = caver.klay.blocks.getBlockByNumber(blockNum)
  print('current block:', block.number)
  nblock = caver.klay.blocks.getBlockByHash(block.hash)
  print('get block by hash({})\n'.format(block.hash), nblock.number)

  assert block.transactions_root == nblock.transactions_root, '다른 블록입니다.'

def test_getBlockReceipts():
  blockNum = caver.klay.blocks.getCurrentBlockNumber()
  block = caver.klay.getBlock(int(blockNum, 16))
  try:
    receipt = caver.klay.blocks.getBlockReceipts(block.hash)
  except:
    assert 0

def test_getTransactionCountByNumber_and_hash():
  blockNum = caver.klay.blocks.getCurrentBlockNumber()
  block = caver.klay.getBlock(int(blockNum, 16))
  assert caver.klay.blocks.getBlockTransactionCountByHash(block.hash) == caver.klay.blocks.getBlockTransactionCountByNumber(blockNum)
