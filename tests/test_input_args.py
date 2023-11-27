import unittest
from unittest.mock import patch
from codefermenter.input_args import get_app_params
from codefermenter import enums


class TestFileConversionUtility(unittest.TestCase):
    """
    This test class contains unit tests for the file conversion utility to ensure
    the correct parsing and validation of command-line arguments.
    """

    def test_validation_direct_direct_files(self):
        """
        Test the command-line validation logic when invalid 'direct' option usage is detected.
        It should raise a SystemExit when '--direct-files' is passed with a string containing
        invalid format (e.g., starting with a number followed by '#' symbol).
        """
        test_args = ['', 'direct', '--direct-files', '13#file1.py,./file2.py']
        with self.assertRaises(SystemExit):
            with patch('sys.argv', test_args):
                get_app_params()

        test_args = ['', 'direct', '--direct-files', 'file1.py,./file2.py']
        with self.assertRaises(SystemExit):
            with patch('sys.argv', test_args):
                get_app_params()

    def test_validation_recursive_direct_files(self):
        """
        Test the command-line validation logic when 'recursive' option is used incorrectly.
        It should raise a SystemExit when '--source-dir' is passed with a string that
        contains invalid format (e.g., begins with 'path#' instead of a valid path).
        """
        test_args = ['', 'recursive', '--source-dir', 'path#/to/dir']
        with self.assertRaises(SystemExit):
            with patch('sys.argv', test_args):
                get_app_params()

    def test_parse_app_parameters_recursive(self):
        """
        Test the parsing of application parameters for recursive file processing.
        It should properly interpret the command-line arguments, setting the appropriate
        attributes on the params object for recursive directory processing.
        """
        test_args = ['', '--remove-source', 'recursive', '--source-dir', '/path/to/dir']
        with patch('sys.argv', test_args):
            params = get_app_params()
            self.assertEqual(params.preparing_type, enums.PreparingType.RECURSIVE)
            self.assertEqual(params.source_dir, '/path/to/dir')
            self.assertTrue(params.remove_source)

    def test_parse_app_parameters_direct(self):
        """
        Test the parsing of application parameters for direct file processing.
        It should correctly parse the command-line arguments and set the direct file
        processing attributes on the params object.
        """
        test_args = ['', '--remove-source', 'direct', '--direct-files', './file1.py,./file2.py']
        with patch('sys.argv', test_args):
            params = get_app_params()
            self.assertEqual(params.preparing_type, enums.PreparingType.DIRECT)
            self.assertEqual(params.direct_files, ['./file1.py', './file2.py'])
            self.assertTrue(params.remove_source)

if __name__ == '__main__':
    unittest.main()