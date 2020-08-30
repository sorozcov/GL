# -*- coding: utf-8 -*-
# Silvio Orozco 18282
# Universidad del Valle de Guatemala
# Gráficas por computadora
# Guatemala 09/08/2020
# shaders.py


#Gourad Shader
#https://en.wikipedia.org/wiki/Gouraud_shading
def gouradShader(render,**kwargs):
    #We obtain our barycentric coordinates
    u,v,w=kwargs['barCoordinates']
    ta,tb,tc=kwargs['vertexTextureList']
    na,nb,nc=kwargs['vertexNormalList']
    b,g,r=kwargs['color']
    
    if render.activeTexture:
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w                            
        b,g,r= render.activeTexture.getTextureCoordinates(tx, ty)
    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    try:
        nz = na[2] * u + nb[2] * v + nc[2] * w
    except:
        nz=0
    #We create out normal for each point
    normal=[nx,ny,nz]
  
    intensity = float(render.mathGl.dotProductVector(normal, render.light))
    #We calculate the color for each pixel with its normal vector and light  
    b = b*intensity/255
    g = g*intensity/255
    r = r*intensity/255
    if intensity>0:
        #Return bgr
        return b,g,r
    else:
        #Return black
        return 0,0,0

def tvShader(render,**kwargs):
    #We obtain our barycentric coordinates
    vertexA,vertexB,vertexC=kwargs['vertexList']
    u,v,w=kwargs['barCoordinates']
    ta,tb,tc=kwargs['vertexTextureList']
    na,nb,nc=kwargs['vertexNormalList']
    b,g,r=kwargs['color']
    tx = ta[0] * u + tb[0] * v + tc[0] * w
    ty = ta[1] * u + tb[1] * v + tc[1] * w
    if render.activeTexture:
        
        if(tx>=990/2048 and tx<= 1560/2048 and ty>=40/2048 and ty<=516/2048):
            txTV=(tx-990/2048)/((1560-990)/2048)
            tyTV=(ty-40/2048)/((516-40)/2048)
            b,g,r = render.activeTexture2.getTextureCoordinates(txTV,tyTV)
        else:                        
            b,g,r= render.activeTexture.getTextureCoordinates(tx, ty)
    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    try:
        nz = na[2] * u + nb[2] * v + nc[2] * w
    except:
        nz=0
    #We create out normal for each point
    normal=[nx,ny,nz]
    if render.activeNormalMap:
        bNM,gNM,rNM= render.activeNormalMap.getTextureCoordinates(tx, ty)
        #We convert rgb color to arange in -1 and 1
        normalMap = [(rNM/255)*2-1,(gNM/255)*2-1,(bNM/255)*2-1]
        normalMap = render.mathGl.normalizeVector(normalMap)
        #We need to get the tangent and bitangent to transform the normal map texture to Tangent Space
        #https://learnopengl.com/Advanced-Lighting/Normal-Mapping
        edge1= render.mathGl.subtractVector(vertexB,vertexA)
        edge2= render.mathGl.subtractVector(vertexC,vertexA)
        deltaUV1 = render.mathGl.subtractVector(tb, ta)
        deltaUV2 = render.mathGl.subtractVector(tc, ta)
        tangent = [0,0,0]
        f = 1 / (deltaUV1[0] * deltaUV2[1] - deltaUV2[0] * deltaUV1[1])
        tangent[0] = f * (deltaUV2[1] * edge1[0] - deltaUV1[1] * edge2[0])
        tangent[1] = f * (deltaUV2[1] * edge1[1] - deltaUV1[1] * edge2[1])
        tangent[2] = f * (deltaUV2[1] * edge1[2] - deltaUV1[1] * edge2[2])
        tangent = render.mathGl.normalizeVector(tangent)

        tangent = render.mathGl.subtractVector(tangent, render.mathGl.scalarMultiplicationVector(normal,render.mathGl.dotProductVector(tangent, normal)))
        #tangent = np.subtract(tangent, np.multiply(np.dot(tangent, normal),normal))
        tangent = render.mathGl.normalizeVector(tangent)

        bitangent = render.mathGl.crossVector(normal, tangent)
        bitangent = render.mathGl.normalizeVector(bitangent)

        #Now we calculate tangent matrix
        tangentMatrix = [[tangent[0],bitangent[0],normal[0]],
                                [tangent[1],bitangent[1],normal[1]],
                                [tangent[2],bitangent[2],normal[2]]]

        light = render.light
        light = render.mathGl.multiplyMatrix(tangentMatrix,light)
        light = render.mathGl.normalizeVector(light)
    
        #We calculate intensity with normalMap and newLight
        intensity = render.mathGl.dotProductVector(normalMap, light)
    else:
        intensity = float(render.mathGl.dotProductVector(normal, render.light))
    #We calculate the color for each pixel with its normal vector and light  
    b = b*intensity/255
    g = g*intensity/255
    r = r*intensity/255
    if intensity>0:
        #Return bgr
        return b,g,r
    else:
        #Return black
        return 0,0,0

#Toon Shader
#https://en.wikipedia.org/wiki/Gouraud_shading
def toonShader(render,**kwargs):
    #We obtain our barycentric coordinates
    u,v,w=kwargs['barCoordinates']
    ta,tb,tc=kwargs['vertexTextureList']
    na,nb,nc=kwargs['vertexNormalList']
    b,g,r=kwargs['color']
    
    if render.activeTexture!=None:
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w                            
        b,g,r= render.activeTexture.getTextureCoordinates(tx, ty)
    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    try:
        nz = na[2] * u + nb[2] * v + nc[2] * w
    except:
        nz=0
    #We create out normal for each point
    normal=[nx,ny,nz]
  
    intensity = render.mathGl.dotProductVector(normal, render.light)
    #We calculate the color for each pixel with its normal vector and light  
    if(0.3>=intensity and intensity>0):
        intensity=0.1
    elif(0.5>=intensity and intensity>0.3):
        intensity=0.5
    elif(0.8>=intensity and intensity>0.5):
        intensity=0.8
    elif(intensity>0.8):
        intensity=1
    b = b*intensity/255
    g = g*intensity/255
    r = r*intensity/255
    if intensity>0:
        #Return bgr
        return b,g,r
    else:
        #Return black
        return 0,0,0


#2 Texture Shader
#https://en.wikipedia.org/wiki/Gouraud_shading
def halfhalfShader(render,**kwargs):
    #We obtain our barycentric coordinates
    u,v,w=kwargs['barCoordinates']
    ta,tb,tc=kwargs['vertexTextureList']
    na,nb,nc=kwargs['vertexNormalList']
    b,g,r=kwargs['color']
    
    if render.activeTexture:
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w                            
        b,g,r= render.activeTexture.getTextureCoordinates(tx, ty)
    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    try:
        nz = na[2] * u + nb[2] * v + nc[2] * w
    except:
        nz=0
    #We create out normal for each point
    normal=[nx,ny,nz]
  
    intensity = float(render.mathGl.dotProductVector(normal, render.light))
    if intensity<0:
        intensity=0
    #We calculate the color for each pixel with its normal vector and light  
    b = b*intensity/255
    g = g*intensity/255
    r = r*intensity/255
    if render.activeTexture2:                           
        b2,g2,r2= render.activeTexture2.getTextureCoordinates(tx, ty)
        b += (b2/255) *(1-intensity)
        g += (g2/255) *(1-intensity)
        r += (r2/255) *(1-intensity)
    #Return bgr
    return b,g,r
    
#My Shader
def predominantColorShader(render,**kwargs):
    #We obtain our barycentric coordinates
    u,v,w=kwargs['barCoordinates']
    ta,tb,tc=kwargs['vertexTextureList']
    na,nb,nc=kwargs['vertexNormalList']
    b,g,r=kwargs['color']
    
    if render.activeTexture:
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w                            
        b,g,r= render.activeTexture.getTextureCoordinates(tx, ty)
    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    try:
        nz = na[2] * u + nb[2] * v + nc[2] * w
    except:
        nz=0
    #We create out normal for each point
    normal=[nx,ny,nz]
  
    intensity = float(render.mathGl.dotProductVector(normal, render.light))
    #We calculate the color for each pixel with its normal vector and light  

    # MD would be the percentage of x light this material will reflect.
    # LD be the percentage of x light the light source emits.
    
    if b>g and b>r:
        g=b
        r=b
    elif r>g and r>b:
        b=r
        g=r
    elif g>b and g>r:
        b=g
        r=g
    
    b = (b/255)*intensity
    g = (g/255)*intensity
    r = (r/255)*intensity
    
    if intensity>0:
        #Return bgr
        return b,g,r
    else:
        #Return black
        return 0,0,0

#Inverse Shader
def inverseShading(render,**kwargs):
    #We obtain our barycentric coordinates
    u,v,w=kwargs['barCoordinates']
    ta,tb,tc=kwargs['vertexTextureList']
    na,nb,nc=kwargs['vertexNormalList']
    b,g,r=kwargs['color']
    
    if render.activeTexture:
        tx = ta[0] * u + tb[0] * v + tc[0] * w
        ty = ta[1] * u + tb[1] * v + tc[1] * w                            
        b,g,r= render.activeTexture.getTextureCoordinates(tx, ty)
    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    try:
        nz = na[2] * u + nb[2] * v + nc[2] * w
    except:
        nz=0
    #We create out normal for each point
    normal=[nx,ny,nz]
  
    intensity = float(render.mathGl.dotProductVector(normal, render.light))
    #We calculate the color for each pixel with its normal vector and light  

    # MD would be the percentage of x light this material will reflect.
    # LD be the percentage of x light the light source emits.
    intensity=1-intensity
    # if b>g and b>r:
    #     g=b
    #     r=b
    # elif r>g and r>b:
    #     b=r
    #     g=r
    # elif g>b and g>r:
    #     b=g
    #     r=g
    
    b = (b/255)*intensity
    g = (g/255)*intensity
    r = (r/255)*intensity
    
    if intensity>0:
        #Return bgr
        return b,g,r
    else:
        #Return white
        return 0,0,0


#Normal Map
#https://learnopengl.com/Advanced-Lighting/Normal-Mapping
#And from example seen in class
def normalMapTexture(render,**kwargs):
    #We obtain our barycentric coordinates
    u,v,w=kwargs['barCoordinates']
    ta,tb,tc=kwargs['vertexTextureList']
    na,nb,nc=kwargs['vertexNormalList']
    vertexA,vertexB,vertexC=kwargs['vertexList']
    b,g,r=kwargs['color']
    tx = ta[0] * u + tb[0] * v + tc[0] * w
    ty = ta[1] * u + tb[1] * v + tc[1] * w    
    if render.activeTexture:                            
        b,g,r= render.activeTexture.getTextureCoordinates(tx, ty)
    nx = na[0] * u + nb[0] * v + nc[0] * w
    ny = na[1] * u + nb[1] * v + nc[1] * w
    try:
        nz = na[2] * u + nb[2] * v + nc[2] * w
    except:
        nz=0
    #We create out normal for each point
    normal=[nx,ny,nz]
    if render.activeNormalMap:
        bNM,gNM,rNM= render.activeNormalMap.getTextureCoordinates(tx, ty)
        #We convert rgb color to arange in -1 and 1
        normalMap = [(rNM/255)*2-1,(gNM/255)*2-1,(bNM/255)*2-1]
        normalMap = render.mathGl.normalizeVector(normalMap)
        #We need to get the tangent and bitangent to transform the normal map texture to Tangent Space
        #https://learnopengl.com/Advanced-Lighting/Normal-Mapping
        edge1= render.mathGl.subtractVector(vertexB,vertexA)
        edge2= render.mathGl.subtractVector(vertexC,vertexA)
        deltaUV1 = render.mathGl.subtractVector(tb, ta)
        deltaUV2 = render.mathGl.subtractVector(tc, ta)
        tangent = [0,0,0]
        f = 1 / (deltaUV1[0] * deltaUV2[1] - deltaUV2[0] * deltaUV1[1])
        tangent[0] = f * (deltaUV2[1] * edge1[0] - deltaUV1[1] * edge2[0])
        tangent[1] = f * (deltaUV2[1] * edge1[1] - deltaUV1[1] * edge2[1])
        tangent[2] = f * (deltaUV2[1] * edge1[2] - deltaUV1[1] * edge2[2])
        tangent = render.mathGl.normalizeVector(tangent)

        tangent = render.mathGl.subtractVector(tangent, render.mathGl.scalarMultiplicationVector(normal,render.mathGl.dotProductVector(tangent, normal)))
        #tangent = np.subtract(tangent, np.multiply(np.dot(tangent, normal),normal))
        tangent = render.mathGl.normalizeVector(tangent)

        bitangent = render.mathGl.crossVector(normal, tangent)
        bitangent = render.mathGl.normalizeVector(bitangent)

        #Now we calculate tangent matrix
        tangentMatrix = [[tangent[0],bitangent[0],normal[0]],
                                [tangent[1],bitangent[1],normal[1]],
                                [tangent[2],bitangent[2],normal[2]]]

        light = render.light
        light = render.mathGl.multiplyMatrix(tangentMatrix,light)
        light = render.mathGl.normalizeVector(light)
    
        #We calculate intensity with normalMap and newLight
        intensity = render.mathGl.dotProductVector(normalMap, light)
    else:
        intensity = float(render.mathGl.dotProductVector(normal, render.light))
    #We calculate the color for each pixel with its normal vector and light  
    b = b*intensity/255
    g = g*intensity/255
    r = r*intensity/255
    if intensity>0:
        #Return bgr
        return b,g,r
    else:
        #Return black
        return 0,0,0
#color function ro return rgb in bytes
def colorScale(r,g,b):
    return bytes([round(b*255),round(g*255),round(r*255)])


