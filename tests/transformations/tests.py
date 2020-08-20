# -*- coding: utf-8 -*-
# Laboratorio 3 Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Render,colorScale
from gllib.obj import Texture
from gllib.shaders import gouradShader,toonShader,halfhalfShader,predominantColorShader,inverseShading
#Using transformations changes lookAtMatrix and createViewMatrix

#Medium shot
mainGl3 = Render(1500,1500)
posModel = ( 0, 0, -3)
mainGl3.lookAtMatrix(posModel,(0,0,0))
mainGl3.activeTexture = Texture('./models/textures/cocacan.bmp')
mainGl3.activeShader = gouradShader
mainGl3.loadObjModel('./models/obj/can.obj',translate=posModel,scale=(0.1,0.1,0.1),rotation=(0,180,0))
mainGl3.glFinish('./tests/transformations/mediumshot.bmp')

#High shot
mainGl3 = Render(1500,1500)
posModel = ( 0, 0, -3)
mainGl3.lookAtMatrix(posModel,(0,2,0))
mainGl3.activeTexture = Texture('./models/textures/cocacan.bmp')
mainGl3.activeShader = gouradShader
mainGl3.loadObjModel('./models/obj/can.obj',translate=posModel,scale=(0.1,0.1,0.1),rotation=(0,180,0))
mainGl3.glFinish('./tests/transformations/highshot.bmp')

#LowShot
mainGl3 = Render(1500,1500)
posModel = ( 0, 0, -3)
mainGl3.lookAtMatrix(posModel,(0,-2,0))
mainGl3.activeTexture = Texture('./models/textures/cocacan.bmp')
mainGl3.activeShader = gouradShader
mainGl3.loadObjModel('./models/obj/can.obj',translate=posModel,scale=(0.1,0.1,0.1),rotation=(0,180,0))
mainGl3.glFinish('./tests/transformations/lowshot.bmp')


# Dutch Shot
mainGl3 = Render(1500,1500)
posModel = ( 0, 0, -3)
mainGl3.createViewMatrix(camPosition=(0,0,0),camRotation=(0,0,15))
mainGl3.activeTexture = Texture('./models/textures/cocacan.bmp')
mainGl3.activeShader = gouradShader
mainGl3.loadObjModel('./models/obj/can.obj',translate=posModel,scale=(0.1,0.1,0.1),rotation=(0,180,0))
mainGl3.glFinish('./tests/transformations/dutchshot.bmp')

