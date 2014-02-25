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
		self.assertEqual(isinstance(pibrella.input.read(),dict),True)
	def test_all_non_calling_response(self):
		"""Test that all works with non-functions"""
		self.assertEqual(isinstance(pibrella.input.pin(),dict),True)
	def test_input_all(self):
		"""Test that we can read *all* inputs"""
		self.assertEqual(pibrella.input.read(),{'a':0,'b':0,'c':0,'d':0})
	def test_input_all_all(self):
		"""Test that we can access the iterator explicitly"""
		self.assertEqual(pibrella.input.all.read(),{'a':0,'b':0,'c':0,'d':0})

if __name__ == '__main__':
	unittest.main()
