from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

temp_users = ["jim","john","james"]

app = Ursina()


class Test_cube(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'quad',
			texture = 'white_cube',
			position = (-3.6,1.6,0.1),
			scale = (3,2)
			)

selected_user = ""
users = tuple([DropdownMenuButton(i, on_click=selected_user) for i in temp_users])
added_users = DropdownMenu('Users', buttons=users,parent = scene,position=(-5,0.5),scale = (2.5,0.5))
if added_users.on_mouse_enter():
	selected_user = added_users

Text.size = 0.3
Text.default_resolution = 1080 * 0.05

back1 = Test_cube()
test = Text(text="log in",parent = scene, origin=(5,-5), background=False,color = Color(0,0,0,0.5))
test = Text(text=selected_user,parent = scene, origin=(2,-1), background=True)


app.run()
