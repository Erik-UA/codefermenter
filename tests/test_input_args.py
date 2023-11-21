import unittest
import argparse
from unittest.mock import patch
from codefermenter.input_args.app_args import create_main_parser, create_app_parameters_for_recursive, create_app_parameters_for_direct, parse_app_parameters
from codefermenter import enums


class TestFileConversionUtility(unittest.TestCase):

    def test_validation_direct_direct_files(self):
        test_args = ['', 'direct', '--direct-files', '13#file1.py,./file2.py']
        with self.assertRaises(SystemExit):
            with patch('sys.argv', test_args):
                parse_app_parameters()

        test_args = ['', 'direct', '--direct-files', 'file1.py,./file2.py']
        with self.assertRaises(SystemExit):
            with patch('sys.argv', test_args):
                parse_app_parameters()


    def test_validation_recursive_direct_files(self):
        test_args = ['', 'recursive', '--source-dir', 'path#/to/dir']
        with self.assertRaises(SystemExit):
            with patch('sys.argv', test_args):
                parse_app_parameters()


    def test_add_recursive_parser(self):
        parser = create_main_parser()
        # Assuming 'recursive' is a valid command for the parser
        args = parser.parse_args(['recursive', '--source-dir', '/path/to/dir'])
        self.assertEqual(args.command, 'recursive')
        self.assertEqual(args.source_dir, '/path/to/dir')

    def test_add_direct_parser(self):
        parser = create_main_parser()
        args = parser.parse_args(['direct', '--direct-files', '../src/file1.py, /tmp/file2.py'])
        self.assertEqual(args.command, 'direct')
        self.assertEqual(args.direct_files, ['../src/file1.py', '/tmp/file2.py'])

    def test_create_app_parameters_for_recursive(self):
        args = lambda: None  # Mock args object
        setattr(args, 'source_dir', '/path/to/dir')
        setattr(args, 'exclude_directories', None)
        setattr(args, 'exclude_files', None)
        setattr(args, 'remove_source', True)

        result = create_app_parameters_for_recursive(args)
        self.assertEqual(result.preparing_type, enums.PreparingType.RECURSIVE)
        self.assertEqual(result.source_dir, '/path/to/dir')
        self.assertTrue(result.remove_source)

    def test_create_app_parameters_for_direct(self):
        args = lambda: None  # Mock args object
        setattr(args, 'direct_files', ['./file1.py', './file2.py'])
        setattr(args, 'remove_source', False)

        result = create_app_parameters_for_direct(args)
        self.assertEqual(result.preparing_type, enums.PreparingType.DIRECT)
        self.assertEqual(result.direct_files, ['./file1.py', './file2.py'])
        self.assertFalse(result.remove_source)

    def test_parse_app_parameters_recursive(self):
        test_args = ['', '--remove-source', 'recursive', '--source-dir', '/path/to/dir', ]
        with patch('sys.argv', test_args):
            params = parse_app_parameters()
            self.assertEqual(params.preparing_type, enums.PreparingType.RECURSIVE)
            self.assertEqual(params.source_dir, '/path/to/dir')
            self.assertTrue(params.remove_source)

    def test_parse_app_parameters_direct(self):
        test_args = ['', '--remove-source', 'direct', '--direct-files', './file1.py,./file2.py']
        with patch('sys.argv', test_args):
            params = parse_app_parameters()
            self.assertEqual(params.preparing_type, enums.PreparingType.DIRECT)
            self.assertEqual(params.direct_files, ['./file1.py', './file2.py'])
            self.assertTrue(params.remove_source)

if __name__ == '__main__':
    unittest.main()
