try:
    import urllib.request as urllib2
    import urllib.error as error
except ImportError:
    import urllib2

#from urllib2 import Request, urlopen, URLError, HTTPError

def findAdmin():
    file = open("admin_panels.txt", "r")

    link = input("Enter Site Name (EX: example.com OR www.example.com): ")

    print("\n ---- AVAILABLE LINKS ---- \n")

    while True:
        subLink = file.readline().strip()
        if(not subLink):
            break
        reqLink = "http://" + link + "/" + subLink
        req = urllib2.Request(reqLink)

        try:
            response = urllib2.urlopen(req)
        except error.HTTPError as e:
            continue
        except error.URLError as e:
            continue
        else:
            print(reqLink)

findAdmin()
