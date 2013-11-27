'''
Created on 26/11/2013

@author: ANTONIO
'''
import exceptions
import math

class Matrix():
    
    def __init__(self, array):
        self.points = array
        
        
    def __add__(self, otherVector):
        if (len (otherVector.points) == len(self.points)):
            newMatrix = []
            for indexLinha in range(len(self.points)):
                newVector = []
                for indexColuna in range(len(self.points[indexLinha])):
                    newVector.append( self.points[indexLinha][indexColuna] + otherVector.points[indexLinha][indexColuna] );
                newMatrix.append( newVector )
            print "soma : ", self.points, "   +   ", otherVector.points, "   =    ", newMatrix
            return newMatrix
        else:
            exceptions.ValueError("Quantidade de elementos diferentes na Matriz")
            return None
        
    def __mul__(self, otherVector):
        if (len (otherVector.points) == len(self.points)):
            newMatrix = []
            for indexLinha in range(len(self.points)):
                newVector = []
                for indexColuna in range(len(self.points[indexLinha])):
                    newVector.append( self.points[indexLinha][indexColuna] * otherVector.points[indexLinha][indexColuna] );
                newMatrix.append( newVector )
            print "multiplicacao : ", self.points, "   *   ", otherVector.points, "   =    ", newMatrix
            return newMatrix
        else:
            exceptions.ValueError("Quantidade de elementos diferentes na Matriz")
            return None
        
    def __neg__(self):
        return Matrix([[self.points[l][c] for l in range(len(self.points))] for c in range(len(self.points[0]))])
    
        

    def __pow__(self, otherMatrix):
#         print "Cross Product : " , self.points ,"  with   " , otherMatrix.points
        novaMatriz = [[0 for _ in range(len(otherMatrix.points[0]))] for m in self.points]
        for l in range(len(novaMatriz)):
            for c in range(len(novaMatriz[l])):
                soma = 0
                for indice in range(len(self.points[l])):
                    soma += (self.points[l][indice] * otherMatrix.points[indice][c])
                novaMatriz[l][c] = soma
        return Matrix(novaMatriz) 
        
    def __len__(self):
        return len(self.points)
    
    def __getitem__(self):
        return self
    
    def rotate(self, angulo):
        rotacaoRadians = angulo * math.pi / 180
        senoAngulo = math.sin(rotacaoRadians)
        cosAngulo = math.cos(rotacaoRadians)
        rotationMatrix = Matrix( [[ cosAngulo, -senoAngulo ], [ senoAngulo, cosAngulo ]])
        return rotationMatrix ** self
        