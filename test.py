from caver.caver import Caver

caver = Caver("https://api.baobab.klaytn.net:8651")
def provider_test():
  caver = Caver("https://api.baobab.klaytn.net:8651")
  block = caver.klay.blocks.getBlockByNumber()
provider_test()

def getBlockTest():
  blockNum = caver.klay.blocks.getCurrentBlockNumber()
  print('current block number:', blockNum)
  '''
  getBlockByNumber와 getBlockByHash는 서로 다른 데이터를 가져오므로 사용에 유의
  '''
  block = caver.klay.blocks.getBlockByNumber(blockNum)
  print('current block:', block.number)
  nblock = caver.klay.blocks.getBlockByHash(block.hash)
  print('get block by hash({})\n'.format(block.hash), nblock.number)

  if block.transactions_root == nblock.transactions_root:
    print('동일한 블록이 맞습니다.')
  else:
    print('다른 블록입니다.')

getBlockTest()