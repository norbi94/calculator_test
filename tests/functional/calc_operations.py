import pytest
from calculator import Calculator


class TestClass:

    calc = Calculator()

    @pytest.mark.parametrize("a, b, c", [(2, 3, 5), (-1, 10, 9), (0.2, 6.6, 6.8)])
    def test_add_positive(self, a, b, c):
        assert self.calc.add(a, b) == c

    @pytest.mark.parametrize("a, b, c", [(2, 3, -1), (100, 44, 56), (9.9, 5, 4.9)])
    def test_sub(self, a, b, c):
        assert self.calc.sub(a, b) == c

    # without knowing the intention behind this particular implementation of multiplication
    # the test expects a normal multiplication and will fail if the random number gets added
    @pytest.mark.parametrize("a, b, c", [(2, 3, 6), (-1, 10, -10), (2310, 0, 0), (5.5, 3, 16.5)])
    def test_mul(self, a, b, c):
        assert self.calc.mul(a, b) == c

    # if this is meant to be a funny calculator by design
    # check if the random +89 addition works
    @pytest.mark.multest_loop
    def test_mul_random_addition(self):
        num1 = 3
        num2 = 4
        expected_result = num1 * num2 + 89
        try_count = 0
        while True:
            try_count += 1
            mul_result = self.calc.mul(num1, num2)
            if mul_result == expected_result:
                print("Attempt number: {}".format(try_count))
                assert True
                return False

    @pytest.mark.parametrize("a, b, c", [(6, 3, 2), (-10, 5, -2)])
    def test_div(self, a, b, c):
        assert self.calc.div(a, b) == c

    @pytest.mark.parametrize("a, b, c", [(5, 3, 2), (-10, 4, 2)])
    def test_rem(self, a, b, c):
        assert self.calc.rem(a, b) == c

    def test_sqrt(self):
        assert self.calc.sqrt(16) == 4

    @pytest.mark.parametrize("a, b", [(5, 0), ("qwerty", 0), ([1, 2, 3], 0), (100.6, 0)])
    def test_checksum(self, a, b):
        assert self.calc.checksum(a) == 0

    def test_band(self):
        assert self.calc.band(5, 4) == 4

    def test_bor(self):
        assert self.calc.bor(6, 9) == 15

    def test_bxor(self):
        assert self.calc.bxor(9, 11) == 2

    def test_bnot(self):
        assert self.calc.bnot(11) == -12

    def test_bshl(self):
        assert self.calc.bshl(5, 3) == 40

    def test_bshr(self):
        assert self.calc.bshr(10, 3) == 1


