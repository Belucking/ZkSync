# test_zksyncprove.py
"""
Tests for ZkSyncProve module.
"""

import unittest
from zksyncprove import ZkSyncProve

class TestZkSyncProve(unittest.TestCase):
    """Test cases for ZkSyncProve class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ZkSyncProve()
        self.assertIsInstance(instance, ZkSyncProve)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ZkSyncProve()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
