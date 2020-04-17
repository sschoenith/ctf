#!usr/bin/python3

import json
import base64
import requests

#example to reverse XOR key from cookie & default data in source code
cookie = 'ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw='
print('Default cookie value = ' + cookie)
#cookie = input("Enter cookie value sent: ")
defaultData = '{"showpassword":"no", "bgcolor":"#ffffff"}'
print('Default values being sent = ' + defaultData)
#defaultData = input("Enter json array sent to server: ")
defaultData = json.loads(defaultData)

def reversedXORkey(cookie, defaultData):
    base64Decoded = base64.b64decode(cookie).decode('utf8')
    jsonPayload = json.dumps(defaultData, separators=(',', ':'), ensure_ascii=False)
    #XOR two strings. Figure out proper way to do this
    return ''.join(chr(ord(a) ^ ord(b)) for a,b in zip(base64Decoded,jsonPayload))

print('Reversed XOR value looks like = ' + reversedXORkey(cookie, defaultData))
xorKey = reversedXORkey(cookie, defaultData)[:4]
print ('XOR Key appears to be: ' + xorKey)


newData = '{"showpassword":"yes", "bgcolor":"#ffffff"}'
newData = json.loads(newData)

def xorEncrypt(newData, xorKey):
    output = []
    for i in range(len(newData)):
        xor = ord(newData[i]) ^ ord(xorKey[i % len(xorKey)])
        output.append(chr(xor))
    xorEncrypted = ''.join(output)
    return xorEncrypted

def updatedCookie(newData, xorKey):
    newData = json.dumps(newData, separators=(',', ':'), ensure_ascii=False)
    newCookieValue = base64.b64encode(xorEncrypt(newData, xorKey).encode('utf8'))
    return newCookieValue.decode('utf8')

sendtoBurp = str(updatedCookie(newData, xorKey))
print ('Use this updated cookie while intercepting traffic: ' + sendtoBurp)
