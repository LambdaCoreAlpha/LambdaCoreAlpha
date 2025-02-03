import unittest  
from src.core import ilahi_optimizasyon  

class TestLambdaCore(unittest.TestCase):  
    def test_ilahi_optimizasyon(self):  
        self.assertEqual(ilahi_optimizasyon(5), 10)  
        self.assertEqual(ilahi_optimizasyon(10), 20)  

if __name__ == "__main__":  
    unittest.main()
