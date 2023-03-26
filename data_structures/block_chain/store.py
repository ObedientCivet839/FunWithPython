import random
from user import Profile
from block import Block, Blockchain, Transaction
import time

# DONE(P1): Implement a store with multiple users and multiple transactions at the same time.
# Each time, a transaction needs to create a new valid block and create a proof.
# Then, they will apply to the server to create a new block.
class Application:
    """Represent a mobile app that will submit requests to the blockchain.
    """
    def __init__(self, app_name: str, users: list[Profile], actions: list[str], bc: Blockchain) -> None:
        """Initialize a new application

        Args:
            app_name (str): name of the app (e.g. "Amazon")
            users (list[Profile]): list of users of the app
            actions (list[str]): actions that the app supports (e.g. "Buy toothbrush")
            bc (Blockchain): the blockchain that the app connects to
        """
        self.name = app_name
        self.users = users
        self.actions = actions
        self.bc = bc
        
    def _createRandomTransaction(self):
        # Pick 2 random users
        # Generate a random description
        user1 = random.choice(self.users)
        user2 = random.choice(self.users)
        action = random.choice(self.actions)
        desc = '{}: {} {} {}'.format(self.name, user1.name.firstlast(), action.lower(), user2.name.firstlast())
        return Transaction(user1, user2, desc)
    
    def generate_hash(self, block: Block):
        computed_hash = block.compute_hash()
        while not Blockchain._is_valid_hash(computed_hash):
            # print("Generating hash:", block.nonce)
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash
    
    def submitTransaction(self):
        # Sleep a random 1-5 seconds
        # sleep_amount = random.randint(1,5)
        # print(self.name, ": Sleeping for", sleep_amount , "seconds")
        # time.sleep(sleep_amount)
        
        txn = self._createRandomTransaction()
        # Create a new block contains the new transaction
        submitted = False
        while not submitted:
            new_block = Block(
                index = self.bc.last_index() + 1,
                transactions=[txn],
                timestamp=time.time(),
                previous_hash=self.bc.last_hash(),
            )
            proof = self.generate_hash(new_block)
            # print("proof:", proof)
            if self.bc.add_block(new_block, proof):
                print("New block added:", new_block)
                submitted = True
            else:
                print("!!! Failed to submit block. Trying again...")
        print("Submitted successful transaction: ", txn)
        
        
        
    