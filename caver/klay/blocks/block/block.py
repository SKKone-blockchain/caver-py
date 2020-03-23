class Block:
  def __init__(self,parameter):
    self.blockscore = parameter["blockscore"]
    self.extra_data = parameter["extraData"]
    self.gas_used = parameter["gasUsed"]
    self.governance_data = parameter["governanceData"]
    self.hash = parameter["hash"]
    self.number = parameter["number"]
    self.parent_hash = parameter["parentHash"]x