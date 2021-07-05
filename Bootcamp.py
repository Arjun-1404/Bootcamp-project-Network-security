
# All 3 projects included
import string
import pbkdf2
import hashlib
print("==============================")
print("Welcome to Algorithm Converter")
print("==============================\n")

var1 = input("Enter text to be converted : ")
alphabet = string.printable

# Md5 is first output for the first project and for 2nd project next 3 outputs sha1,blake2s,sha384 are taken


def md5():
    y = var1.encode("utf-8")
    z = hashlib.md5(y)
    a = z.hexdigest()
    print(a)

# Project 2


def sha1():
    y = var1.encode("utf-8")
    z = hashlib.sha1(y)
    a = z.hexdigest()
    print(a)


def blake2s():
    y = var1.encode("utf-8")
    z = hashlib.blake2s(y)
    a = z.hexdigest()
    print(a)


def sha384():
    y = var1.encode("utf-8")
    z = hashlib.sha384(y)
    a = z.hexdigest()
    print(a)

# Project 3 Iterate and Salting


def iterate():
    y = var1.encode("utf-8")
    a = hashlib.md5(y)
    b = a.hexdigest()
    z = pbkdf2.crypt(b, iterations=4)
    print(z)


def salt():

    for i in var1:
        position = alphabet.find(i)
        new_position = position + 3
        encrypt = alphabet[new_position]
        print(encrypt.lower(), end="")


print("\nThe MD5 hash is : ", end="")
md5()
print("=======================")
print("The sha1 hash is :", end="")
sha1()
print("=======================")
print("The blake2s hash is : ", end="")
blake2s()
print("=======================")
print("The sha384 hash is :", end="")
sha384()
print("=======================")
print("The iterated hash is : ", end="")
iterate()
print("=======================")
print("The Salted hash is : ", end="")
salt()
print("\n=======================")
