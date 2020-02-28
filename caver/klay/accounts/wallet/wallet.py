from ..account.account import Account

class Wallet:
  # TODO: Wallet Must be Singleton in One Caver Module
  def __init__(self, userAccounts = []) :
    self.accounts = {}
    for account in userAccounts :
      self.accounts[account.address] = account

  def addNewAccount(self, account) :
    if type(account) is Account :
      self.accounts[account.address] = account
    else :
      raise Exception # TODO specify the Exception

  def getAccountByAddress(self, address) :
    return self.accounts[address]

  def removeAccountByAddress(self, address) :
    del self.accounts[address]

  def clear(self, address) :
    self.accounts.clear()