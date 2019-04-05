import serial
import time
import tkinter as tk
from scipy.spatial import distance

# matching sketch at
# https://create.arduino.cc/editor/piti118/d62e2b1e-f304-48b8-99cd-0d57f0375e1c/preview

class LabelValue(tk.Frame):
    def __init__(self, master, vname, vtext, *arg, **kwargs):
        super().__init__(master, *arg, **kwargs)
        self.label = tk.Label(text=vname)
        self.label.pack(side=tk.LEFT)
        self.value = tk.Label(textvariable=vtext)
        self.value.pack(side=tk.LEFT)


class ColourUI(tk.Frame):
    def __init__(self, parent, ser):
        super().__init__(parent)
        self.ser = ser

        topframe = tk.Frame(parent)
        frame1 = tk.Frame(parent)
        frame2 = tk.Frame(parent)
        frame3 = tk.Frame(parent)
        botframe = tk.Frame(parent)

        self.detect_button = tk.Button(topframe,
                                   text="detect colour",
                                   command=(self.detect)).pack()
        self.colour_red = tk.IntVar()
        self.colour_red_label = LabelValue(frame1, 'R:', self.colour_red)
        self.colour_red_label.pack(side=tk.TOP)
        self.colour_green = tk.IntVar()
        self.colour_green_label = LabelValue(frame2, 'G:', self.colour_green)
        self.colour_green_label.pack(side=tk.TOP)
        self.colour_blue = tk.IntVar()
        self.colour_blue_label = LabelValue(frame3, 'B:', self.colour_blue)
        self.colour_blue_label.pack(side=tk.TOP)

        self.colour = tk.IntVar()
        self.colour_label = tk.Label(botframe, textvariable=self.colour)
        self.colour_label.pack()

        topframe.pack(side=tk.TOP)
        frame1.pack(side=tk.TOP)
        frame2.pack(side=tk.TOP)
        frame3.pack(side=tk.TOP)
        botframe.pack(side=tk.BOTTOM)

    def send_rec(self, msg):
        self.ser.write((msg + "\n").encode())
        return self.ser.read_until(b"\n", 255).decode().strip()

    def detect(self):
        red = self.send_rec('red')
        self.colour_red.set(red)
        green = self.send_rec('green')
        self.colour_green.set(green)
        blue = self.send_rec('blue')
        self.colour_blue.set(blue)

        RED = (46,5,23)
        GREEN = (45,13,22)
        BLUE = (43,6,22)
        col = (int(red), int(green),int(blue))

        red_eul = distance.euclidean(RED, col)
        grn_eul = distance.euclidean(GREEN, col)
        blu_eul = distance.euclidean(BLUE, col)

        print(red_eul, grn_eul, blu_eul)

        if(red_eul<=grn_eul and red_eul<=blu_eul):
            self.colour.set("red")
        elif(grn_eul<=red_eul and grn_eul<=blu_eul):
            self.colour.set("green")
        else:
            self.colour.set("blue")


def main():
    address = "/dev/cu.usbmodem144241"  # change this to yours!!!
    baudrate = 9600  # make sure the baud rate matches
    with serial.Serial(address, baudrate) as ser:
        time.sleep(2)  # it takes a while for arduino to get ready so wait!
        root = tk.Tk()
        ui = ColourUI(root, ser)
        root.mainloop()


if __name__ == "__main__":
    main()
