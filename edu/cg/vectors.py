'''
Created on 26/11/2013

@author: ANTONIO
'''
import exceptions

class Vector():
    
    def __init__(self, points):
        self.points = points
        
        
    def __add__(self, otherVector):
        if (len (otherVector) == len(self.points)):
            newVector = []
            for index in range(len(self.points)):
                newVector.append( self.points[index] + otherVector.points[index] );
            print "soma : ", self.points, "   +   ", otherVector.points, "   =    ", newVector
            return newVector
        else:
            exceptions.ValueError("Quantidade de elementos diferentes no vetor")
            return None
        
    def __mul__(self, otherVector):
        if (len (otherVector) == len(self.points)):
            newVector = []
            for index in range(len(self.points)):
                newVector.append( self.points[index] * otherVector.points[index] );
            print "multiplicacao : ", self.points, "   *   ", otherVector.points, "   =    ", newVector
            return newVector
        else:
            exceptions.ValueError("Quantidade de elementos diferentes no vetor")
            return None
        
    
        
    def __len__(self):
        return len(self.points)
    
    def __getitem__(self):
        return self
        