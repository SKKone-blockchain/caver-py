class Block:
  def __init__(self,parameter):
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 9a78dec01cd5a52c7456ee5dd931268c572bea0f
    '''
    parameter들 중 result에 존재하는 것만 받음
    '''
    def getParam(name):
      try:
        return parameter[name]
      except:
        return None

    self.blockscore = getParam("blockscore")
    self.extra_data = getParam("extraData")
    self.gas_used = getParam("gasUsed")
    self.governance_data = getParam("governanceData")
    self.hash = getParam("hash")
    self.number = getParam("number")
    self.parent_hash = getParam("parentHash")
    self.logs_bloom = getParam('logsBloom')
    self.transactions_root = getParam('transactionsRoot')
    self.state_root = getParam('stateRoot')
    self.receipts_root = getParam('receiptsRoot')
    self.reward = getParam('reward')
    self.block_score = getParam('blockScore')
    self.total_block_score = getParam('totalBlockScore')
    self.size = getParam('size')
    self.timestamp = getParam('timestamp')
    self.timestamp_FoS = getParam('timestampFoS')
    self.transactions = getParam('transactions')
    self.vote_data = getParam('voteData')
<<<<<<< HEAD
=======
    self.blockscore = parameter["blockscore"]
    self.extra_data = parameter["extraData"]
    self.gas_used = parameter["gasUsed"]
    self.governance_data = parameter["governanceData"]
    self.hash = parameter["hash"]
    self.number = parameter["number"]
    self.parent_hash = parameter["parentHash"]
>>>>>>> 86db6c1390cae6aba0395469f047d93243807964
=======
>>>>>>> 9a78dec01cd5a52c7456ee5dd931268c572bea0f
