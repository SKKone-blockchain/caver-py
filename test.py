from caver.caver import Caver

def provider_test():
  caver = Caver("localhost:8551")
  print(caver.getProvider())

provider_test()