# -*- coding: utf-8 -*-
# Proyecto Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Render,colorScale
from gllib.obj import Texture
from gllib.shaders import gouradShader,toonShader,halfhalfShader,predominantColorShader,inverseShading,tvShader,normalMapTexture,randomColorShader

#We define earth position for the camara to look at
earthModelPos=(0,0,-1.05)
#Create our render for every model
mainGl3 = Render(2000,2000)
#Assign a background image to our scene
mainGl3.glClearBackground("./models/textures/spacebackground.bmp")
#Camara looking at earth position
mainGl3.lookAtMatrix(earthModelPos,(0,0,0))


#Moon Model
mainGl3.activeTexture = Texture('./models/textures/moon.bmp')
mainGl3.activeShader = gouradShader
mainGl3.loadObjModel('./models/obj/moon.obj', translate=(-1.8,-1.8,-5), scale=(1/4,1/4,1/4), rotation=(0,0,0))

#R2 Model using Normal Maps to shade 1
mainGl3.activeTexture = Texture('./models/textures/R2.bmp')
mainGl3.activeNormalMap = Texture('./models/textures/R2Normal.bmp')
mainGl3.activeShader = normalMapTexture
mainGl3.loadObjModel('./models/obj/R2.obj',translate=(0.16,-0.06,-0.5),scale=(2/90,2/90,2/90),rotation=(0,-25,0))

#Earth Model with 2 textures, using halfHalfShader
mainGl3.activeTexture = Texture('./models/textures/earth.bmp')
mainGl3.activeTexture2 = Texture('./models/textures/fire.bmp')
mainGl3.activeShader = halfhalfShader
mainGl3.loadObjModel('./models/obj/earth.obj',translate=earthModelPos,scale=(1/1800,1/1800,1/1800))


#Rocket Model 
mainGl3.activeTexture = Texture('./models/textures/rocket.bmp')
mainGl3.activeShader = predominantColorShader
mainGl3.loadObjModel('./models/obj/rocket.obj',translate=(0.6,0.45,-3),scale=(1/80,1/450,1/180),rotation=(90,150,200))

#Aircraft Model 2
mainGl3.activeTexture = Texture('./models/textures/aircraft.bmp')
mainGl3.activeShader = gouradShader
mainGl3.loadObjModel('./models/obj/aircraft.obj',translate=(1.3,1.2,-3),scale=(1/3400,1/3400,1/3400),rotation=(-20,0,45+180))


#Hamster Model using toonShader 3
mainGl3.activeTexture = Texture('./models/textures/hamster.bmp')
mainGl3.activeShader = toonShader
mainGl3.loadObjModel('./models/obj/hamster.obj',translate=(-0.38,-0.29,-1),scale=(7/450,7/450,7/450),rotation=(0,-45,0))

#Astronaut Model using inverse shading to iluminate from outside to inside 4
mainGl3.activeTexture = None
mainGl3.activeShader = inverseShading
mainGl3.loadObjModel('./models/obj/astronaut.obj',translate=(0,0.19,-1),scale=(3/25000,3/25000,3/25000),rotation=(0,-10,0))


#Coca Cola Can Model 5 with random color shader
mainGl3.activeTexture = Texture('./models/textures/cocacan.bmp')
mainGl3.activeShader = randomColorShader
mainGl3.loadObjModel('./models/obj/can.obj',translate=(-0.068,0.3,-0.99),scale=(1/320,1/320,1/320),rotation=(0,190,0))

#Mars Model using moon object changing texture and randomColorShader
mainGl3.activeTexture = Texture('./models/textures/mars.bmp')
mainGl3.activeShader = randomColorShader
mainGl3.loadObjModel('./models/obj/moon.obj', translate=(-2.5,+2.1,-6.7), scale=(1/4,1/4,1/4), rotation=(0,100,0))

#Draw our Final Scene in projectscene.bmp
mainGl3.glFinish('./tests/project1/projectscene.bmp')


#Finally we create another Render to use a different background and generate a cool effect
mainGl3 = Render(2000,2000)
mainGl3.glClearBackground("./models/textures/spacebackground2.bmp")

#TV Model showing our projectscene with tvShader and normal mapping 5
mainGl3.activeTexture = Texture('./models/textures/tv2.bmp')
mainGl3.activeTexture2 = Texture('./tests/project1/projectscene.bmp')
mainGl3.activeNormalMap = Texture('./models/textures/TVNormal.bmp')
mainGl3.activeShader = tvShader
mainGl3.loadObjModel('./models/obj/tv2.obj',translate=(0,0,-1),scale=(1/200,1/200,1/200),rotation=(0,-20,0))

#Draw our cool final scene projectTVnormal
mainGl3.glFinish('./tests/project1/projectTVnormal.bmp')











