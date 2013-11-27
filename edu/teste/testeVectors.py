'''
Created on 26/11/2013

@author: ANTONIO
'''

from edu.cg.vectors import Vector
from edu.cg.matrix import Matrix
import math
import pygame
from pygame.locals import QUIT
v1 = Vector( (4.0, 7.0) )
v2 = Vector( (1.0, 2.0) )

pygame.init()

# m1 = Matrix( [ [1.0, 2.0, 3.0], [4.0, 5.0, 6.0]] )
# m2 = Matrix( [ [4.0, 5.0, 6.0], [4.0, 5.0, 6.0], [4.0, 5.0, 6.0]] )

# m1 = Matrix( [ [1, 3], [5, 2], [0, 4] ])
# m2 = Matrix( [ [3, 6, 9, 4], [2, 7, 8, 3] ])

soma = 0
for i in range(1, 181):
    soma += i
print soma % 360, i 

ponto = Matrix([[4.0],[7.0]])
screen = pygame.display.set_mode((640, 480), 0, 32)
poligono = Matrix([ [50, 10], [50, 60], [150, 60], [150, 10], [50, 10] ])

print poligono.points
print (-poligono).points
 
pygame.draw.polygon( screen, (255, 0, 0), poligono.points, 2)
 
# 
# poligono

angulo = 0

while( True ):

    angulo += 1
    
    angulo = angulo % 360
    
#     print poligono.points
    polRotated = (-poligono).rotate(angulo)
#     print polRotated.points
    
    screen.fill( (0,0,0) )
    pygame.draw.polygon( screen, (255, 255, 0), poligono.points, 2)
    pygame.draw.polygon( screen, (255, 0, 0), (-polRotated).points, 2)
    pygame.display.update()

    for e in pygame.event.get():
        if (e.type == QUIT):
            exit()

