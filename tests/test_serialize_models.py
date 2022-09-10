import sys, os
import unittest
from serialize_models import deserialize
os.chdir("D:\\10XAcademy\\Ad-campaign-performance")
path_to_module = os.path.abspath(os.getcwd()+"\\scripts")
if path_to_module not in sys.path:
    sys.path.append(path_to_module)

class TestCases(unittest.TestCase):
     def test_deserializing(filePath):
        """
         an assertion level for opening pickle files
        """
        assert os.path.exists(deserialize(filePath)) == False, "File does not exist"

if __name__ == '__main__':
    unittest.main()