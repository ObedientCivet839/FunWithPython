import random
from lib.user import Profile
from lib.block import Block, Blockchain, Transaction
import time
from datetime import datetime

# DONE(P1): Implement a store with multiple users and multiple transactions at the same time.
# Each time, a transaction needs to create a new valid block and create a proof.
# Then, they will apply to the server to create a new block.

# DONE(P2): Using Adapter, implements different types of transactions
# Adapter is making the custom inputs to look like each other.
class ActionTransaction(Transaction):
    def __init__(self, from_user: Profile, to_user: Profile, action: str):
        super().__init__(from_user, to_user, "")
        self.from_user = from_user
        self.to_user = to_user
        self.action = action
    
    def description(self):
        desc = '{} {} {}'.format(self.from_user.name.firstlast(), self.action.lower(), self.to_user.name.firstlast())
        return desc

    def __str__(self):
        return self.description()

# Using decorators to append application name and timestamp to the description
class ApplicationTxnDecorator:
    def __init__(self, app: str, txn: Transaction):
        self.app = app
        self.transaction = txn
    
    def description(self):
        return '{}: {}'.format(self.app, self.transaction.description())
    
    def __str__(self):
        return self.description()

class TimestampedTxnDecorator:
    def __init__(self, txn):
        self.transaction = txn
        self.timestamp = str(datetime.now())
    
    def description(self):
        return '{}: {}'.format(self.timestamp, self.transaction.description())

    def __str__(self) -> str:
        return self.description()

class MoneyTransaction(Transaction):
    def __init__(self, amount: int, currency: str):
        pass

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
        
        action_txn = ActionTransaction(user1, user2, action)
        timestamped_decorator = TimestampedTxnDecorator(action_txn)
        app_decorator = ApplicationTxnDecorator(self.name, timestamped_decorator)
        return timestamped_decorator
    
    def submitTransaction(self, sleep = False):
        if sleep:
            # Sleep a random 1-5 seconds
            sleep_amount = random.randint(1,5)
            print(self.name, ": Sleeping for", sleep_amount , "seconds")
            time.sleep(sleep_amount)
        
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
            proof = self.bc.generate_hash(new_block)
            # print("proof:", proof)
            if self.bc.add_block(new_block, proof):
                print("New block added:", new_block)
                submitted = True
            else:
                print("!!! Failed to submit block. Trying again...")
        print("Submitted successful transaction: ", txn)
    