class Account:
  def __init__(self, address, accountKey) :
    self.address = address
    self.accountKey = accountKey
    self.key_type = accountKey.type