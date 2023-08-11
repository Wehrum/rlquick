from time import sleep
from inputs import get_gamepad
import math
import threading
from pynput.keyboard import Key, Controller

keyboard = Controller()

def keywriter(timer, string):
    keyboard.press("t")
    sleep(timer)
    # keyboard.release('T')
    for item in string:
        if(item.isupper()):
            keyboard.press(Key.shift)
            keyboard.press(str(item))
            keyboard.release(str(item))
            keyboard.release(Key.shift)
            sleep(timer)
        else:
            keyboard.press(str(item))
            keyboard.release(str(item))
            sleep(timer)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

class XboxController(object):
    MAX_TRIG_VAL = math.pow(2, 8)
    MAX_JOY_VAL = math.pow(2, 15)

    def __init__(self):

        self.LeftJoystickY = 0
        self.LeftJoystickX = 0
        self.RightJoystickY = 0
        self.RightJoystickX = 0
        self.LeftTrigger = 0
        self.RightTrigger = 0
        self.LeftBumper = 0
        self.RightBumper = 0
        self.A = 0
        self.X = 0
        self.Y = 0
        self.B = 0
        self.LeftThumb = 0
        self.RightThumb = 0
        self.Back = 0
        self.Start = 0
        self.LeftDPad = 0
        self.RightDPad = 0
        self.UpDPad = 0
        self.DownDPad = 0

        self._monitor_thread = threading.Thread(target=self._monitor_controller, args=())
        self._monitor_thread.daemon = True
        self._monitor_thread.start()

    def read(self): # return the buttons/triggers that you care about in this methode
        rb = self.RightBumper
        left = self.LeftDPad
        up = self.UpDPad
        # if(left == -1):
        #     print("Left was pressed")
        # if(left == 1):
        #     print("Right was pressed")
        # if(up == -1):
        #     print("Up was pressed")
        # if(up == 1):
        #     print("Down was pressed")
        if(left == -1 and rb == 1): # Left
            keywriter(0.0005, "I don't understand why you have to be toxic, it's just a game..")
        if(left == 1 and rb == 1): # Right
            keywriter(0.0005, "OwO")
        if(up == -1 and rb == 1): # Up
            keywriter(0.0005, "RawRRR XDD")
        if(up == 1 and rb == 1): # Down
            keywriter(0.0005, "Sorry for my utter failure at whiffing, I suck sometimes! :O")
        return [left, up, rb]

    def _monitor_controller(self):
        while True:
            events = get_gamepad()
            for event in events:
                if event.code == 'ABS_Y':
                    self.LeftJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_X':
                    self.LeftJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RY':
                    self.RightJoystickY = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_RX':
                    self.RightJoystickX = event.state / XboxController.MAX_JOY_VAL # normalize between -1 and 1
                elif event.code == 'ABS_Z':
                    self.LeftTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'ABS_RZ':
                    self.RightTrigger = event.state / XboxController.MAX_TRIG_VAL # normalize between 0 and 1
                elif event.code == 'BTN_TL':
                    self.LeftBumper = event.state
                elif event.code == 'BTN_TR':
                    self.RightBumper = event.state
                elif event.code == 'BTN_SOUTH':
                    self.A = event.state
                elif event.code == 'BTN_NORTH':
                    self.Y = event.state #previously switched with X
                elif event.code == 'BTN_WEST':
                    self.X = event.state #previously switched with Y
                elif event.code == 'BTN_EAST':
                    self.B = event.state
                elif event.code == 'BTN_THUMBL':
                    self.LeftThumb = event.state
                elif event.code == 'BTN_THUMBR':
                    self.RightThumb = event.state
                elif event.code == 'BTN_SELECT':
                    self.Back = event.state
                elif event.code == 'BTN_START':
                    self.Start = event.state
                elif event.code == 'ABS_HAT0X':
                    self.LeftDPad = event.state
                elif event.code == 'ABS_HAT0X':
                    self.RightDPad = event.state
                elif event.code == 'ABS_HAT0Y':
                    self.UpDPad = event.state
                elif event.code == 'ABS_HAT0Y':
                    self.DownDPad = event.state




if __name__ == '__main__':
    joy = XboxController()
    while True:
        joy.read()