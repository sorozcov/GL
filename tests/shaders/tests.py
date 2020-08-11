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


def dotProductVector(vectorA,vectorB):
    if(len(vectorA)!=len(vectorB)):
        return 0
    vectorDotResult=0
    for i in range(len(vectorA)):
        vectorDotResult=vectorDotResult+vectorA[i]*vectorB[i]
    return vectorDotResult

def multiplyMatrix(matrixA,matrixB,returnVector=True,returnDotProduct=True):

    if(str(type(matrixA[0]))!="<class 'list'>"):
        matrixA=[matrixA]
    if(str(type(matrixB[0]))!="<class 'list'>"):
        matrixB=[matrixB]
        
    if(len(matrixA[0])!=len(matrixB)):
        #Unable to do matrix multiplication
        return False
    if(len(matrixA)==1 and len(matrixB[0])==1 and returnDotProduct):
        vectorB=[]
        for k in range(len(matrixB)):
            vectorB.append(matrixB[k][0])
        return(dotProductVector(matrixA[0],vectorB))

    matrixResult=[[0 for x in range(len(matrixB[0]))] for y in range(len(matrixA))]
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            vectorB=[]
            for k in range(len(matrixB)):
                vectorB.append(matrixB[k][j])
            matrixResult[i][j]=dotProductVector(matrixA[i],vectorB)
    if(len(matrixResult)==1 and returnVector):
        return matrixResult[0]
    return matrixResult

A=[[1,2,3],[4,5,6]]
B=[[7,8],[9,10],[11,12]]
L=[[1],[2],[3]]
J=[[2,4],[3,5],[5,6]]
K=[1,2,3]
M=[[2,8,8],[3,6,7],[5,6,7]]
# print(multiplyMatrix(A,B))

print(multiplyMatrix(A,B))