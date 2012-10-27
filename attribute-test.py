import attribute
import link
import unittest

class TestAttributeMethods(unittest.TestCase):

    def setUp(self):
        self.a = attribute.Attribute()
        self.b = attribute.Attribute()

    def test_setAndGet(self):
        self.a.set(10)
        self.assertEqual(self.a.get(), 10)

    def test_fixedAponSet(self):
        self.assertEqual(self.a.state, link.FLOATING)
        self.a.set(1)
        self.assertEqual(self.a.state, link.FIXED)
        
    def test_linking1(self):
        self.b.linkTo(self.a)
        self.a.set(5)
        self.assertEqual(self.b.get(), 5)    

    def test_linking2(self):
        self.a.set(5)
        self.b.linkTo(self.a)
        self.assertEqual(self.b.get(), 5)
        
    def test_addConstOperator(self):
        self.d = self.a + 10
        self.a.set(4)
        self.assertEqual(self.d.get(), 14)

    def test_addOperator(self):
        self.d = self.a + self.b
        self.a.set(4)
        self.b.set(5)
        self.assertEqual(self.d.get(), 9)
        
    def test_linkByOperator(self):
        self.b << self.a
        self.a.set(2)
        self.assertEqual(self.b.get(), 2)
        
    def test_setByOperator1(self):
        self.b << self.a
        self.a << 5
        self.assertEqual(self.b.get(), 5)  
        
    def test_setByOperator2(self):
        self.a << 3
        self.b << self.a
        self.assertEqual(self.b.get(), 3)          