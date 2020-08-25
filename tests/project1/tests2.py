# -*- coding: utf-8 -*-
# Laboratorio 3 Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Render,colorScale
from gllib.obj import Texture
from gllib.shaders import gouradShader,toonShader,halfhalfShader,predominantColorShader,inverseShading


earthModelPos=(0,0,-1)

mainGl3 = Render(2000,2000)
mainGl3.lookAtMatrix(earthModelPos,(0,0,0))
mainGl3.activeTexture = Texture('./models/textures/moon.bmp')
mainGl3.activeShader = gouradShader
mainGl3.loadObjModel('./models/obj/moon.obj', translate=(-2,-2,-5), scale=(1/4,1/4,1/4), rotation=(0,0,0))



mainGl3.activeTexture = Texture('./models/textures/earth.bmp')
mainGl3.activeTexture2 = Texture('./models/textures/fire.bmp')
mainGl3.activeShader = halfhalfShader

mainGl3.loadObjModel('./models/obj/earth.obj',translate=earthModelPos,scale=(1/1000,1/1000,1/1000))



# mainGl3.activeTexture = Texture('./models/textures/rocket.bmp')
# mainGl3.activeShader = gouradShader
# mainGl3.loadObjModel('./models/obj/rocket.obj',translate=(1200,1200,0),scale=(7,13,4),rotation=(90,150,200))

# mainGl3.activeTexture = Texture('./models/textures/aircraft.bmp')
# mainGl3.activeShader = gouradShader
# mainGl3.loadObjModel('./models/obj/aircraft.obj',translate=(1650,1650,0),scale=(0.25,0.25,0.25),rotation=(-20,0,45+180))



# mainGl3.activeTexture = Texture('./models/textures/hamster.bmp')
# mainGl3.activeShader = toonShader
# mainGl3.loadObjModel('./models/obj/hamster.obj',translate=(1500,600,0),scale=(35,35,35),rotation=(0,90,0))



# mainGl3.activeTexture = None
# mainGl3.activeShader = inverseShading
# mainGl3.loadObjModel('./models/obj/astronaut.obj',translate=(1750,400,0),scale=(0.3,0.3,0.3),rotation=(0,-20,0))


# mainGl3.activeTexture = Texture('./models/textures/cocacan.bmp')
# mainGl3.activeShader = gouradShader
# mainGl3.loadObjModel('./models/obj/can.obj',translate=(250,1500,0),scale=(10,10,10),rotation=(0,180,0))



# mainGl3.activeTexture = Texture('./models/textures/droidm.bmp')
# mainGl3.activeShader = None
# mainGl3.loadObjModel('./models/obj/droidm.obj',translate=(1600,1200,0),scale=(110,110,110),rotation=(-270,90+45,-45))


# mainGl3.activeTexture = None
# mainGl3.activeShader = inverseShading
# mainGl3.loadObjModel('./models/obj/R2.obj',translate=(1300,400,0),scale=(40,40,40),rotation=(0,-45,0))


mainGl3.glFinish('./tests/project1/project.bmp')











