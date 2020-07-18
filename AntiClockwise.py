import math
import os
import random
import re
import sys
def matrixRotation(matrix, r):
    #r=n times of rotation of matrix
    row=len(matrix) 
    col=len(matrix[0])
    layer=0
    #get number of layers in your matrix
    if row > col:
        layer=col//2
    else:
        layer=row//2
        
    lcm=[] #list for number of element in each layer
    newr = r
    listr=[] #list for each layer to complete its one loop in n rotation
    
    for i in range(layer):
        n=(col*2)+(row-2)*2
        col -= 2
        row -=2
        lcm.append(n)#append number of element of each layer in list
    # its makes rotation very fast for big matrix or number of rotaion time
    for i in lcm:
        if r>i:
            listr.append(newr%i) # append remainder n times after completing loop
        else:
            listr.append(newr)

    #its make rotation fast if number of layer is low and rotation time is very high
    common=lcm[0] 
    for i in lcm[1:]:
        common= int(common*i/math.gcd(common,i))
        #they will align same at this number
    if r > common:
        r =r%common
#rotation for matrix of each element of each layer in anti clock wise direction
    top = 0
    bottom = len(matrix)-1

    left = 0
    right = len(matrix[0])-1
    
    for z in listr:#get rotation time for each layer
        for x in range(z):
            
            prev = matrix[top+1][right]
            for i in range(right,left-1,-1):
                curr = matrix[top][i]
                matrix[top][i]= prev
                prev =curr
            
            for i in range(top+1,bottom+1):
                curr = matrix[i][left]
                matrix[i][left]=prev
                prev=curr
            
            for i in range(left+1,right+1):
                curr =matrix[bottom][i]
                matrix[bottom][i]=prev
                prev = curr
            
            for i in range(bottom-1,top-1,-1):
                curr = matrix[i][right]
                matrix[i][right]=prev
                prev = curr
        #get lower Layer
        right -=1
        left +=1
        bottom -=1
        top +=1
   
    for  i in matrix:
        print(str(i)[1:-1].replace(",",""))
    
     
        

if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r)
