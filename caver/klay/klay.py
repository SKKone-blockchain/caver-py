from .account.account import Account

class Klay:
  def __init__(self, provider):
    self.provider = provider
    self.account = Account()