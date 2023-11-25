import unittest
import argparse
from unittest.mock import patch
from codefermenter.input_args import get_app_params
from codefermenter.input_args import CommandManager, CommandDirect, CommandRecursive
from codefermenter import enums


class TestFileConversionUtility(unittest.TestCase):

    def test_validation_direct_direct_files(self):
        test_args = ['', 'direct', '--direct-files', '13#file1.py,./file2.py']
        with self.assertRaises(SystemExit):
            with patch('sys.argv', test_args):
                get_app_params()

        test_args = ['', 'direct', '--direct-files', 'file1.py,./file2.py']
        with self.assertRaises(SystemExit):
            with patch('sys.argv', test_args):
                get_app_params()


    def test_validation_recursive_direct_files(self):
        test_args = ['', 'recursive', '--source-dir', 'path#/to/dir']
        with self.assertRaises(SystemExit):
            with patch('sys.argv', test_args):
                get_app_params()


    def test_parse_app_parameters_recursive(self):
        test_args = ['', '--remove-source', 'recursive', '--source-dir', '/path/to/dir', ]
        with patch('sys.argv', test_args):
            params = get_app_params()
            self.assertEqual(params.preparing_type, enums.PreparingType.RECURSIVE)
            self.assertEqual(params.source_dir, '/path/to/dir')
            self.assertTrue(params.remove_source)


    def test_parse_app_parameters_direct(self):
        test_args = ['', '--remove-source', 'direct', '--direct-files', './file1.py,./file2.py']
        with patch('sys.argv', test_args):
            params = get_app_params()
            self.assertEqual(params.preparing_type, enums.PreparingType.DIRECT)
            self.assertEqual(params.direct_files, ['./file1.py', './file2.py'])
            self.assertTrue(params.remove_source)

if __name__ == '__main__':
    unittest.main()
