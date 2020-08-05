# -*- coding: utf-8 -*-
# Laboratorio 3 Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Render,colorScale
# from gl.math import MathGl
# from obj import Obj


#Prubas mathgl
# math=MathGl()
# vectorA=[3,5,8]
# vectorB=[7,8,9]
# print(np.subtract(vectorA,vectorB))
# print(math.subtractVector(vectorA,vectorB))
# print(np.cross(vectorA,vectorB))
# print(math.crossVector(vectorA,vectorB))
# print(math.normalizeVector(vectorA / np.linalg.norm(vectorA)))
# print(math.normalizeVector(vectorA))
# print(np.dot(vectorA,vectorB))
# print(math.dotProductVector(vectorA,vectorB))

# #We draw our Trex
mainGl3=Render(1400,1400)
mainGl3.loadObjModel('./tests/shadingObj/trex.obj',700,200,4,4)
mainGl3.glFinish('./tests/shadingObj/graphic1.bmp')
mainGl3.glFinishZbuffer('./tests/shadingObj/graphic1zbuffer.bmp')

mainGl3=Render(1400,1400)
mainGl3.loadObjModel('./tests/shadingObj/rock.obj',700,700,3,3)
mainGl3.glFinishZbuffer('./tests/shadingObj/graphic2zbuffer.bmp')
