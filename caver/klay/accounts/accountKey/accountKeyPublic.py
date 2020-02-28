class AccountKeyPublic:
  def __init__(self, private_key) :
    if type(private_key) is str :
      self.key = private_key
      self.type = '0x02' # '0x02 is accountKeyPublic'
    else :
      raise Exception # TODO Specify Exception Type