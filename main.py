import keyboard
from playsound import playsound
import os

#keydowns = []
soundFolder = 'audio/'
extension = '.mp3'
detected = []

def callback_pressed(event):
    if(event.name in detected):
        playsound(f'{soundFolder}{event.name}{extension}', False)
    #                     NKCream/         a         .mp3
    else:
        playsound(f'{soundFolder}unknown{extension}', False)


def callback_released(event):
    pass

def fixFiles(where, ext):
    for file in os.listdir(f'./{where}'):
        if(ext in file):
            detected.append(file.split('.')[0])
            os.rename(f'./{where}/{file}', f'./{where}/{file.lower()}')
#                       ./NKCream/A.mp3     ./NKCream/a.mp3

def start(soundsFolder, ext):
    fixFiles(soundsFolder, ext)
    print(detected)
    keyboard.on_press(callback_pressed)
    keyboard.on_release(callback_released)
    keyboard.wait()

if __name__ == '__main__':
    start(soundsFolder=soundFolder , ext=extension)

"""
detected keys: a-z 0-9 - left up right down tab 'caps lock' , . / ` delete home ins pgup pgdown end F1-F7 esc 'scorll lock' pause compose windows alt 'alt gr' menu ctrl 
 unknown keys: = ' ; [ ] \
"""
