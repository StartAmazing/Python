import unittest
from use_unittest import get_format_name

class NamesTestCase(unittest.TestCase):
    '''测试name_function.py'''
    def test_first_last_name(self):
        '''能够正确地处理像Janis Joplin这样的姓名吗？'''
        formatted_name = get_format_name('jains', 'joplin')
        self.assertEqual(formatted_name, "Jains Joplin")

    def test_first_middle_last_name(self):
        '''能够正确地处理像Janis Alan Joplin这样的姓名吗？'''
        formatted_name = get_format_name('jains', 'alan', 'joplin')
        self.assertEqual(formatted_name, "Jains Joplin Alan")


unittest.main()