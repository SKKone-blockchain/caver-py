class Block:
  def __init__(self,parameter):
    '''
    parameter들 중 result에 존재하는 것만 받음
    '''
    def getParam(name):
      try:
        return parameter[name]
      except:
        return None
    self.data = {}  # 모든 member를 관리하기 좋게 dictionary에 모음
    for i in parameter.keys():
      self.data[i] = parameter[i]
    # self.blockscore = getParam("blockscore")
    # self.extra_data = getParam("extraData")
    # self.gas_used = getParam("gasUsed")
    # self.governance_data = getParam("governanceData")
    # self.hash = getParam("hash")
    # self.number = getParam("number")
    # self.parent_hash = getParam("parentHash")
    # self.logs_bloom = getParam('logsBloom')
    # self.transactions_root = getParam('transactionsRoot')
    # self.state_root = getParam('stateRoot')
    # self.receipts_root = getParam('receiptsRoot')
    # self.reward = getParam('reward')
    # self.block_score = getParam('blockScore')
    # self.total_block_score = getParam('totalBlockScore')
    # self.size = getParam('size')
    # self.timestamp = getParam('timestamp')
    # self.timestamp_FoS = getParam('timestampFoS')
    # self.transactions = getParam('transactions')
    # self.vote_data = getParam('voteData')

  def __repr__(self):
    return str(self.data)