import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella


if sys.version[:3] == '2.6':
	import unittest2 as unittest
else:
	import unittest

class TestAASanity(unittest.TestCase):
	def test_light_exists(self):
		"""Test that each light exists"""
		self.assertEqual(isinstance(pibrella.light.red,pibrella.Light),True)
		self.assertEqual(isinstance(pibrella.light.yellow,pibrella.Light),True)
		self.assertEqual(isinstance(pibrella.light.green,pibrella.Light),True)
		self.assertEqual(isinstance(pibrella.light.amber,pibrella.Light),True)

	def test_light_index(self):
		"""Test that each output is at the correct index"""
		self.assertEqual(pibrella.light.green,pibrella.light[2])
		self.assertEqual(pibrella.light.yellow,pibrella.light[1])
		self.assertEqual(pibrella.light.red,pibrella.light[0])

	def test_light_alias(self):
		"""Test that Amber and Yellow are the same"""
		self.assertEqual(pibrella.light.yellow,pibrella.light.amber)

if __name__ == '__main__':
	unittest.main()
