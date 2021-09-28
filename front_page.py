from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

temp_users = ["jim","john","james"]

app = Ursina()

def update():
	print(New_name,"New_name")
	#print(selected_user)
	#added_users = DropdownMenu('Users', buttons=tuple([DropdownMenuButton(user) for user in temp_users]),parent = scene,position=(-5,0.5),scale = (2.5,0.5))
	#added_users.input(held_keys)

Text.size = 0.02
Text.default_resolution = 1080 * 0.05

back1 = Entity(parent=scene,model="quad",position=(-3.6,1.6,0.1),scale=(3,2))
log_in = Text(text="log in",scale = 15,parent = scene, origin=(4.8,-5), background=False,color = Color(0,0,0,0.8))

back2 = Entity(parent=scene,model="quad",position=(3.6,1.6,0.1),scale=(3,2))
sign_up = Text(text="sign up",scale = 15,parent = scene, origin=(-3.5,-5), background=False,color = Color(0,0,0,0.8))
New_name = InputField(text_field = TextField(world_parent=scene, x=-.45, y=.3, z=-.1, max_lines=2)).input(held_keys)


app.run()
