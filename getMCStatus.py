import json 
from mcstatus import JavaServer

serverList = [["The 1.7.10 Pack", "1710.aberrantwinds.xyz"], ["ROTN", "rotn.aberrantwinds.xyz"], ["RAD2", "RAD2.aberrantwinds.xyz"], ["Fake", "notarealip.aberrantwinds.xyz"], ["Edge of Infinity", "eoi.aberrantwinds.xyz"]]
serverPingableList = serverList
serverDict = dict()

def pingServers():
    counter = 0
    for ip in serverList:
        try:
            server = JavaServer.lookup(ip[1])
            server.ping()
        except IOError:
            serverPingableList.pop(counter)
            print(f"Server not available: {ip[1]}")

        counter += 1
        

def getStatus():
    i = 0
    for ip in serverPingableList:
        serverLabel = "server" + str(i)
        try:
            server = JavaServer.lookup(ip[1])
            status = server.status()

            serverDict[serverLabel] = dict()
            serverDict[serverLabel]["name"] = ip[0]
            serverDict[serverLabel]["ip"] = ip[1]
            serverDict[serverLabel]["players"] = status.players.online
            serverDict[serverLabel]["ping"] = status.latency

        except IOError:
            print(f"Invalid IP: {ip[1]}")

        i += 1

def writeToFile():
    with open('my_json.json', 'w') as fp:
            json.dump(serverDict, fp)

    fp.close()

def readFromFile():
    file = open('my_json.json')

    data = json.load(file)

    print(data)

def main():
    pingServers()
    getStatus()
    writeToFile()
    readFromFile()


if __name__ == "__main__":
    main()

