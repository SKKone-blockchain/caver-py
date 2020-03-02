from bytes import Bytes
from hashFunction import *

def createKeyPair(entropy) :
  innerHex = keccak256(Bytes.concat(Bytes.random(32), Bytes.random(32)))
  middleHex = Bytes.concat(Bytes.concat(Bytes.random(32), innerHex), Bytes.random(32))
  outerHex = keccak256(middleHex)
  return generateKeyPairWithPrivateKey(outerHex)

def generateKeyPairWithPrivateKey(privateKey) :
  # 아래 자바스크립트 코드 참조, 타원곡선암호와 동일한 방식으로 퍼블릭키 도출 후
  # 짝수 홀수에 따라 퍼블릭키 결정
  # Ethereum KeyPair와 동일

  # const buffer = Buffer(privateKey.slice(2), "hex");
  # const ecKey = secp256k1.keyFromPrivate(buffer);
  # const publicKey = "0x" + ecKey.getPublic(false, 'hex').slice(2);
  # const publicHash = keccak256(publicKey);
  # const address = toChecksum("0x" + publicHash.slice(-40));
  address  = 'calculated publickey_hash_check'
  key_pair = {
    "address" : address,
    "private_key" : privateKey
  }

  return key_pair
