from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### Hardware ###
redled = LED(14)
greenled = LED(18)
blueled = LED(24)

### GUI Definitons ###
win = Tk()
win.title("5.2C")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")
frame = Frame(win)
frame.pack()
r = StringVar(win,"red")

### Event Functions ###
def GreenledToggle():
        greenled.on()
        redled.off()
        blueled.off()
        
def BlueledToggle():
        blueled.on()
        redled.off()
        greenled.off()
        
        
def RedledToggle():
        redled.on()
        blueled.off()
        greenled.off()
        
def close():
    RPi.GPIO.cleanup()
    win.destroy()
    
### Widgets ###
redledButton = Radiobutton(frame, text = 'Turn RED LED ON', font = myFont, command = RedledToggle, variable = r, value = 1)
redledButton.pack(anchor = W)

greenledButton = Radiobutton(frame, text = 'Turn GREED LED ON', font = myFont, command = GreenledToggle, variable = r, value = 2)
greenledButton.pack(anchor = W)

blueledButton = Radiobutton(frame, text = 'Turn BLUE LED ON', font = myFont, command = BlueledToggle, variable = r, value = 3)
blueledButton.pack(anchor = W)

exitButton = Button(win, text = 'Exit', font = myFont, command = close, bg = 'red', height = 1, width = 6)
exitButton.pack(padx = 5, pady = 5)

### Exit cleanly ###
win.protocol("WM_DELETE WINDOW", close)

### Loop forever ###
win.mainloop()
    
