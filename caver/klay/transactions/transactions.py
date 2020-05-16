from .transaction.transaction import Transaction, TransactionReceipt
import requests
import json


class Transactions:
  def __init__(self, provider):
    self.provider = provider