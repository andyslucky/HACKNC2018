
# This is code to be run on the Raspberry PI
import socket
import select
import threading

import serial
import os

class Client:
    def __init__(self):
        self.host = "152.23.91.121"
        self.state = 0
        self.port = 2521
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.__readthread = None
        self.COM = self.getDevice("/dev/tty.usbmodem")
        self.ser = serial.Serial(self.COM)

    def connect(self):
        # self.connection.connect((self.host,self.port))
        self.__readthread = threading.Thread(target=self.read,args=tuple([]))
        self.__readthread.start()

    def __parseinput(self,response):
        if "COMMAND" in response:
            print("accepted command")
            if "0" in response:
                print("turning off")
                return self.set_light(0)
            elif "1" in response:
                print("turning on")
                return self.set_light(1)
        elif "GET" in response:
            if "STATE" in response:
                self.connection.sendall(str(self.state).encode("utf8"))

    def read(self):
        self.connection.connect((self.host,self.port))
        while True:
            rlist,wlist,errlist = select.select([self.connection],[self.connection],[self.connection],3)
            for conn in rlist:
                response = conn.recv(128)
                # print("recieved: " + str(response))
                if response is not None and response != b"":
                    self.__parseinput(response.decode("utf8"))
                else:
                    pass

    def getDevice(self, beginsWith):
        return "/dev/cu.usbmodem1411"

        for dev in list(os.walk("/dev"))[0][2]: #shhh don't ask why
            if '/dev/' + dev[:len(beginsWith)-5] == beginsWith:
                return '/dev/' +dev
        raise Exception("Relay not connected")

    def set_light(self, state):
        sendByte = [b'o', b'O'][state]
        self.ser.write(sendByte)
        self.ser.flush()

        self.state = state
        return True

    def get_sensor_raw(self):
        val = b""

        # this line makes no sense. It does not toggle the light,
        # but without it this function doesn't work
        # self.set_light(0)
        self.ser.write(b'_')
        self.ser.flush()

        b = self.ser.read()
        while b != b"\n":
            val += b
            b = self.ser.read()
            self.ser.flush()
        return (str(val)[2:-3])

    def toggle_light(self):
        self.set_light(not self.state)

def passes(prev, curr, level):
    return prev < level < curr or curr < level < prev

client = Client()
client.connect()

import subprocess, time

lightsense = ""
soundsense = ""
tempsense = ""

start = time.time()

from matplotlib import pyplot

from random import random

import time

import numpy as np

lightHist = []
lightSensorHist = []
tempSensorHist = []

powerRating = 60

dt = 5

def toCost(J):
    return J/3600000. * .12

totalPower = 0

while True:

    subprocess.call("clear", shell=True)

    lightsense, soundsense, tempsense = client.get_sensor_raw().split()

    lightsense, soundsense, tempsense = int(lightsense), int(soundsense), int(tempsense)

    lightOn = int(client.state) #round(random()) #replace with int(client.state)

    totalPower += lightOn*dt*powerRating/3600000.

    # power

    pyplot.clf()

    lightHist.append(totalPower)
    pyplot.plot(np.arange(len(lightHist)), lightHist)

    pyplot.xlabel("time (s)")
    pyplot.ylabel("power (kW/h)")
    pyplot.title("Power Consumption")

    pyplot.savefig("plotpower.png")

    pyplot.clf()

    # light sense
    lightSensorHist.append(lightsense) #replace with lightsense
    pyplot.plot(np.arange(len(lightSensorHist)), lightSensorHist)

    pyplot.xlabel("time (s)")
    pyplot.ylabel("relative scale")
    pyplot.title("Brightness")

    pyplot.savefig("plotlightsensor.png")

    pyplot.clf()

    # tempurature sense
    tempSensorHist.append(tempsense) #replace with tempsense
    pyplot.plot(np.arange(len(tempSensorHist)), tempSensorHist)

    pyplot.xlabel("time (s)")
    pyplot.ylabel("relative scale")
    pyplot.title("Temperature")

    pyplot.savefig("plottempsensor.png")

    print("lightsense %s\nsoundsense %s\ntempsense %s" % (lightsense, soundsense, tempsense))

    time.sleep(dt)
