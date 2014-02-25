import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella


if sys.version[:3] == '2.6':
	import unittest2 as unittest
else:
	import unittest

class TestAASanity(unittest.TestCase):
	def test_inputexists(self):
		"""Test that button exists"""
		self.assertEqual(isinstance(pibrella.button,pibrella.Button),True)

class TestBBInput(unittest.TestCase):
	def test_inputread(self):
		"""Test that button can be read()"""
		self.assertEqual(pibrella.button.read(), 0)

if __name__ == '__main__':
	unittest.main()
