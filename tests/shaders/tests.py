# -*- coding: utf-8 -*-
# Laboratorio 3 Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Render,colorScale
from gllib.obj import Texture
from gllib.shaders import gouradShader,toonShader,halfhalfShader,predominantColorShader,inverseShading

# # Half Half Shader
# mainGl3=Render(1400,1400)
# mainGl3.activeTexture = Texture('./models/textures/earthDay.bmp')
# mainGl3.activeTexture2 = Texture('./models/textures/earthNight.bmp')
# mainGl3.activeShader = halfhalfShader
# mainGl3.light=mainGl3.mathGl.normalizeVector([1,0,1])
# mainGl3.loadObjModel('./models/obj/earth.obj',700,700,1,1)
# mainGl3.glFinish('./tests/shaders/graphicearth.bmp')


# #Toon Shader
# mainGl3=Render(1400,1400)
# mainGl3.activeShader = toonShader
# mainGl3.light=mainGl3.mathGl.normalizeVector([1,0,1])
# mainGl3.loadObjModel('./models/obj/can.obj',700,700,50,50)
# mainGl3.glFinish('./tests/shaders/graphictoonshader.bmp')

# #Toon Shader
# mainGl3=Render(1400,1400)
# mainGl3.activeShader = toonShader
# mainGl3.light=mainGl3.mathGl.normalizeVector([1,0,1])
# mainGl3.activeTexture = Texture('./models/textures/apple.bmp')
# mainGl3.loadObjModel('./models/obj/apple.obj',700,700,7,7)
# mainGl3.glFinish('./tests/shaders/appletoonshader.bmp')

# #Gourad Shader
# mainGl3=Render(1400,1400)
# mainGl3.activeShader = gouradShader
# mainGl3.activeTexture = Texture('./models/textures/apple.bmp')
# mainGl3.loadObjModel('./models/obj/apple.obj',700,700,7,7)
# mainGl3.glFinish('./tests/shaders/applegouradshader.bmp')

# #Toon Shader
# mainGl3=Render(1400,1400)
# mainGl3.activeShader = toonShader
# mainGl3.activeTexture = Texture('./models/textures/patrik.bmp')
# mainGl3.currentColor = colorScale(255/255,158/255,158/255)
# mainGl3.loadObjModel('./models/obj/patrik.obj',700,400,3,3)
# mainGl3.glFinish('./tests/shaders/patriktext.bmp')



# #predominantColorShader
# mainGl3=Render(1400,1400)
# mainGl3.activeShader = predominantColorShader
# mainGl3.activeTexture = Texture('./models/textures/apple.bmp')
# mainGl3.loadObjModel('./models/obj/apple.obj',700,700,7,7)
# mainGl3.glFinish('./tests/shaders/myshaderapple.bmp')

#inverseShading
# mainGl3=Render(1400,1400)
# mainGl3.activeShader = inverseShading
# mainGl3.activeTexture = Texture('./models/textures/apple.bmp')
# mainGl3.loadObjModel('./models/obj/apple.obj',700,700,7,7)
# mainGl3.glFinish('./tests/shaders/myshaderappleinverse.bmp')

# mainGl3=Render(1000,1000)
# mainGl3.activeShader = gouradShader
# mainGl3.activeTexture = Texture('./models/textures/model.bmp')
# mainGl3.loadObjModel('./models/obj/model.obj',500,400,300,300,400,300)
# mainGl3.glFinish('./tests/shaders/graphicmodel.bmp')


