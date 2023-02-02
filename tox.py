import keyboard
import time
import random
import pystray
from pystray import Icon as icon, Menu as menu, MenuItem as item
from PIL import Image, ImageDraw
import sys
import configparser
from win32gui import GetWindowText, GetForegroundWindow
from threading import Thread
from io import BytesIO
import base64
import os
from pynput.keyboard import Key, Controller
import pynput.keyboard as keyb2
from icon import iconIMGB64 


os.system("title mAdE wiTh ❤️ by Epog")
state = False
key = '"'
holdKey = False
oldSystem = False

config = configparser.ConfigParser()
config.read('config.INI')

if os.path.isfile('config.INI'):
    state = config.getboolean('DEFAULT', 'onlylol')
    key = config.get('DEFAULT', 'key')
    holdKey = config.getboolean('DEFAULT', 'holdKey')
    oldSystem = config.getboolean('DEFAULT', 'oldSystem')

      
else:
    config['DEFAULT']['onlyLol'] = str(state)   
    config['DEFAULT']['key'] = str(key)   
    config['DEFAULT']['holdKey'] = str(holdKey)
    config['DEFAULT']['oldSystem'] = str(oldSystem)

with open('config.INI', 'w') as configfile:    
    config.write(configfile)



def exit_action(icon):
    icon.visible = False
    icon.stop()
    os._exit(0)

def on_clickedhold(icon, item):
    global holdKey
    holdKey = not item.checked
    config['DEFAULT']['holdKey'] = str(holdKey)

    with open('config.INI', 'w') as configfile:    
        config.write(configfile)

def on_clickedlol(icon, item):
    global state
    state = not item.checked
    config['DEFAULT']['onlyLol'] = str(state)

    with open('config.INI', 'w') as configfile:    
        config.write(configfile)

def on_clickedOld(icon, item):
    global oldSystem
    oldSystem = not item.checked
    config['DEFAULT']['onlyLol'] = str(oldSystem)

    with open('config.INI', 'w') as configfile:    
        config.write(configfile)

def on_clickedbind(icon, item):
    print("Press a Key to Bind")
    newKey = keyboard.read_event()
    print("New Key set to \""+newKey.name.upper()+"\"")

    global key
    key = newKey.name

    config['DEFAULT']['key'] = str(key)

    with open('config.INI', 'w') as configfile:    
        config.write(configfile)



iconIMG = Image.open(BytesIO(base64.b64decode(iconIMGB64)))


keyboards = Controller()


def iconStart():
    icon('test', iconIMG, menu=menu(
        item(
            "League Only?",
            on_clickedlol,
            checked=lambda item: state),
             item(
            "Hold Key?",
            on_clickedhold,
            checked=lambda item: holdKey), 

            item(
            "New Keybind (Current "+key.upper()+")",
            on_clickedbind), item(
            "Quit",
            exit_action))).run()


def startHandler():

    altHold = False

    characters = {'g': ['ģ'], 'o': ['ō', 'ø', 'ǿ'], 'n': ['ŋ', 'ň', 'ņ', 'ń', 'ń', 'ñ'], 'l': ['ľ', 'ł'], 'y': ['ý', 'ỳ', 'ŷ', 'ÿ',], 'k': ['ķ'], 'd': ['đ'], 's': ['ŝ', 'ș', 'š', 'ś'], 'u': [
        'ú', 'ù', 'ŭ', 'û', 'ů', 'ü', 'ű', 'ũ', 'ų'], 'a': ['à', 'á', 'â', 'ã', 'ä', 'å'], 'i': ['í', 'ï', 'į', 'ì', 'ĩ'], 'c': ['ċ', 'ć', 'č', 'ĉ'], 'e': ['ê', 'é', 'è', 'ë', 'ē', 'ĕ', 'ě', 'ė', 'ę']}

    text = ""

    def typeS(t):
        if t.lower() in characters:
            if t.islower():
                keyboard.press_and_release(
                    keyboard.key_to_scan_codes("backspace"))
                keyboards.type(random.choice(characters[t.lower()]))

            else:
                keyboard.press_and_release(
                    keyboard.key_to_scan_codes("backspace"))
                keyboards.type(random.choice(characters[t.lower()]).upper())

    def typeSv2(t):
        
        if t.lower() in characters:

            if t.islower():
                keyboards.type(random.choice(characters[t.lower()]))
                keyboard.press_and_release(
                    keyboard.key_to_scan_codes("backspace"))

            else:
                keyboards.type(random.choice(characters[t.lower()]).upper())
                keyboard.press_and_release(
                    keyboard.key_to_scan_codes("backspace"))


    print('Press '+key.upper()+' key and type whatever you want.') 
    while True:
        event = keyboard.read_event()

        if event.name != 'alt' and oldSystem == False and altHold == True:
                 if (event.name != 'tab'):
                    if (event.name != 'ctrl'):
                        if (event.name != 'left windows'):
                             if (event.name != "shift"):
                                if (event.name != 'caps lock'):
                                     if (event.name != 'backspace'):
                                         if (event.name != 'enter'):
                                            if (event.name != 'space'):
                                                if state==True:
                                                    if GetWindowText(GetForegroundWindow()) == "League of Legends (TM) Client":
                                                        typeSv2(event.name[0])
                                                else:
                                                    typeSv2(event.name[0])
        if event.event_type == keyboard.KEY_DOWN and event.name == key and oldSystem ==False:
            if(holdKey):
                altHold = True
            else:
                altHold = not altHold

        if event.event_type == keyboard.KEY_UP and event.name == key and altHold == True and oldSystem ==False:
            if holdKey:
                altHold = False
            
        if event.event_type == keyboard.KEY_DOWN and oldSystem ==False and altHold == True:
            if (event.name != 'alt'):
                if (event.name != 'tab'):
                    if (event.name != 'ctrl'):
                        if (event.name != 'left windows'):
                            if (event.name != "shift"):
                                if (event.name != 'caps lock'):
                                    if (event.name != 'backspace'):
                                        if (event.name != 'enter'):
                                            if (event.name != 'space'):
                                                if state==True:
                                                    if GetWindowText(GetForegroundWindow()) == "League of Legends (TM) Client":
                                                        typeS(event.name[0])
                                                else:
                                                    typeS(event.name[0])






if __name__ == '__main__':
    Thread(target=iconStart).start()
    Thread(target=startHandler).start()
