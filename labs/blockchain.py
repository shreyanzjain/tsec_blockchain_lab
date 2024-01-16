'''
This is the implementation of a BlockChain Class

BlockChain:
    attr:
        chain = List of Blocks

    methods:
        add_block(data)
        get_latest_block() -> returns a Block object

Block(index, previous_hash, data):
    attr:
        index = index of the block (0 for genesis block)
        previous_hash = hash of the previous block ('0' for genesis block)
        timestamp = timestamp of creation of the block
        data = data stored in the block
        nonce = random number (used for mining)
        hash = hash calculated using the above attributes and the sha256 algorithm

'''
from datetime import datetime
import random
import hashlib
import json

class Block:
    def __init__(self, index: int, previous_hash: str, data: object):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        self.data = data
        self.nonce = random.randint(0, 2**31 - 1)
        self.hash = hashlib.sha256((f"{self.index}" + 
                                   f"{self.previous_hash}" + 
                                   f"{self.timestamp}" + 
                                   f"{self.data}" + f"{self.nonce}").encode(encoding="utf-8")).hexdigest()

class BlockChain:
    def __init__(self):
        self.chain = [Block(0, "0", "Genesis")]
    
    def add_block(self, data: object):
        prevBlock = self.chain[-1]
        new_block = Block(prevBlock.index + 1,
                          prevBlock.hash,
                          data)
        self.chain.append(new_block)
    
    def get_latest_block(self):
        return self.chain[-1]

if __name__ == "__main__":
    chain = BlockChain()
    chain.add_block('Hello, world')
    chain.add_block({
        "aloha": 1221
    })

    for i in chain.chain:
        print(json.dumps(i.__dict__, indent=4))