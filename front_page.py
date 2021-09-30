from ursina import *
import json
from hashlib import sha256

app = Ursina()

new = []

class usable_button(Button):
	def __init__(self,texture = "white_cube",x=6.5,y=0):
		super().__init__(
			parent = scene,
			text = "sign up",
			color = color.gray,
			texture = texture,
			highlight_color = color.light_gray,
			pressed_color = color.dark_gray,
			position = (x,y),
			scale = (1.5,1)
			)

	def button_input(self,username,password):
		if self.hovered == True:
			#if held_keys == "left mouse down":

				with open("Storage/temp_storage.json","r") as f:
					datafile = json.load(f)
				b = bytes(password, 'utf-8')
				password = sha256(b).hexdigest()
				datafile[username] = str(password)
				with open("Storage/temp_storage.json","w") as f:
					json.dump(datafile, f, indent=4)

"""
				with open("Storage/temp_storage.json", "r+") as f:
					data = json.load(f)
					data.update({username,password})
					f.seek(0)
					json.dump(data, f)
"""




Text.size = 0.02
Text.default_resolution = 1080 * 0.05

new_name = InputField(y=.02,x=.45,limit_content_to="1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@;:?.,!*% ")
new_pass = InputField(y=-.04,x=.45,limit_content_to="1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@;:?.,!*% ",hide_content=True)
new_name.next_field = new_pass

back1 = Entity(parent=scene,model="quad",position=(-3.6,1.6,0.1),scale=(3,2))
log_in = Text(text="log in",scale = 15,parent = scene, origin=(4.8,-5), background=False,color = Color(0,0,0,0.8))

back2 = Entity(parent=scene,model="quad",position=(3.6,1.6,0.1),scale=(3,2))
sign_up = Text(text="sign up",scale = 15,parent = scene, origin=(-3.5,-5), background=False,color = Color(0,0,0,0.8))

sign_up_button = usable_button()
#sign_up_button.input = new.append

not_words = ["down","up","enter","caps","shift","click"]

def update():
	print(new_name.text)
	sign_up_button.button_input(new_name.text,new_pass.text)
app.run()
