# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import unittest
from Funcion import *
class PruebaTresMayores(unittest.TestCase):
    def test_prueva(self):
        self.assertEquals(mayor(1,3,-4),3)
        self.assertEquals(mayor(0,0,0),0)
        self.assertEquals(mayor(2,1,-1),2)
        self.assertEquals(mayor(5,6,7),7)
        self.assertEquals(mayor(-1,-1,0),0)
        self.assertEquals(mayor(1,2,2),2)
        self.assertEquals(mayor(3,4,3),4)
        self.assertEquals(mayor(5,4,3),5)
        self.assertEquals(mayor(-1,-23,-1),-1)
if __name__ == "__main__":
    unittest.main()
