class Account:
  def __init__(self, address, accountKey) :
    self.address = address
    self.accountKey = accountKey
    self.private_key = accountKey.private_key
    self.key_type = accountKey.type