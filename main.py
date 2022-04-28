from ursina import *	#the graphics engine
import json, menu		#json for log ins, menu for moving to the next screen
from hashlib import sha256	#for hashing the passwords

app = Ursina()	#activates ursina
window.fps_counter.enabled = False	#stops ursina's default FPS counter in the top corner from being made
usable_characters = "1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@;:?.,!*% "	#characters that can be used in passwords

class my_button(Button):	# The button I will use instead of the default
	def __init__(self,x=3.5,y=0,message="",width = 2):
		super().__init__(parent = scene, text = message, color = color.light_gray, texture = "white_cube",
highlight_color = color.white, pressed_color = color.dark_gray, position = (x,y), scale = (width,0.5))	#all of the default values from the super class

Text.size = 0.02	#sets a text size that works well for the places I'm using it
Text.default_resolution = 1080 * 0.05 	#sets the resoultion of the text

new_name = InputField(y=-.1,x=.45,limit_content_to=usable_characters)	#sign up user names
new_pass = InputField(y=-.16,x=.45,limit_content_to=usable_characters,hide_content=True)	#sign up password
new_name.next_field = new_pass	#links both inputs together so you can press tab to go between them

log_name = InputField(y=-.1,x=-.45,limit_content_to=usable_characters)
log_pass = InputField(y=-.16,x=-.45,limit_content_to=usable_characters,hide_content=True)
log_name.next_field = log_pass

log_in_background = Entity(parent=scene,model="quad",position=(-3.6,1.6,0.1),scale=(3,1),texture = "white_cube")	#coloured screen for the header text to sit on
log_in = Text(text="log in",scale = 15,parent = scene, origin=(4.8,-5), background=False,color = Color(0,0,0,0.8))	#text to show which boxes are for logins or sign ups

sign_ip_background = Entity(parent=scene,model="quad",position=(3.6,1.6,0.1),scale=(3,1),texture = "white_cube")
sign_up = Text(text="sign up",scale = 15,parent = scene, origin=(-3.5,-5), background=False,color = Color(0,0,0,0.8))

def sign_up_function():	#stores the new sign up
	username=new_name.text
	password=new_pass.text

	with open("Storage/account.json","r") as f:
		datafile = json.load(f)
	b = bytes(password, 'utf-8')
	password = sha256(b).hexdigest()	#hashes the input password
	if not(username in datafile):	#prevents a user being overwritten
		datafile[username] = str(password)
	with open("Storage/account.json","w") as f:
		json.dump(datafile, f, indent=4) 

def log_in_function():	#logs users in
	username=log_name.text
	password=log_pass.text

	with open("Storage/account.json","r") as f:
		datafile = json.load(f)	#searches fot the username
	b = bytes(password, 'utf-8')
	password = sha256(b).hexdigest()

	try:
		if datafile[username] == password:
			scene.clear()
			menu.run(app)	#changes to the menu screen
	except KeyError:	#if username doesnt exist
		pass

sign_up_button = my_button(message="sign up")
log_in_button = my_button(x=-3.5,message = "log in")
sign_up_button.on_click = sign_up_function	#assigns the functions to the buttons when clicked
log_in_button.on_click = log_in_function

app.run()
