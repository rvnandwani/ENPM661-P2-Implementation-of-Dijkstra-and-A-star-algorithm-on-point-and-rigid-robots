#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pygame
import math
import sys
import numpy as np


# In[14]:




print("Enter robot parameters")
rad=float(input("radius =  "))
clr=float(input("clearence =  "))

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





# In[15]:


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

def obstacle_space_disp(x,y,r):
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

def obstacle_space(x,y,r,d=rad+clr):
    line1=(6525.0/25) - d*math.sqrt((-41.0/25)**2+1)
    line2=d*math.sqrt((-2.0/19)**2+1)+(1314.0/19)
    line3=d*math.sqrt((38.0/7)**2+1)-(5830.0/7)
    line4=(6101.0/20)-d*math.sqrt((37.0/20)**2+1)
    line5= d*math.sqrt((-38.0/23)**2+1) + (8530.0/23)
    line6l= (6551.0/10)- d*math.sqrt((-37.0/10)**2+1)
    line6r=  d*math.sqrt((-37.0/10)**2+1) +(6551.0/10)
    q = 0
    if (x<(d/r))or (x>(250-d)/r) or (y<(d/r)) or (y>(150-d)/r):
        q=1
    if ((x-math.ceil(190/r))**2+(y-math.ceil(130/r))**2-(math.ceil((15+d)/r))**2)<0:
        q=1
    if ((2.0/19)*x + y - line2/r < 0) and (y+(41.0/25)*x -line1/r > 0) and (y - ((15-d)/r)> 0) and (y<(-37.0/10)*x+line6r/r):
        q=1
    if ((-38.0/7)*x +y - line3/r < 0) and ((38.0/23)*x + y - line5/r < 0)  and ((-37.0/20)*x +y +line4/r > 0) and (y>(-37.0/10)*x+line6l/r):
        q=1
    if (x-math.floor((50-d)/r) > 0) and (x - math.floor((100+d)/r) < 0) and (y - math.floor((67.5-d)/r) > 0) and (y - math.floor((112.5+d)/r) < 0):
        q=1
    if ((x-math.ceil(140/r))/(math.ceil(15+d)/r))**2 + ((y - math.ceil(120/r))/(math.ceil(6+d)/r))**2 - 1 < 0:
        q=1
    return q

# In[16]:


p_nd=[ndi]
c_nd=[ndi]
vp_nd=[]
vc_nd=[]
v_cst=[]


if (obstacle_space(goal[0],goal[1],r)==1 or obstacle_space(ndi[0],ndi[1],r)):
    sys.exit("Either goal node or start node lies inside obstacle or outside workspace")

if (ndi[0] not in range(0,251) or goal[0] not in range(0,251) or ndi[1] not in range(0,151) or goal[1] not in range(0,151)):
    sys.exit("Entered node cordinates are not integers or invalid resolution")


# In[17]:



x=0
cst=[0]
ndx=ndi
flag=0

while(flag!=1 and c_nd!=[]):
    
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
            
            
    #--- DOWN Command ---
    nd,cost=down(ndx)
    if (nd[1]<=rows and obstacle_space(nd[0],nd[1],5)!=1):
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

            
    vp_nd.append(p_nd.pop(x))
    vc_nd.append(c_nd.pop(x))
    v_cst.append(cst.pop(x))
    
    if(vc_nd[-1]==goal):
        flag=1
        
    if(flag!=1 and c_nd!=[]):
        x=cst.index(min(cst))
        ndx=c_nd[x][:]
    
if(flag==0 and c_nd==[]):
    sys.exit("Path not found")
    

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





# In[18]:


obs_space = []
for i in range(0,251):
    for j in range(0,151):
        q=obstacle_space_disp(i,j,r)
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





# In[ ]:





# In[ ]:





# In[ ]:




