import math
import random
import datetime
import hashlib
import binascii


def hash1(msg):
    hash_object = hashlib.sha256(msg.encode("utf-8"))
    hex_dig = hash_object.hexdigest()
    return hex_dig


def genCash(include, numOfZeros):
    loop = True
    counter = 0
    random.seed(datetime.datetime.now())
    x = str(random.randint(1, 1180591620717411303424))
    while loop:
        counter = counter + 1
        solution = True
        testHash = hash1(include + ":" + x + ":" + str(counter))
        for i in range(0, numOfZeros):
            if testHash[i] != "0":
                solution = False
                break

        if solution == True:
            loop = False

    print("")
    print("Value (ProofOfWork):")
    print("")
    print(include + ":" + x + ":" + str(counter))
    print("")
    print("")
    print("Hash (Vertification):")
    print("")
    print(hash1(include + ":" + x + ":" + str(counter)))
    print("")
    print("")
    print("It took me " + "{:,}".format(counter) + " hashes to figure this out")


genCash("Hello World12341234214", 3)
