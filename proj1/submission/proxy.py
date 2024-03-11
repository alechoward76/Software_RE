# Alec Howard
# 1/24/2024
# Proxy For Evil Corp's Message Encryption System

import requests
import urllib3

# Disable SSL Warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {"X-API-KEY": "8DEC7CF5226BEA6A6E92CAC30A465384"}
url = "https://p1.sre.tuctf.com/"


# Make server Connection
def WebRequestMotd():
    """Make a request to the server to get the message of the day"""
    response = requests.get(url + "motd", headers=headers, verify=False)
    ReadResponseCode(response.status_code)
    motd(response.text)


def PostMotd():
    """Post a message to the server to replace the message of the day"""

    motd = "Alec Was Here"
    data = {"motd": motd}
    headers = {
        "X-API-KEY": "8DEC7CF5226BEA6A6E92CAC30A465384",
        "Content-Type": "application/json; utf-8",
        "Accept": "application/json",
    }
    response = requests.post(url + "set_motd", headers=headers, json=data)
    ReadResponseCode(response.status_code)
    print(response.text)


def WebRequestEncrypt(message, key):
    """Post a message to the server to be encrypted"""
    # Create an object tp hold the message and key
    data = {"message": message, "key": key}
    # set the header to include api key, content type, and accept

    headers = {
        "X-API-KEY": "8DEC7CF5226BEA6A6E92CAC30A465384",
        "Content-Type": "application/json; utf-8",
        "Accept": "application/json",
    }

    response = requests.post(url + "encrypt", headers=headers, json=data)
    ReadResponseCode(response.status_code)
    encryptedMessage(response.text)


def encryptedMessage(resp):
    """Decode & Print the encrypted message"""
    # decode the bytes returned
    print(resp.encode("utf-8").decode("unicode_escape"))


def ReadResponseCode(code):
    """Read the response code and print a message if it is not 200"""
    if code == 200:
        pass
    else:
        print("Connection Failed\n")


def motd(resp):
    """Print the message of the day"""
    print(resp)


def ReceiveMessage():
    """Get message and key from user and send to server"""
    while True:
        print("Message: ", end="")
        message = input()
        print("Key: ", end="")
        key = input()
        while not key.isdigit():
            print("Invalid Key")
            print("Message: ", end="")
            message = input()
            print("Key: ", end="")
            key = input()

        key = int(key) % 255
        WebRequestEncrypt(message, key)


# Create main
def main():
    """Main function"""

    # PostMotd()
    print("Welcome to the Proxy Server for Evil Corp's Message Encryption System!\n")
    WebRequestMotd()
    ReceiveMessage()


# Call main
if __name__ == "__main__":
    main()
