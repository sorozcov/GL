# -*- coding: utf-8 -*-
# Laboratorio 3 Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Render,colorScale
from gllib.obj import Texture


# #We draw our model
mainGl3=Render(1400,1400)
text = Texture('./tests/textureObj/earth.bmp')
mainGl3.loadObjModel('./tests/textureObj/earth.obj',700,700,1,1,texture=text)
mainGl3.glFinish('./tests/textureObj/graphicearth.bmp')

mainGl3=Render(1400,1400)
text = Texture('./tests/textureObj/trex.bmp')
mainGl3.loadObjModel('./tests/textureObj/trex.obj',700,200,4,4,texture=text)
mainGl3.glFinish('./tests/textureObj/graphic1.bmp')


mainGl3=Render(1400,1400)
text = Texture('./tests/textureObj/model.bmp')
mainGl3.loadObjModel('./tests/textureObj/model.obj',700,700,350,350,texture=text)
mainGl3.glFinish('./tests/textureObj/graphicmodel.bmp')




