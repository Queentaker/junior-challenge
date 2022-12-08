import random
import string

random.seed("ibf")
#changed the identifier function into a class
class Identifier:

    def __init__(self):
        self.__already_took_identifiers=[]

    def generate_unique_identifier(self, length:int =12):
        random_identifier="".join(random.choice(string.ascii_letters) for i in range(length))

        while random_identifier in self.__already_took_identifiers:
            random_identifier="".join(random.choice(string.ascii_letters) for i in range(length))
        self.__already_took_identifiers.append(random_identifier)

        return random_identifier
