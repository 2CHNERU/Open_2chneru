# -*- coding: utf-8 -*-

#######################################
#Created on Thu Jan 18 01:19:03 2024

#@author: yukih
#######################################


import serial
# import time

class Communicator:
    
    def __init__(self, com, baud_rate):
        self.ser = serial.Serial(f'COM{com}', baud_rate)
    
    
    def main(self, voltage):
        
        try:
            data = int(voltage)

        except ValueError:
            data = 'str'
        
        if data == 'str' and voltage == 'CC':
            self.ser.write(f'{0}'.encode())
            self.ser.close()
        elif data == 'str' or data > 5000:
            print('error')
        else:
            self.voltage = int(voltage)
            self.ser.write(f'{self.voltage}'.encode())


py_comm = Communicator(com=5, baud_rate=9600)

value = 0

while value != 'CC':
    
    value = input(' >> ')
    
    py_comm.main(voltage=value)

print('終了')
