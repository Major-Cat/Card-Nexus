from ursina import *
from ursina.prefabs.dropdown_menu import DropdownMenu, DropdownMenuButton

global selected_user
global b
selected_user = ""
temp_users = ["jim","john","james"]

app = Ursina()

def does_a_ting(i):
	selected_user = i
	print(selected_user)



def update():
	#print(selected_user)
	b = tuple([DropdownMenuButton(i, on_click=does_a_ting) for i in temp_users])

	added_users = DropdownMenu('Users', buttons=b,parent = scene,position=(-5,0.5),scale = (2.5,0.5))

class Test_cube(Entity):
	def __init__(self):
		super().__init__(
			parent = scene,
			model = 'quad',
			texture = 'white_cube',
			position = (-3.6,1.6,0.1),
			scale = (3,2)
			)


Text.size = 0.02
Text.default_resolution = 1080 * 0.05

back1 = Test_cube()
test = Text(text="log in",scale = 15,parent = scene, origin=(5,-5), background=False,color = Color(0,0,0,0.8))
#test = Text(text=selected_user,parent = scene, origin=(2,-1), background=True)


app.run()
