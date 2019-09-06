#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pygame
import numpy as np
import sys
import math

# In[ ]:


import math
import sys
print("Enter initial node cordinates")
xi=float(input("x =  "))
yi=float(input("y =  "))
ndi=[xi,yi]
print("Enter goal node cordinates")
xg=float(input("x =  "))
yg=float(input("y =  "))
goal=[xg,yg]
r=int(input("Enter Resolution (must be an integer value) =  "))

goal= [n / r for n in goal]
ndi=[m / r for m in ndi]

rows=150/r
coloums=250/r


# In[ ]:


def heu(node):
    h = math.sqrt ( (node[0] - goal[0])**2 +  (node[1] - goal[1])**2 )
    return h


# In[ ]:


def left(ct_nd):
    n_nd=[0,0]
    n_nd[0]=ct_nd[0]-1
    n_nd[1]=ct_nd[1]
    cost=1
    return n_nd,cost

def right(ct_nd):
    n_nd=[0,0]
    n_nd[0]=ct_nd[0]+1
    n_nd[1]=ct_nd[1]
    cost=1
    return n_nd,cost

def down(ct_nd):
    n_nd=[0,0]
    n_nd[0]=ct_nd[0]
    n_nd[1]=ct_nd[1]+1
    cost=1
    return n_nd,cost

def up(ct_nd):
    n_nd=[0,0]
    n_nd[0]=ct_nd[0]
    n_nd[1]=ct_nd[1]-1
    cost=1
    return n_nd,cost

def down_left(ct_nd):
    n_nd=[0,0]
    n_nd[0]=ct_nd[0]-1
    n_nd[1]=ct_nd[1]+1
    cost=1.42
    return n_nd,cost

def up_left(ct_nd):
    n_nd=[0,0]
    n_nd[0]=ct_nd[0]-1
    n_nd[1]=ct_nd[1]-1
    cost=1.42
    return n_nd,cost
                  
def up_right(ct_nd):
    n_nd=[0,0]
    n_nd[0]=ct_nd[0]+1
    n_nd[1]=ct_nd[1]-1
    cost=1.42
    return n_nd,cost
                  
def down_right(ct_nd):
    n_nd=[0,0]
    n_nd[0]=ct_nd[0]+1
    n_nd[1]=ct_nd[1]+1
    cost=1.42
    return n_nd,cost



def obstacle_space(x,y,r):
    c = 0
    if ((x-math.ceil(190/r))**2+math.ceil(y-(130/r))**2-math.ceil(15/r)**2)<=0:
        c=1
    if (2*x + 19*y - 1314/r <= 0) and (41*x+ 25*y -6525/r >= 0) and (y - 15/r>= 0) and (37*x +10*y - 6551/r <= 0):
        c=1
    if (38*x- 7*y - 5830/r >= 0) and (38*x + 23*y - 8530/r <= 0) and (37*x -20*y -6101/r <= 0) and (37*x +10*y - 6551/r >= 0):
        c=1
    if (x-math.floor(50/r) >= 0) and (x - math.floor(100/r) <= 0) and (y - math.floor(67.5/r) >= 0) and (y - math.floor(112.5/r) <= 0):
        c=1
    if ((x-math.ceil(140/r))/math.ceil(15/r))**2 + ((y - math.ceil(120/r))/math.ceil(6/r))**2 - 1 <=0:
        c=1
    return c


# In[ ]:





# In[ ]:


p_nd=[ndi]
c_nd=[ndi]
h_nd=[round(heu(ndi),2)]
vp_nd=[]
vc_nd=[]
v_cst=[]
vh_nd=[]

if (obstacle_space(goal[0],goal[1],r)==1 or obstacle_space(ndi[0],ndi[1],r)):
    sys.exit("Either goal node or start node lies inside obstacle or outside the workspace")

if (ndi[0] not in range(0,251) or goal[0] not in range(0,251) or ndi[1] not in range(0,151) or goal[1] not in range(0,151)):
    sys.exit("Entered node cordinates are not integers or outside the workspace or invalid resolution")


# In[ ]:




x=0
cst=[0]
ndx=ndi
flag=0
exit=0
count=0
while(flag!=1):
    
    #--- UP Command ---
    nd,cost=up(ndx)
    if (nd[1]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in vc_nd:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
                h_nd.append(round((cost+cst[x]+heu(nd)),2))
            
            
    #--- DOWN Command ---
    nd,cost=down(ndx)
    if (nd[1]<=rows and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in vc_nd:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
                h_nd.append(round((cost+cst[x]+heu(nd)),2))
            
            
    #--- LEFT Command ---
    nd,cost=left(ndx)
    if (nd[0]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in vc_nd:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
                h_nd.append(round((cost+cst[x]+heu(nd)),2))
            

    #--- RIGHT Command ---
    nd,cost=right(ndx)
    if (nd[0]<=coloums and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in vc_nd:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
                h_nd.append(round((cost+cst[x]+heu(nd)),2))


            
    #--- UP LEFT Command ---
    nd,cost=up_left(ndx)
    if (nd[1]>=0 and nd[0]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in vc_nd:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
                h_nd.append(round((cost+cst[x]+heu(nd)),2))


            
    #--- UP RIGHT Command ---
    nd,cost=up_right(ndx)
    if (nd[0]<=coloums and nd[1]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in vc_nd:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
                h_nd.append(round((cost+cst[x]+heu(nd)),2))


            
    #--- DOWN LEFT Command ---
    nd,cost=down_left(ndx)
    if (nd[1]<=rows and nd[0]>=0 and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in vc_nd:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
                h_nd.append(round((cost+cst[x]+heu(nd)),2))


            
    #--- DOWN RIGHT Command ---
    nd,cost=down_right(ndx)
    if (nd[1]<=rows and nd[0]<=coloums and obstacle_space(nd[0],nd[1],r)!=1):
        if nd not in vc_nd:
            xl=range(0,len(c_nd))
            xl=xl[::-1]
            check=0
            for cku in xl:
                if(nd == c_nd[cku]):
                    check=1
                    if(cst[cku]>=(cst[x]+cost)):
                        p_nd[cku]=ndx
                        cst[cku]=round((cst[x]+cost),1)
                        break
                    
                    
            if (check!=1):
                p_nd.append(ndx)
                c_nd.append(nd)
                cst.append(round((cost+cst[x]),1))
                h_nd.append(round((cost+cst[x]+heu(nd)),2))


            
    vp_nd.append(p_nd.pop(x))
    vc_nd.append(c_nd.pop(x))
    v_cst.append(cst.pop(x))
    vh_nd.append(h_nd.pop(x))
    
    
    if(vc_nd[-1]==goal):
        flag=1
        
    if(flag!=1):
        x=h_nd.index(min(h_nd))
        ndx=c_nd[x][:]
    


seq=[]
seq.append(vc_nd[-1])
seq.append(vp_nd[-1])
x=vp_nd[-1]
i=1
while(x!=ndi):
    if(vc_nd[-i]==x):
        seq.append(vp_nd[-i])
        x=vp_nd[-i]
    i=i+1     







# In[ ]:





# In[ ]:


obs_space = []
for i in range(0,251):
    for j in range(0,151):
        q=obstacle_space(i,j,r)
        if q == 1:
            obs_space.append([i,j])

k=2
my_list = np.array(vc_nd)
vc_nd=my_list*k*r
my_list1 = np.array(seq)
seq=my_list1*k*r
my_list2 = np.array(obs_space)
obs_space = my_list2*k*r


pygame.init()

#Defining the colors
Black = [0, 0, 0]
red = [255, 0, 0]
Blue = [0, 100, 255]
White = [255, 255, 255]

#Height and Width of Display
SIZE = [250*k+r+r, 150*k+r+r]
screen = pygame.display.set_mode(SIZE)

pygame.display.set_caption("OUTPUT")
clock = pygame.time.Clock()
done = False
while not done:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:  
            done = True   
 
    screen.fill(Black)
#Printing the obstacles
    for i in obs_space:
        pygame.draw.rect(screen, Blue, [i[0],150*k-i[1],r*k,r*k])
    pygame.display.flip()
    clock.tick(20)
#Printing the visited nodes
    for i in vc_nd:
        pygame.time.wait(1)
        pygame.draw.rect(screen, White, [i[0],150*k-i[1],r*k,r*k])
        pygame.display.flip()
#Printing the path
    for j in seq[::-1]:
        pygame.time.wait(1)
        pygame.draw.rect(screen, red, [j[0], 150*k-j[1], r*k,r*k])
        pygame.display.flip()
    pygame.display.flip()

    pygame.time.wait(1500)
    done = True
pygame.quit()


# In[ ]:





# In[ ]:




