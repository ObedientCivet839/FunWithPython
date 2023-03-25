from block import Block
from user import createProfile

def main():
    user = createProfile("Harry", "J", "Potter", '1990-09-19')
    block1 = Block(user, "block1")
    print(block1)

if __name__ == "__main__":
    main()