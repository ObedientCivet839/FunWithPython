from user import Profile
from datetime import datetime
import time

from hashlib import sha256
import json

class Transaction:
    def __init__(self, from_user: Profile, to_user: Profile, desc: str):
        self.from_user = from_user
        self.to_user = to_user
        self.description = desc

    def __str__(self) -> str:
        # return json.dumps(self.__dict__, sort_keys=True, default=str)
        return self.description


class Block:
    def __init__(self, index: int, transactions: list[Transaction], timestamp: datetime, previous_hash: str, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
    
    def compute_hash(self):
        block_string = json.dumps(self.__dict__, sort_keys=True, default=str)
        # print("block_string:", block_string)
        return sha256(block_string.encode()).hexdigest()
    
    def __str__(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True, default=str)

class Blockchain:
    difficulty = 4

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self._create_genesis_block()
    
    def __str__(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True, default=str)

    def _create_genesis_block(self):
        genesis_block = Block(0, [], time.time(), "0")
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)
    
    @property
    def last_block(self):
        return self.chain[-1]
    
    def _proof(self, block):
        # Set current nonce
        computed_hash = block.compute_hash()
        while not Blockchain._is_valid_hash(computed_hash):
            # Keep recalculating until hash starts with '0'
            block.nonce += 1
            computed_hash = block.compute_hash()
        print("block.nonce (number of tries):", block.nonce)
        return computed_hash
    
    @classmethod
    def _is_valid_hash(cls, hash: str) -> bool:
        return hash.startswith('0'*Blockchain.difficulty)

    def _is_valid_proof(self, block: Block, block_hash: str) -> bool:
        """Confirm that the proof is valid for this block.

        Args:
            block (Block): block
            block_hash (str): hash

        Returns:
            bool: Returns True if the block_hash is valid for this block.
        """
        # Confirm that the hash is valid
        return Blockchain._is_valid_hash(block_hash) and block_hash == block.compute_hash()

    def _add_new_transaction(self, transaction: Transaction):
        """Add a new transaction to the current blockchain.

        Args:
            transaction (Transaction): new transaction
        """
        self.unconfirmed_transactions.append(transaction)
    
    def _mine(self) -> int:
        """[PRIVATE - Do not use directly] Create a new block that contains all current unconfirmed transactions.

        Returns:
            int: Index of the new block
        """
        if not self.unconfirmed_transactions:
            return False # No new transactions to mine
        
        last_block = self.last_block
        new_block = Block(
            index=last_block.index + 1,
            transactions=self.unconfirmed_transactions, # create a new block that contains all the unconfirmed transactions
            timestamp=time.time(),
            previous_hash=last_block.hash)
        
        proof = self._proof(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index

    def add_block(self, block: Block, proof: str) -> bool:
        previous_hash = self.last_block.hash
        # Make sure that this block has the last hash
        if previous_hash != block.previous_hash:
            return False
        if not self._is_valid_proof(block, proof):
            return False
        block.hash = proof
        self.chain.append(block)
        return True

    def last_index(self) -> int:
        return self.last_block.index
    
    def last_hash(self) -> str:
        return self.last_block.hash

