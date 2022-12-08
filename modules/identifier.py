import random
import string

random.seed("ibf")
class Identifier(object):
    instance = None


    def __init__(self):
        self.__already_tooken_identifiers=[]

    def generate_identifier(self,length:int =12):
        random_identifier="".join(random.choice(string.ascii_letters) for i in range(length))

        while random_identifier in self.__already_tooken_identifiers:
            random_identifier="".join(random.choice(string.ascii_letters) for i in range(length))
        self.__already_tooken_identifiers.append(random_identifier)
        return random_identifier
