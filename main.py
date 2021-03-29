#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import logging

PORT = 'COM5'
BAUDRATE = 460800
PIN = None

from gsmmodem.modem import GsmModem

def main():
    print('Initializing modem...')
    modem = GsmModem(PORT, 115200 )
    modem.smsTextMode = False 
    modem.connect(PIN)

    try:
        message = u'ঠিকআছে'
        modem.sendSms('01737959836' , message)
    finally:
        modem.close();

if __name__ == '__main__':
    main()