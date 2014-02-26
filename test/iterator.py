import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import pibrella

if sys.version[:3] == '2.6':
	import unittest2 as unittest
else:
	import unittest

class TestAASanity(unittest.TestCase):
	def test_all_response(self):
		"""Test that all returns a dict"""
		self.assertTrue(isinstance(pibrella.input.read(),dict))
	def test_all_non_calling_response(self):
		"""Test that all works with non-functions"""
		self.assertTrue(isinstance(pibrella.input.pin(),dict))
	def test_input_all(self):
		"""Test that we can read *all* inputs"""
		self.assertEqual(pibrella.input.read(),{'a':0,'b':0,'c':0,'d':0})
	def test_collection_list(self):
		"""Test that we can see what's in a collection"""
		self.assertTrue("buzzer" in str(pibrella.pin))
	def test_accessor(self):
		"""Test that we can get a pin by name or index"""
		self.assertTrue(isinstance(pibrella.input[0],pibrella.Input))
		self.assertTrue(isinstance(pibrella.input['a'],pibrella.Input))

if __name__ == '__main__':
	unittest.main()
