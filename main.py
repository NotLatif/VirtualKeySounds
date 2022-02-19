import keyboard

keydowns = []

def callback_pressed(event):
    name = event.name
    print(name)

def callback_released(event):
    pass

def start():
    keyboard.on_press(callback_pressed)
    keyboard.on_release(callback_released)
    keyboard.wait()

if __name__ == '__main__':
    start() 


