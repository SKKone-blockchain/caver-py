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

    self.blockscore = getParam("blockscore")
    self.extra_data = getParam("extraData")
    self.gas_used = getParam("gasUsed")
    self.governance_data = getParam("governanceData")
    self.hash = getParam("hash")
    self.number = int(getParam("number"),16)
    self.parent_hash = getParam("parentHash")
    self.proposer = getParam('proposer')
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
    self.starting_block = getParam('startingBlock')
    self.current_block = getParam('currentBlock')
    self.highest_block = getParam('highestBlock')
    self.pulled_states = getParam('pulledStates')
    self.known_states = getParam('knownStates')