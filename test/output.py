import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella


if sys.version[:3] == '2.6':
	import unittest2 as unittest
else:
	import unittest

class TestAASanity(unittest.TestCase):
	def test_outputexists(self):
		"""Test that each output exists"""
		self.assertEqual(isinstance(pibrella.output.e,pibrella.Output),True)
		self.assertEqual(isinstance(pibrella.output.f,pibrella.Output),True)
		self.assertEqual(isinstance(pibrella.output.g,pibrella.Output),True)
		self.assertEqual(isinstance(pibrella.output.h,pibrella.Output),True)

	def test_output_index(self):
		"""Test that each output is at the correct index"""
		self.assertEqual(pibrella.output.e,pibrella.output[0])
		self.assertEqual(pibrella.output.f,pibrella.output[1])
		self.assertEqual(pibrella.output.g,pibrella.output[2])
		self.assertEqual(pibrella.output.h,pibrella.output[3])

class TestBBInput(unittest.TestCase):
	def test_outputwrite(self):
		"""Test that an output can be write()"""
		pibrella.output.e.write(1)
		self.assertEqual(pibrella.output.e.read(),1)

		pibrella.output.f.write(1)
		self.assertEqual(pibrella.output.f.read(),1)
		
		pibrella.output.g.write(1)
		self.assertEqual(pibrella.output.g.read(),1)

		pibrella.output.h.write(1)
		self.assertEqual(pibrella.output.h.read(),1)

if __name__ == '__main__':
	unittest.main()
