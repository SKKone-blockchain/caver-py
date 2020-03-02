from .accounts.accounts import Accounts

class Klay:
  def __init__(self, provider):
    self.provider = provider
    self.accounts = Accounts()