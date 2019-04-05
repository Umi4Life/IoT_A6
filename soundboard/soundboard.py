import pygame
import warnings
import serial
import serial.tools.list_ports
import time
from playsound import playsound
from pygame import mixer

mixer.init()
play = {
        '0':"oof.mp3",
        '1':"hitmarker.mp3",
        '2':"classic_hurt.mp3",
        '3':"yare-yare-daze.mp3"
        }

def connect_arduino(baudrate=250000):
    def is_arduino(p):
        return p.manufacturer is not None and 'arduino' in p.manufacturer.lower()

    ports = serial.tools.list_ports.comports()
    arduino_ports = [p for p in ports if is_arduino(p)]

    def port2str(p):
        return "%s - %s (%s)" % (p.device, p.description, p.manufacturer)

    if not arduino_ports:
        portlist = "\n".join([port2str(p) for p in ports])
        raise IOError("No Arduino found\n" + portlist)

    if len(arduino_ports) > 1:
        portlist = "\n".join([port2str(p) for p in ports])
        warnings.warn('Multiple Arduinos found - using the first\n' + portlist)

    selected_port = arduino_ports[0]
    print("Using %s" % port2str(selected_port))
    ser = serial.Serial(selected_port.device, baudrate)
    time.sleep(2)  # this is important it takes time to handshake
    return ser

def main():
    with connect_arduino(250000) as ser:
        while(True):
            read = ser.read_until(b"\n", 255).decode().strip()
            print(read)
            mixer.music.load(play[read])
            mixer.music.play()



if __name__ == '__main__':
    main()