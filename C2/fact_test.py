class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        with self.subTest(i=1):
            self.assertRaises(TypeError, factorize, "string")
        with self.subTest(i=2):
            self.assertRaises(TypeError, factorize, 1.5)

    def test_negative(self):
        for x in -1, -10, -100:
            with self.subTest(x=x):
                with self.assertRaises(ValueError):
                    factorize(x)

    def test_zero_and_one_cases(self):
        with self.subTest(i=0):
            self.assertEqual((0,), factorize(0))

        with self.subTest(i=1):
            self.assertEqual((1,), factorize(1))

    def test_simple_numbers(self):
        for i, n in (1, 3), (2, 13), (3, 29):
            with self.subTest(i=i):
                self.assertEqual((n,), factorize(n))

    def test_two_simple_multipliers(self):
        with self.subTest(i=1):
            self.assertEqual((2, 3), factorize(6))

        with self.subTest(i=2):
            self.assertEqual((2, 13), factorize(26))

        with self.subTest(i=3):
            self.assertEqual((11, 11), factorize(121))

    def test_many_multipliers(self):
        with self.subTest(i=1):
            self.assertEqual((7, 11, 13), factorize(1001))

        with self.subTest(i=2):
            self.assertEqual((2, 3, 5, 7, 11, 13, 17, 19), factorize(9699690))