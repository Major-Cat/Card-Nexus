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


testboi = tuple([DropdownMenuButton(i) for i in temp_users])
print(testboi,"testboi")
added_users = DropdownMenu('Users', buttons=testboi,parent = scene,position=(-5,0.5),scale = (2.5,0.5))
if added_users.on_mouse_enter():
	print("hello there")

Text.size = 0.3
Text.default_resolution = 1080 * 0.05

back1 = Test_cube()
test = Text(text="log in",parent = scene, origin=(5,-5), background=False,color = Color(0,0,0,0.5))
test = Text(text="log in",parent = scene, origin=(5,-5), background=False,color = Color(0,0,0,0.5))


app.run()
