from caver.caver import Caver

caver = Caver("https://api.baobab.klaytn.net:8651")

def test_class():
  assert caver.klay.provider != None
  assert caver.klay.accounts != None
  assert caver.klay.blocks != None
  assert caver.klay.defaultBlock != None