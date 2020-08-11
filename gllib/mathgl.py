# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 30/07/2020
#  mathgl.py

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

    #Function to multiply matrix and vectors with matrix
    def multiplyMatrix(self,matrixA,matrixB,returnVector=True,returnDotProduct=True):

        #We check if we are multiplying vectors
        if(str(type(matrixA[0]))!="<class 'list'>"):
            matrixA=[matrixA]
        if(str(type(matrixB[0]))!="<class 'list'>"):
            matrixB=[matrixB]
        
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
        return matrixResult