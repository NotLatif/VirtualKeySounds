import keyboard
from playsound import playsound

#keydowns = []

def callback_pressed(event):
    playsounda(f'NK Cream Sounds/{event.name.upper()}.mp3')
    #name = event.name

def callback_released(event):
    pass

def start():
    keyboard.on_press(callback_pressed)
    keyboard.on_release(callback_released)
    keyboard.wait()

if __name__ == '__main__':
    start()