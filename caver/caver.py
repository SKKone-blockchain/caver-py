from .klay.klay import Klay

class Caver:
  # provier is network url ex)) "localhost:8551, https://api.baobab.klaytn.net:8651/"
  def __init__(self, provider):
    self.provider = provider
    self.klay = Klay("localhost:8551")

  def getProvider(self):
    return self.provider