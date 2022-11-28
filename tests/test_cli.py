import argparse
import unittest

from unittest.mock import patch, mock_open

from main.cli import parser, read_file
from main.exception import NotArgument, FileDoesNotExist


class TestParser(unittest.TestCase):

    @patch('main.cli.open', mock_open(read_data='qwe'))
    def test_read_file(self):
        self.assertEqual(read_file('file_name'), 'qwe')

    @patch('main.cli.read_file', return_value='asd')
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(string=None, file='text.txt'))
    def test_file_command(self, mock_args, mock_read_file):
        self.assertEqual(parser(), 3)
        mock_args.assert_called_once()
        mock_read_file.assert_called_with('text.txt')

    @patch('main.cli.count_unical_symbol', return_value=3)
    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(string='asd', file=None))
    def test_string_command(self, mock_args, mock_count):
        self.assertEqual(parser(), 3)
        mock_args.assert_called_once()
        mock_count.assert_called_with('asd')

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(string=None, file=None))
    def test_exeption_non_argument_string(self, mock_args):
        self.assertRaises(NotArgument, msg="Use '--string' or '--file command'")
        mock_args.assert_not_called()

    @patch('argparse.ArgumentParser.parse_args', return_value=argparse.Namespace(string=None, file='asd'))
    def test_wrong_file_way(self, mock_way):
        self.assertRaises(FileDoesNotExist, msg="The specified file does not exist")
        mock_way.assert_not_called()
