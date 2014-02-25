import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella


if sys.version[:3] == '2.6':
	import unittest2 as unittest
else:
	import unittest

class TestAASanity(unittest.TestCase):
	def test_inputexists(self):
		"""Test that each input exists"""
		self.assertEqual(isinstance(pibrella.input.a,pibrella.Input),True)
		self.assertEqual(isinstance(pibrella.input.b,pibrella.Input),True)
		self.assertEqual(isinstance(pibrella.input.c,pibrella.Input),True)
		self.assertEqual(isinstance(pibrella.input.d,pibrella.Input),True)

	def test_input_index(self):
		"""Test that each input is at the correct index"""
		self.assertEqual(pibrella.input.a,pibrella.input[0])
		self.assertEqual(pibrella.input.b,pibrella.input[1])
		self.assertEqual(pibrella.input.c,pibrella.input[2])
		self.assertEqual(pibrella.input.d,pibrella.input[3])

class TestBBInput(unittest.TestCase):
	def test_inputread(self):
		"""Test that an input can be read()"""
		self.assertEqual(pibrella.input.a.read(), 0)
		self.assertEqual(pibrella.input.b.read(), 0)
		self.assertEqual(pibrella.input.c.read(), 0)
		self.assertEqual(pibrella.input.d.read(), 0)

if __name__ == '__main__':
	unittest.main()
