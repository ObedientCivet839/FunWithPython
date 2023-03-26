from lib.block import Block, Blockchain, Transaction
from lib.user import createProfile
from apps.store import Application

import threading

def runStores():
    user1 = createProfile("Harry", "J", "Potter", '1990-09-19')
    user2 = createProfile("Ron", "A", "Weasley", '1989-03-11')
    user3 = createProfile("Hermione", "C", "Ranger", '1989-04-01')
    user4 = createProfile("Draco", "M", "Malfoy", '1990-08-01')

    # Creating a new blockchain
    bc = Blockchain()
    
    amazon = Application(
        "Amazon",
        [user1, user2, user3, user4],
        ["Buy eggs", "Sell shoes", "Buy earpods"],
        bc)
    google = Application(
        "Google",
        [user1, user2, user3, user4],
        ["Buy phone", "Sell phone", "Pay photos"],
        bc)
    
    def multipleSubmit(fn, times):
        for i in range(times):
            fn()
    
    # DONE(P1): Multi-thread support
    t1 = threading.Thread(target=multipleSubmit, args=(amazon.submitTransaction, 10))
    t2 = threading.Thread(target=multipleSubmit, args=(google.submitTransaction, 10))
    
    # Start 2 threads
    t1.start()
    t2.start()
    
    # Wait until 2 threads are completely executed
    t1.join()
    t2.join()
    
    print("Blockchain of size:", len(bc.chain))
    # for b in bc.chain:
    #     print(b)

def main():
    runStores()

if __name__ == "__main__":
    main()