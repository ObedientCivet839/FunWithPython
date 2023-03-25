from user import Profile
from datetime import datetime


class Block:
    def __init__(self, user: Profile, data: str):
        self.user = user
        self.timestamp = datetime.now()
