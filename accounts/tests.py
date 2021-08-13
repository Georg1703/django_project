from django.test import TestCase


class MyFirstTest(TestCase):

    def test_my_first_test(self):
        return False
        self.assertIs(test_my_first_test(), True)
