import unittest
from unittest.mock import patch
from io import StringIO
import mastermind

class TestCase(unittest.TestCase):

    def test_create_code(self):
      result = mastermind.create_code()
      self.assertEqual (type(result), list)
      self.assertEqual (len(result), 4)
      inrange = True
      if 0 in result or 9 in result:
        inrange = False
      self.assertEqual(inrange, True)

    @patch("sys.stdin", StringIO("1234\n2345\nasdf"))
    def test_get_answer(self):
      self.assertEqual(mastermind.get_answer(),"1234")
      self.assertEqual(mastermind.get_answer(),"2345")
      #self.assertEqual(mastermind.get_answer(),"125")
      #self.assertEqual(mastermind.get_answer(),"asdf")

    def test_check_correctness(self):
      self.assertTrue(mastermind.check_correctness((4, 0), 0))
      self.assertFalse(mastermind.check_correctness((0, 4), 0))
      self.assertFalse(mastermind.check_correctness((1, 3), 0))
      self.assertFalse(mastermind.check_correctness((2, 2), 0))
      self.assertFalse(mastermind.check_correctness((3, 1), 0))

if __name__ == '__main__':                          
    unittest.main()