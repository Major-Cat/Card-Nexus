from ursina import *
import json, menu
from hashlib import sha256

app = Ursina()
usable_characters = "1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@;:?.,!*% "

class my_button(Button):
	def __init__(self,x=3.5,y=0,message="",width = 2):
		super().__init__(parent = scene, text = message, color = color.light_gray, texture = "white_cube", highlight_color = color.white, pressed_color = color.dark_gray, position = (x,y), scale = (width,0.5))

Text.size = 0.02
Text.default_resolution = 1080 * 0.05

new_name = InputField(y=-.1,x=.45,limit_content_to=usable_characters)
new_pass = InputField(y=-.16,x=.45,limit_content_to=usable_characters,hide_content=True)
new_name.next_field = new_pass

log_name = InputField(y=-.1,x=-.45,limit_content_to=usable_characters)
log_pass = InputField(y=-.16,x=-.45,limit_content_to=usable_characters,hide_content=True)
log_name.next_field = log_pass

log_in_background = Entity(parent=scene,model="quad",position=(-3.6,1.6,0.1),scale=(3,1),texture = "white_cube")
log_in = Text(text="log in",scale = 15,parent = scene, origin=(4.8,-5), background=False,color = Color(0,0,0,0.8))

sign_ip_background = Entity(parent=scene,model="quad",position=(3.6,1.6,0.1),scale=(3,1),texture = "white_cube")
sign_up = Text(text="sign up",scale = 15,parent = scene, origin=(-3.5,-5), background=False,color = Color(0,0,0,0.8))

def sign_up_function():
	username=new_name.text
	password=new_pass.text

	with open("Storage/account.json","r") as f:
		datafile = json.load(f)
	b = bytes(password, 'utf-8')
	password = sha256(b).hexdigest()
	if not(username in datafile):
		datafile[username] = str(password)
	with open("Storage/account.json","w") as f:
		json.dump(datafile, f, indent=4)

def log_in_function():
	username=log_name.text
	password=log_pass.text

	with open("Storage/account.json","r") as f:
		datafile = json.load(f)
	b = bytes(password, 'utf-8')
	password = sha256(b).hexdigest()

	try:
		if datafile[username] == password:
			scene.clear()
			menu.run(app)
	except KeyError:
		pass

sign_up_button = my_button(message="sign up")
log_in_button = my_button(x=-3.5,message = "log in")
sign_up_button.on_click = sign_up_function
log_in_button.on_click = log_in_function

app.run()