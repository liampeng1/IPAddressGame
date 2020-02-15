import ipaddress
import random

NETMASKS = [8, 16, 24]

def getRandIPAddress():
    global NETMASKS
    randIPAddressString = ""
    for i in range(4):
        randIPAddressString += str(random.randint(0, 255)) + "."
    randIPAddressString = randIPAddressString[:-1]
    randIPAddress = ipaddress.IPv4Address(randIPAddressString)
    return randIPAddress

def addressToNetowrk(randIPAddress, randNetmask):
    ipNums = str(randIPAddress).split('.')
    i = 3
    hostNetMask = 32 - randNetmask
    while hostNetMask > 0:
        ipNums[i] = '0'
        i -= 1
        hostNetMask -= 8
    networkString = '.'.join(ipNums) + '/' + str(randNetmask)
    return ipaddress.IPv4Network(networkString)

def getRandNetmask():
    return random.choice(NETMASKS)

def playNumHosts():
    netmask = random.choice(NETMASKS)
    hosts = 2 ** (32 - netmask)
    ans = input("What netmask can accomodate " + str(hosts) + " hosts? : /")
    if ans == str(netmask):
        print ("Correct!")
    else:
        print ("Wrong!")
    print ("The answer is /"+str(netmask))

def playNetAddress():
    randIPAddress = getRandIPAddress()
    randNetmask = getRandNetmask()
    ipNetowrk = addressToNetowrk(randIPAddress, randNetmask)
    ipNetworkAddress = str(ipNetowrk).split('/')[0]
    ans = input("What is the network address if a host's IP Address is " + str(randIPAddress) + "/" + str(randNetmask) + "?\r\nEnter Here : ")
    if ans == ipNetworkAddress:
        print ("Correct!")
    else:
        print ("Wrong!")
    print ("The correct answer is : " + ipNetworkAddress)

def getAddressRange(ipNetwork):
    [min, netmask] = str(ipNetwork).split('/')
    ipNums = str(min).split('.')
    i = 3
    hostNetMask = 32 - int(netmask)
    while hostNetMask > 0:
        ipNums[i] = '255'
        i -= 1
        hostNetMask -= 8
    max = ipaddress.IPv4Address('.'.join(ipNums))
    return [ipaddress.IPv4Address(min), max]

def playAddressRange():
    randIPAddress = getRandIPAddress()
    randNetmask = getRandNetmask()
    ipNetwork = addressToNetowrk(randIPAddress, randNetmask)
    print("What is the range of hosts for this Network " + str(ipNetwork) + " ?")
    [min, max] = getAddressRange(ipNetwork)
    minAns = input("Enter the range min address : ")
    maxAns = input("Enter the range max address : ")
    if minAns == str(min) and maxAns == str(max):
        print ("Correct!")
    else:
        print ("Wrong!")
    print ("The answers are :")
    print ("\tmin : " + str(min))
    print ("\tmax : " + str(max))

def playSubnetMemb():
    ipNetwork1 = addressToNetowrk(getRandIPAddress(), getRandNetmask())
    ipNetwork2 = addressToNetowrk(getRandIPAddress(), getRandNetmask())
    netmask1 = int(str(ipNetwork1).split("/")[1])
    netmask2 = int(str(ipNetwork2).split("/")[1])
    isSubnet = False
    if netmask1 > netmask2:
        subnets = list(ipNetwork2.subnets(new_prefix=netmask1))
        isSubnet = False
        for subnet in subnets:
            if ipNetwork1 == subnet:
                isSubnet = True
    ansNum = input("Is " + str(ipNetwork1) + " a subnet of " + str(ipNetwork2) + " ? (Yes : 1 , No : 2) : ")
    ans = int(ansNum) == 1
    if isSubnet == ans:
        print("Correct!")
    else:
        print("Wrong!")

def main():
    playAgain = True
    while (playAgain):
        print ("Games:")
        print ("\t1) Number of Hosts")
        print ("\t2) Network Address")
        print ("\t3) Address Range")
        print ("\t4) Subnet Membership")
        gameNum = int(input("Enter your choice (Number) here : "))
        if gameNum == 1:
            playNumHosts()
        if gameNum == 2:
            playNetAddress()
        if gameNum == 3:
            playAddressRange()
        if gameNum == 4:
            playSubnetMemb()
        playAgainResp = input("Do you want to play again? Yes : 1 , No : 2\r\n")
        playAgain = int(playAgainResp) == 1
    print ("Bye")

if __name__== "__main__":
    main()
