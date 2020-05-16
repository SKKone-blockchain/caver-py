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
