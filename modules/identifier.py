import random
import string

random.seed("ibf")
class identifier:
    def __init__(self):
        self.already_tooken_identifiers=[]
    def generate_identifier(length:int =12):
        return "".join(random.choice(string.ascii_letters) for i in range(length))
