# -*- coding: utf-8 -*-
# Laboratorio 3 Tests.py

#Import our gl library
import math
import os,sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from gllib.gl import Render,colorScale
from gllib.obj import Texture
from gllib.shaders import gouradShader,toonShader,halfhalfShader,predominantColorShader,inverseShading



# mainGl3 = Render(1500,1500)
# mainGl3.activeTexture = Texture('./models/textures/model.bmp')
# mainGl3.activeShader = gouradShader
# mainGl3.loadObjModel('./models/obj/model.obj', translate=(250,250,250), scale=(200,200,200), rotation=(0,90,0))

# mainGl3.glFinish('./tests/transformations/output.bmp')


#Function to calculate inverse matrix
def invMatrix(matrixA):
    try:
        if(len(matrixA)!=len(matrixA[0])):
            return False
        detMatrixA=detMatrix(matrixA)
        if(detMatrixA!=0):
            return scalarMultiplicationMatrix(attachedMatrix(matrixA,transpose=True),1/detMatrixA)
        else:
            return False
        
    except:
        #Any error on matrix given
        return False

#Function to calculate transpose matrix
def transposeMatrix(matrixA):
    try:
        transMatrix=[[0 for j in range(len(matrixA))] for i in range(len(matrixA[0]))]
        for i in range(len(matrixA)):
            for j in range(len(matrixA[0])):
                transMatrix[j][i]=matrixA[i][j]
        return transMatrix
    except:
        #Any error
        return False


#Function to calculate attached matrix
def attachedMatrix(matrixA,transpose=False):
    try:
        adjMatrix=[[0 for i in range(len(matrixA[0]))] for j in range(len(matrixA))]
        for i in range(len(matrixA)):
            for j in range(len(matrixA[0])):
                adjMatrix[i][j]=detMatrixIJ(matrixA,i,j)*((-1)**(i+j+2))
        adjMatrix=adjMatrix if not transpose else transposeMatrix(adjMatrix)
        return adjMatrix
    except:
        #Any error
        return False

#Calculate determinant of position ij of matrix for attached matrix
def detMatrixIJ(matrixA,i,j):
    if(len(matrixA)!=len(matrixA[0])):
        return False
    if(len(matrixA)==2):
        return matrixA[i][j]
    else:
        return detMatrix(generateMatrixWithoutIJ(matrixA,i,j))

#Function to calculate matrix determinant
def detMatrix(matrixA):
    if(len(matrixA)!=len(matrixA[0])):
        return False
    if(len(matrixA)==2):
        return matrixA[0][0]*matrixA[1][1]-matrixA[0][1]*matrixA[1][0]
    else:
        mults=matrixA[0]
        det=0
        for j in range(len(mults)):
            det=det+detMatrix(generateMatrixWithoutJ(matrixA,j))*mults[j]*((-1)**j)
        return det

#Generate matrix withou column j
def generateMatrixWithoutJ(matrixA,jk):
    newMatrix=[[matrixA[i+1][j] if j<jk else matrixA[i+1][j+1%len(matrixA[0])]  for j in range(len(matrixA[0])-1)] for i in range(len(matrixA)-1)]
    return newMatrix

def generateMatrixWithoutIJ(matrixA,ii,jj):
    newMatrix=[[0 for j in range(len(matrixA[0])-1)] for i in range(len(matrixA)-1)]
    jFinal=0
    iFinal=0
    for i in range(len(matrixA)-1):
        for j in range(len(matrixA[0])-1):
            jFinal =j if(j<jj) else (j+1)%len(matrixA[0])
            iFinal =i if(i<ii) else (i+1)%len(matrixA)
            newMatrix[i][j]=matrixA[iFinal][jFinal]
    return newMatrix
                

#Function to multiply matrix by scalar
def scalarMultiplicationMatrix(matrixA,scalar=1):
    for i in range(len(matrixA)):
            for j in range(len(matrixA[0])):
                matrixA[i][j]=matrixA[i][j]*scalar
    return matrixA


mat=[
    [2,1,0],
    [1,1,0],
    [0,0,1]]
mat2=[
    [1,0,3,-3],
    [2,-3,-2,3],
    [-1,2,1,2],
    [3,2,5,0]]
mat3=[[1,2],
    [2,-3]]

mat4=[
    [4,0,0],
    [0,0,-2],
    [1,-2,4]]

mat5=[
    [1,1,0,0],
    [0,-1,-2,0],
    [0,0,1,-1],
    [0,0,0,1]
    ]
print(invMatrix(mat5))
