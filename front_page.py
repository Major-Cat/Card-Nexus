from ursina import *
#from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

temp_users = ["jim","john","james"]
app = Ursina()

class t_button(Button):
	def __init__(self,texture = "white_cube",x=5,y=0,New_name=None,New_pass=None):
		super().__init__(
			parent = scene,
			color = color.white,
			texture = texture,
			highlight_color = color.light_gray,
			pressed_color = color.gray,
			position = (x,y)
			)

	def input(self,key):
		if self.hovered:
			if key == 'left mouse down':
				return self.New_name.text,self.New_pass.text


Text.size = 0.02
Text.default_resolution = 1080 * 0.05

new_name = InputField(y=-.12,x=.5,limit_content_to="1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@;:?.,!*% ")
new_pass = InputField(y=-.18,x=.5,limit_content_to="1234567890-_qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM@;:?.,!*% ",hide_content=True)
new_name.next_field = new_pass

back1 = Entity(parent=scene,model="quad",position=(-3.6,1.6,0.1),scale=(3,2))
log_in = Text(text="log in",scale = 15,parent = scene, origin=(4.8,-5), background=False,color = Color(0,0,0,0.8))

back2 = Entity(parent=scene,model="quad",position=(3.6,1.6,0.1),scale=(3,2))
sign_up = Text(text="sign up",scale = 15,parent = scene, origin=(-3.5,-5), background=False,color = Color(0,0,0,0.8))
sign_up_button = t_button(New_name = new_name, New_pass = new_pass)


#def update():
	#global New_name
	#New_name = new_name.text
	#print(New_name,"New_name")
	#print(selected_user)
	#added_users = DropdownMenu('Users', buttons=tuple([DropdownMenuButton(user) for user in temp_users]),parent = scene,position=(-5,0.5),scale = (2.5,0.5))
	#added_users.input(held_keys)



#username_field = InputField(y=-.12, limit_content_to='0123456789')
#password_field = InputField(y=-.18, hide_content=True)
#username_field.next_field = password_field


app.run()
