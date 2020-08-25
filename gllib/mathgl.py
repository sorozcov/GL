# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 30/07/2020
#  mathgl.py

from math import pi,cos,sin
#class MathGl for mathematical operations needed for gl
class MathGl(object):
    #Function to calculate a triangle barycentric coordinates of a point 
    def triangleBarycentricCoordinates(self,vertexList, pointP):
        pointA = vertexList[0]
        pointB = vertexList[1]
        pointC = vertexList[2]
        
        try:
            #Calculate u,v and w then return it
            u = ( ((pointB[1] - pointC[1])*(pointP[0] - pointC[0]) + (pointC[0] - pointB[0])*(pointP[1] - pointC[1]) ) /
                ((pointB[1] - pointC[1])*(pointA[0] - pointC[0]) + (pointC[0] - pointB[0])*(pointA[1] - pointC[1])) )

            v = ( ((pointC[1] - pointA[1])*(pointP[0] - pointC[0]) + (pointA[0] - pointC[0])*(pointP[1] - pointC[1]) ) /
                ((pointB[1] - pointC[1])*(pointA[0] - pointC[0]) + (pointC[0] - pointB[0])*(pointA[1] - pointC[1])) )

            w = 1 - u - v
        except:
            return -1, -1, -1

        return u, v, w
    
    #Function to substract two vectors
    def subtractVector(self,vectorA,vectorB):
        if(len(vectorA)!=len(vectorB)):
            return
        vectorResult=[None] * len(vectorA)
        for i in range(len(vectorA)):
            vectorResult[i]=vectorA[i]-vectorB[i]
        return vectorResult
    
    #Function to do product cross two vectors
    def crossVector(self,vectorA,vectorB):
        if(len(vectorA)!=len(vectorB)):
            return
        ux,uy,uz=vectorA
        vx,vy,vz=vectorB
        wx=uy*vz-uz*vy
        wy=uz*vx-ux*vz
        wz=ux*vy-uy*vx
        return [wx,wy,wz]
    
    #Function to do product cross two vectors
    def normalizeVector(self,vectorA):
        vectorValue=self.valueVector(vectorA)
        normalized=[0]*len(vectorA)
        if(vectorValue>0):
            normalized = [coord/vectorValue for coord in vectorA]

        return normalized
    
    #Function get the value of a vector
    def valueVector(self,vectorA):
        vectorValue=0
        for i in range(len(vectorA)):
            vectorValue=vectorValue+vectorA[i]**2
        vectorValue=vectorValue**(1/2)
        return vectorValue

    #Function to do product cross two vectors
    def dotProductVector(self,vectorA,vectorB):
        if(len(vectorA)!=len(vectorB)):
            return 0
        vectorDotResult=0
        for i in range(len(vectorA)):
            vectorDotResult=vectorDotResult+vectorA[i]*vectorB[i]
        return vectorDotResult
    #Multiply the array of matrixes
    def multiplyMatrixes(self,matrixes=[]):
        resultMatrix=matrixes[0]
        for i in range(len(matrixes)-1):
            resultMatrix=self.multiplyMatrix(resultMatrix,matrixes[i+1])
        return resultMatrix

    #Function to multiply matrix and vectors with matrix
    def multiplyMatrix(self,matrixA,matrixB,returnVector=True,returnDotProduct=True):

        #We check if we are multiplying vectors
        if(str(type(matrixA[0]))!="<class 'list'>"):
            matrixA=[matrixA]
        if(str(type(matrixB[0]))!="<class 'list'>"):
            for j in range(len(matrixB)):
                matrixB[j]=[matrixB[j]]
        
        #We check that matrix multiplication is possible, else we return false
        if(len(matrixA[0])!=len(matrixB)):
            #Unable to do matrix multiplication
            return False

        #We check if both are vectors and if we wants dotProduct Return
        if(len(matrixA)==1 and len(matrixB[0])==1 and returnDotProduct):
            vectorB=[]
            for k in range(len(matrixB)):
                vectorB.append(matrixB[k][0])
            return(self.dotProductVector(matrixA[0],vectorB))

        #We start to multiply the matrix and return result
        matrixResult=[[0 for x in range(len(matrixB[0]))] for y in range(len(matrixA))]
        for i in range(len(matrixA)):
            for j in range(len(matrixB[0])):
                vectorB=[]
                for k in range(len(matrixB)):
                    vectorB.append(matrixB[k][j])
                matrixResult[i][j]=self.dotProductVector(matrixA[i],vectorB)
        #If result is a vector, based on returnVector or return as matrix
        if(len(matrixResult)==1 and returnVector):
            return matrixResult[0]
        elif(len(matrixResult[0])==1 and returnVector):
            vectorResult=[]
            for k in range(len(matrixResult)):
                    vectorResult.append(matrixResult[k][0])
            return vectorResult
        return matrixResult
    
    #From degreesToRadians
    def degreesToRadians(self,deg):
        return deg*2*pi/360
    #cos
    def cos(self,rad):
        return cos(rad)
    #sin
    def sin(self,rad):
        return sin(rad)

    #Function to calculate inverse matrix
    def invMatrix(self,matrixA):
        try:
            if(len(matrixA)!=len(matrixA[0])):
                return False
            detMatrixA=self.detMatrix(matrixA)
            if(detMatrixA!=0):
                return self.scalarMultiplicationMatrix(self.attachedMatrix(matrixA,transpose=True),1/detMatrixA)
            else:
                return False
            
        except:
            #Any error on matrix given
            return False

    #Function to calculate transpose matrix
    def transposeMatrix(self,matrixA):
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
    def attachedMatrix(self,matrixA,transpose=False):
        try:
            adjMatrix=[[0 for i in range(len(matrixA[0]))] for j in range(len(matrixA))]
            for i in range(len(matrixA)):
                for j in range(len(matrixA[0])):
                    adjMatrix[i][j]=self.detMatrixIJ(matrixA,i,j)*((-1)**(i+j+2))
            adjMatrix=adjMatrix if not transpose else self.transposeMatrix(adjMatrix)
            return adjMatrix
        except:
            #Any error
            return False

    #Calculate determinant of position ij of matrix for attached matrix
    def detMatrixIJ(self,matrixA,i,j):
        if(len(matrixA)!=len(matrixA[0])):
            return False
        if(len(matrixA)==2):
            return matrixA[i][j]
        else:
            return self.detMatrix(self.generateMatrixWithoutIJ(matrixA,i,j))

    #Function to calculate matrix determinant
    def detMatrix(self,matrixA):
        if(len(matrixA)!=len(matrixA[0])):
            return False
        if(len(matrixA)==2):
            return matrixA[0][0]*matrixA[1][1]-matrixA[0][1]*matrixA[1][0]
        else:
            mults=matrixA[0]
            det=0
            for j in range(len(mults)):
                det=det+self.detMatrix(self.generateMatrixWithoutJ(matrixA,j))*mults[j]*((-1)**j)
            return det

    #Generate matrix withou column j
    def generateMatrixWithoutJ(self,matrixA,jk):
        newMatrix=[[matrixA[i+1][j] if j<jk else matrixA[i+1][j+1%len(matrixA[0])]  for j in range(len(matrixA[0])-1)] for i in range(len(matrixA)-1)]
        return newMatrix

    #Generate matrix without column j and row i
    def generateMatrixWithoutIJ(self,matrixA,ii,jj):
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
    def scalarMultiplicationMatrix(self,matrixA,scalar=1):
        for i in range(len(matrixA)):
                for j in range(len(matrixA[0])):
                    matrixA[i][j]=matrixA[i][j]*scalar
        return matrixA