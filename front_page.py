from ursina import *

app = Ursina()

class t_button(Button):
	def __init__(self,texture = "white_cube",x=6.5,y=0,New_name=None,New_pass=None):
		self.New_name,self.New_pass = New_name, New_pass
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

	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				#print(self.New_name.text,",",self.New_pass.text)
				return self.New_name.text,",",self.New_pass.text


Text.size = 0.02
Text.default_resolution = 1080 * 0.05

new_name = InputField(y=.02,x=.45,limit_content_to="1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@;:?.,!*% ")
new_pass = InputField(y=-.04,x=.45,limit_content_to="1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@;:?.,!*% ",hide_content=True)
new_name.next_field = new_pass

back1 = Entity(parent=scene,model="quad",position=(-3.6,1.6,0.1),scale=(3,2))
log_in = Text(text="log in",scale = 15,parent = scene, origin=(4.8,-5), background=False,color = Color(0,0,0,0.8))

back2 = Entity(parent=scene,model="quad",position=(3.6,1.6,0.1),scale=(3,2))
sign_up = Text(text="sign up",scale = 15,parent = scene, origin=(-3.5,-5), background=False,color = Color(0,0,0,0.8))
sign_up_button = t_button(New_name = new_name, New_pass = new_pass)

def update():
	if held_keys == "left mouse down":
		print("hello world")
		new_dude = sign_up_button.input(held_keys)
		print(new_dude,"new dude")





app.run()
