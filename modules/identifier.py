import random
import string

random.seed("ibf")
#changed the identifier function into a class
def generate_identifier(length=12):
    return "".join(random.choice(string.ascii_letters) for i in range(length))
