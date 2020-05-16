class Transactions:
  def __init__(self):
    '''
    parameter들 중 result에 존재하는 것만 받음
    '''
    def getParam(name):
      try:
        return parameter[name]
      except:
        return None

    self.block_hash = getParam("blockHash")
    self.block_number = getParam("blockNumber")
    self.fee_payer = getParam("feePayer")
    self.fee_payer_signatures = getParam("feePayerSignatures")
    self.from_address = getParam("from") # Python inhibits using from
    self.gas = getParam("gas")
    self.gas_price = getParam("gasPrice")
    self.hash = getParam("hash")
    self.nonce = getParam("nonce")
    self.send_Tx_hash = getParam("sendTxHash")
    self.signatures = getParam("signatures")
    self.to = getParam("to")
    self.transaction_index  = getParam("transactionIndex")
    self.type = getParam("type")
    self.type_int = getParam("typeInt")
    self.value = getParam("value")
    self.gas_used = getParam("gasUsed")
    self.code_format = getParam("codeFormat")
    self.contract_address = getParam("contractAddress")
    self.logs = getParam("logs")
    self.logsBloom = getParam("logsBloom")
    self.status = getParam("status")
    self.transaction_hash = getParam("transactionHash")