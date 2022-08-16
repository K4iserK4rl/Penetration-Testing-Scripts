import hashlib

wordlistLocation = str(input("Enter wordlist file location: "))
hashInput = str(input("Enter hash to be cracked: "))

numBits = len(str((bin(int(hashInput, 16))))[2:])

with open(wordlistLocation, 'r') as file:
    for line in file.readlines():
        if(numBits == 128):
            hashOb = hashlib.md5(line.strip().encode())
        elif(numBits == 160):
            hashOb = hashlib.sha1(line.strip().encode())
        elif(numBits == 224):
            hashOb = hashlib.sha224(line.strip().encode())
        elif(numBits == 255 or numBits == 256):
            hashOb = hashlib.sha256(line.strip().encode())
        elif(numBits == 384):
            hashOb = hashlib.sha384(line.strip().encode())
        elif(numBits == 512):
            hashOb = hashlib.sha512(line.strip().encode())
        hashPass = hashOb.hexdigest()
        if hashPass == hashInput:
            print("Found cleartext password: " + line.strip())
            exit(0)
