"""
Summer 2018

This script generates a first name, last name, and fake email address based on
the generated names. It returns the generated info in a tuple with the form:
(first_name, last_name, email)
"""

from faker import Faker
import time
import random

def rand_email(verbose = False):
    # pull from list of known fake domains
    f = open('refined-email-domains.txt')
    lines = f.readlines()

    # initialize and seed the faker with current time
    fake = Faker()
    fake.seed(int(time.time()*10000))
    name = fake.name()

    # ensure the name generated is a standard one (no Dr., Jr., Sr, etc.)
    while len(name.split(" ")) != 2:
        name = fake.name()

    names = name.split(' ')
    email = names[0] + '.' + names[1] + '@' + random.choice(lines)
    if verbose:
        print(names[0], names[1], email)
    return names[0], names[1], email


if __name__ == "__main__":
    for i in range(50):
        rand_email()
