import unittest


class A(unittest.TestCase):

    def setUp(self):
        print("\nSetup for Class A")

    def tearDown(self):
        print("Tear Down for Class A\n")

    def test_A1(self):
        print("Test test_A1")

    def test_A2(self):
        print("Test test_A2")

    def test_A3(self):
        print("Test test_A3")


class B(unittest.TestCase):

    def setUp(self):
        print("\nSetup for Class B")

    def tearDown(self):
        print("Tear Down for Class B\n")

    def test_B1(self):
        print("Test test_B1")

    def test_B2(self):
        print("Test test_B2")

    def test_B3(self):
        print("Test test_B3")


class C(unittest.TestCase):

    def setUp(self):
        print("\nSetup for Class C")

    def tearDown(self):
        print("Tear Down for Class C\n")

    def test_C1(self):
        print("Test test_C1")

    def test_C2(self):
        print("Test test_C2")

    def test_C3(self):
        print("Test test_C3")
