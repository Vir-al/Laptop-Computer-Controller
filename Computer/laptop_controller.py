# Laptop Controller
# Viral Limbani

# Basic Remote Controller for any omputer or laptop from mobile phone(Both should be conneted to the same local netwrok ie. WIFI/LAN)

import socket
import json
from pynput.mouse import Button, Controller as mController
from pynput.keyboard import Key, Controller as kController,KeyCode
import wmi

############ Constants ############

VK_VOLUME_MUTE = 0xAD
VK_VOLUME_DOWN = 0xAE
VK_VOLUME_UP = 0xAF
VK_MEDIA_NEXT_TRACK = 0xB0
VK_MEDIA_PREV_TRACK = 0xB1
VK_MEDIA_PLAY_PAUSE = 0xB3
VK_MEDIA_STOP = 0xB2
MUTE_FLAG = True

############ Controllers ############
mouse = mController()
keyboard = kController()


############ Actions ############
# To add your custom Actions
# Write the function below the performAction(function) containing the procedure for the Action
# make elif statment with the unique Action name
# Call the function inside the if statment fo particular Action
# You can set multiple ations in one if statment to make a routine
# For Eg. Action == 'Good Morning'
# 			playMusicList()
# 			openNewsInBrowser()

def performAction(data):
	if data['action'] == 'mouse_move':
		mouseMove(data['delx'],data['dely'])
	elif data['action'] == 'left_click':
		mouseClick(Button.left)
	elif data['action'] == 'double_click':
		mouseClick(Button.left,2)
	elif data['action'] == 'right_click':
		mouseClick(Button.right)
	elif data['action'] == 'scroll_click':
		mouseClick(Button.middle)
	elif data['action'] == 'scroll_up':
		mouseScroll(True,5)
	elif data['action'] == 'scroll_down':
		mouseScroll(False,5)
	elif data['action'] == 'volume_up':
		volume(True)
	elif data['action'] == 'volume_down':
		volume(False)
	elif data['action'] == 'mute':
		global MUTE_FLAG
		if MUTE_FLAG:
			mute()
			MUTE_FLAG = False
	elif data['action'] == 'unmute':
		if not MUTE_FLAG:
			mute()
			MUTE_FLAG = True
	elif data['action'] == 'brightness_up':
		brightness(10)
	elif data['action'] == 'brightness_down':
		brightness(-10)
	elif data['action'] == 'dim':
		bright(False)
	elif data['action'] == 'bright':
		bright(True)
	elif data['action'] == 'previous_track':
		changeTrack(previous = True)
	elif data['action'] == 'next_track':
		changeTrack(previous = False)
	elif data['action'] == 'play_pause':
		play(stop = False)
	elif data['action'] == 'stop_track':
		play(stop = True)

############ Functions ############
# Write your custom Functions for Actions or routine here
def mouseMove(delx, dely):
	mouse.move(delx, dely)

def mouseClick(b,c = 1):
	mouse.click(b,c)

def mouseScroll(up, intensity):
	if up:
		mouse.scroll(0,10 * intensity)
	else:
		mouse.scroll(0,-10 * intensity)

def volume(up):
	if up:
		keyboard.press(KeyCode.from_vk(VK_VOLUME_UP))
		keyboard.release(KeyCode.from_vk(VK_VOLUME_UP))
	else:
		keyboard.press(KeyCode.from_vk(VK_VOLUME_DOWN))
		keyboard.release(KeyCode.from_vk(VK_VOLUME_DOWN))

def mute():
	keyboard.press(KeyCode.from_vk(VK_VOLUME_MUTE))
	keyboard.release(KeyCode.from_vk(VK_VOLUME_MUTE))

def brightness(intensity):
	brightness = wmi.WMI(namespace='wmi').WmiMonitorBrightness()[0].currentBrightness + intensity
	if brightness >= 0 and brightness <= 100:
		wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(brightness, 0)

def bright(flag):
	if(flag):
		wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(100, 0)
	else:
		wmi.WMI(namespace='wmi').WmiMonitorBrightnessMethods()[0].WmiSetBrightness(0, 0)

def changeTrack(previous):
	if previous:
		keyboard.press(KeyCode.from_vk(VK_MEDIA_PREV_TRACK))
		keyboard.release(KeyCode.from_vk(VK_MEDIA_PREV_TRACK))
	else:
		keyboard.press(KeyCode.from_vk(VK_MEDIA_NEXT_TRACK))
		keyboard.release(KeyCode.from_vk(VK_MEDIA_NEXT_TRACK))

def play(stop = False):
	if stop:
		keyboard.press(KeyCode.from_vk(VK_MEDIA_STOP))
		keyboard.release(KeyCode.from_vk(VK_MEDIA_STOP))
	else:
		keyboard.press(KeyCode.from_vk(VK_MEDIA_PLAY_PAUSE))
		keyboard.release(KeyCode.from_vk(VK_MEDIA_PLAY_PAUSE))

# DO NOT ALTER THE CODE BELOW THIS LINE UNLESS YOU KNOW EXATLY HOW IT WORKS
# You need to know,
# 1. Python socket programming: https://docs.python.org/2/howto/sockets.html
# 2. JSON in python: https://docs.python.org/2/library/json.html


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created")

port = 443
connection.bind((socket.gethostbyname(socket.gethostname()),port))
print("Socket Bind on ", socket.gethostbyname(socket.gethostname()))

connection.listen(2)
print("Listening for incoming connection")

flag = True
while(flag):
	conn, addr = connection.accept()
	data = conn.recv(1024).decode()
	performAction(json.loads(data))
	conn.close()
	# Printing the actions recieved from the mobile device
	print(str(data))

