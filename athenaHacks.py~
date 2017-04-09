import mraa
import time
import httplib

link = "www.python.org"
dataLib = dict()

led1_pins = 8
led2_pins = 7
led3_pins = 6
led4_pins = 4
led5_pins = 3
led6_pins = 2

led1 = mraa.Gpio(led1_pins)
led2 = mraa.Gpio(led2_pins)
led3 = mraa.Gpio(led3_pins)
led4 = mraa.Gpio(led4_pins)
led5 = mraa.Gpio(led5_pins)
led6 = mraa.Gpio(led6_pins)

led1.dir(mraa.DIR_OUT)
led2.dir(mraa.DIR_OUT)
led3.dir(mraa.DIR_OUT)
led4.dir(mraa.DIR_OUT)
led5.dir(mraa.DIR_OUT)
led6.dir(mraa.DIR_OUT)

def turnOnLed(ledNum):
    ledNum.write(1)

def turnOffLed(ledNum):
    ledNum.write(0)

def turnOffAllLed():
    l = [led1, led2, led3, led4, led5, led6]
    for i in range(6):
        l[i].write(0)

        
def getRequest(url):
    connection = httplib.HTTPConnection(url)
    connection.request("GET", "/about.html")
    r1 = connection.getresponse()
    print r1.status, r1.reason
    data1 = r1.read()
    connection.request("GET", "/parrot.spam")
    r2 = connection.getresponse()
    print r2.status, r2.reason
    connection.close()


def parseData(data):
    dotList = dataLib['data']
    for brailleDots in dotList:
        if brailleDots != "None":
            lightBrailleDot(brailleDots)    
        else:
            time.sleep(1)


def lightBrailleDot(brailleLetter):
    l = [None, led1, led2, led3, led4, led5, led6]
    for num in brailleLetter:
        turnOnLed(l[int(num)])
    time.sleep(1)
    turnOffAllLed()
    

   
getRequest(link)
dataLib["data"] = ["123", "None", "423", "6"]
parseData(dataLib);

