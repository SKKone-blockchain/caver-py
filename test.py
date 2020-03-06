from caver.caver import Caver

def provider_test():
  caver = Caver("localhost:8551")
  a = caver.klay.accounts.create()
  print (a.address)
  print (a.accountKey.key.to_bytes())
  print (a.accountKey.key.to_hex())
  print (a.accountKey.type)

provider_test()