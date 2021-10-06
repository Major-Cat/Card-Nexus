from ursina import *
import json
from hashlib import sha256

app = Ursina()
usable_characters = "1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@;:?.,!*% "

class usable_button(Button):
	def __init__(self,x=5,y=-1.2,message="",width = 1.5):
		super().__init__(
			parent = scene,
			text = message,
			color = color.light_gray,
			texture = "white_cube",
			highlight_color = color.white,
			pressed_color = color.dark_gray,
			position = (x,y),
			scale = (width,1)
			)

	def sign_up_function(self,username,password):
		print(self.hovered,"hover")
		if self.hovered and held_keys["left mouse"]:
			with open("Storage/temp_storage.json","r") as f:
				datafile = json.load(f)
			b = bytes(password, 'utf-8')
			password = sha256(b).hexdigest()
			datafile[username] = str(password)
			with open("Storage/temp_storage.json","w") as f:
				json.dump(datafile, f, indent=4)

	def log_in_function(self,username,password):
		if self.hovered and held_keys["left mouse"]:
			with open("Storage/temp_storage.json","r") as f:
				datafile = json.load(f)
			b = bytes(password, 'utf-8')
			password = sha256(b).hexdigest()
			log_in = False
			for i in datafile:
				if i[1] == password:
					log_in = True 	#gonna have to have this run the next file
			#if log_in == False:

	#def guest_mode(self):
		#if self.hovered and held_keys["left mouse"]:
		#	pass 	#this will also just run the next file or something that I'll adjust based on what the other files want passed to them


#def run():
Text.size = 0.02
Text.default_resolution = 1080 * 0.05

new_name = InputField(y=.02,x=.45,limit_content_to=usable_characters)
new_pass = InputField(y=-.04,x=.45,limit_content_to=usable_characters,hide_content=True)
new_name.next_field = new_pass

log_name = InputField(y=.02,x=-.45,limit_content_to=usable_characters)
log_pass = InputField(y=-.04,x=-.45,limit_content_to=usable_characters,hide_content=True)
log_name.next_field = log_pass

log_in_background = Entity(parent=scene,model="quad",position=(-3.6,1.6,0.1),scale=(3,2))
log_in = Text(text="log in",scale = 15,parent = scene, origin=(4.8,-5), background=False,color = Color(0,0,0,0.8))

sign_ip_background = Entity(parent=scene,model="quad",position=(3.6,1.6,0.1),scale=(3,2))
sign_up = Text(text="sign up",scale = 15,parent = scene, origin=(-3.5,-5), background=False,color = Color(0,0,0,0.8))

sign_up_button = usable_button(message="sign up")
#log_in_button = usable_button(x=-2.5,y=-1.2,message = "log in")
#guest_button = usable_button(x=-0,y=-3,message = "Continue as guest",width = 4)

def update():
	sign_up_button.sign_up_function(new_name.text,new_pass.text)
	#log_in_button.log_in_function(log_name.text,log_pass.text)
	#guest_button.guest_mode()
app.run()