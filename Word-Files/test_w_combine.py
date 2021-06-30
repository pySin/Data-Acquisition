# Test Combine Word script

import unittest
from combine_word_files import integrate_f
import os

class test_results(unittest.TestCase):

    # Create variables to test.
    path = 'C:/Users/Sinan/Desktop/python/TaskFunctions/test_w_files'
    ob = integrate_f()
    docx_files = ob.filter_files(path, '.*\.docx')
    file_text = ob.read_docx(path, 'the_plan.docx')
    combined_text = ob.combine_texts(path, docx_files)

    # Can this function find the right number of .docx files?
    def test_1_filter_files(self):
        self.assertEqual(len(self.docx_files), 4, 'Files should be 4!')

    # Can this function read a .docx file?
    def test_2_read_read(self):
        self.assertTrue(len(self.file_text) > 1, 'File reading problem!')

    # Is the text from all .docx files bigger than the text from 1 file?
    def test_3_combine_texts(self):
        self.assertTrue(len(self.combined_text) > len(self.file_text))

    # Does this function really create a .docx file?
    def test_4_make_docx(self):
        result_f_name = 'result_file_2.docx'
        self.ob.make_docx(self.path, result_f_name, self.combined_text)
        self.assertTrue(result_f_name in self.ob.filter_files(self.path,
                                                              '.*\.docx'))
        os.remove(self.path+'/'+result_f_name)

if __name__ == '__main__':
    unittest.main()
