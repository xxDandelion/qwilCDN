import unittest


class TestSanity(unittest.TestCase):

        @classmethod
        def setUpClass(cls) -> None:
            """ this runs before all tests in this file. """


        @classmethod
        def tearDownClass(cls) -> None:
            """" this runs after all tests in this file. """


        def setUp(self):
            """ Setup for every test method. """



        def tearDown(self) -> None:
            """ Teardown for every test method. """



        def test_1(self) -> None:
            """ Test checks if given string is in titled case """

            print('calling test_is_title')



        def test_2(self) -> None:
            """ Test checks if string is in lower case """

            print('calling test_is_lower')



        def test_3(self) -> None:
            """ Test checks if string is in upper case """

            print('calling test_is_upper')




