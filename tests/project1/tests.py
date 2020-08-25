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
# mainGl3.lookAtMatrix(earthModelPos,(0,0,0))
# mainGl3.activeTexture = Texture('./models/textures/moon.bmp')
# mainGl3.activeShader = gouradShader
# mainGl3.loadObjModel('./models/obj/moon.obj', translate=(-1.8,-1.8,-5), scale=(1/4,1/4,1/4), rotation=(0,0,0))



# mainGl3.activeTexture = Texture('./models/textures/earth.bmp')
# mainGl3.activeTexture2 = Texture('./models/textures/fire.bmp')
# mainGl3.activeShader = halfhalfShader

# mainGl3.loadObjModel('./models/obj/earth.obj',translate=earthModelPos,scale=(1/1800,1/1800,1/1800))



# mainGl3.activeTexture = Texture('./models/textures/rocket.bmp')
# mainGl3.activeShader = gouradShader
# mainGl3.loadObjModel('./models/obj/rocket.obj',translate=(0.6,0.45,-3),scale=(1/80,1/450,1/180),rotation=(90,150,200))

# mainGl3.activeTexture = Texture('./models/textures/aircraft.bmp')
# mainGl3.activeShader = gouradShader
# mainGl3.loadObjModel('./models/obj/aircraft.obj',translate=(1.3,1.2,-3),scale=(1/3400,1/3400,1/3400),rotation=(-20,0,45+180))



# mainGl3.activeTexture = Texture('./models/textures/hamster.bmp')
# mainGl3.activeShader = toonShader
# mainGl3.loadObjModel('./models/obj/hamster.obj',translate=(0.3,-0.4,-1),scale=(7/510,7/510,7/510),rotation=(0,90,0))



# mainGl3.activeTexture = None
# mainGl3.activeShader = inverseShading
# mainGl3.loadObjModel('./models/obj/astronaut.obj',translate=(0.4,-0.41,-1),scale=(3/25000,3/25000,3/25000),rotation=(0,-20,0))


# mainGl3.activeTexture = Texture('./models/textures/cocacan.bmp')
# mainGl3.activeShader = gouradShader
# mainGl3.loadObjModel('./models/obj/can.obj',translate=(0.3,-0.3,-1),scale=(1/270,1/270,1/270),rotation=(0,180,0))



# mainGl3.activeTexture = Texture('./models/textures/droidm.bmp')
# mainGl3.activeShader = None
# mainGl3.loadObjModel('./models/obj/droidm.obj',translate=(1600,1200,0),scale=(110,110,110),rotation=(-270,90+45,-45))


# mainGl3.activeTexture = Texture('./models/textures/R2.bmp')
# mainGl3.activeShader = gouradShader
# mainGl3.loadObjModel('./models/obj/R2.obj',translate=(0.43,-0.3,-1),scale=(2/125,2/125,2/125),rotation=(0,-45,0))

# mainGl3.activeTexture = Texture('./models/textures/R2.bmp')
mainGl3.activeShader = gouradShader
mainGl3.loadObjModel('./models/obj/pc.obj',translate=(0,0,-1),scale=(1/150,1/150,1/150),rotation=(0,0,0))

mainGl3.glFinish('./tests/project1/projectscene.bmp')











