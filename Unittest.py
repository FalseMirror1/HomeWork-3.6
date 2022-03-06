import unittest
from app import *


class MyUnitTest(unittest.TestCase):
    def test_add_new_doc(self):
        self.assertEqual(add_new_doc('232323', 'doc', 'Lenin', '4'), '4')

    def test_delete_doc(self):
        self.assertEqual(delete_doc('10006'), ('10006', True))

    def test_get_doc_owner_name(self):
        self.assertEqual(get_doc_owner_name('2207 876234'), 'Василий Гупкин')