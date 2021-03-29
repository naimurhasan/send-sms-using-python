"""
sms.py - Used to send txt messages.
"""
import serial
import time
 
class TextMessage:
    def __init__(self, recipient="111", message="u"):
        self.recipient = recipient
        self.content = message
 
    def setRecipient(self, number):
        self.recipient = number
 
    def setContent(self, message):
        self.content = message
 
    def connectPhone(self):
        self.ser = serial.Serial('COM5', 460800, timeout=5)
        time.sleep(1)
 
    def sendMessage(self):
        self.ser.write('ATZ\r'.encode())
        time.sleep(1)
        self.ser.write('AT+CMGF=1\r'.encode())
        time.sleep(1)
        self.ser.write('''AT+CMGS="'''.encode() + '01737959836'.encode()  + '''"\r'''.encode())
        time.sleep(1)
        self.ser.write('Hi'.encode(encoding='UTF-8',errors='strict') + "\r".encode())
        time.sleep(1)
        self.ser.write(chr(26).encode())
        time.sleep(1)
 
    def disconnectPhone(self):
        self.ser.close()

# if __name__ == '__main__':

sms = TextMessage()
sms.connectPhone()
sms.sendMessage()
sms.disconnectPhone()

print('Message sent');