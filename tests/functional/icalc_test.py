import icalc
from unittest.mock import patch
from icalc import InteractiveCalculator


class TestIcalcsm:

    ic = InteractiveCalculator()

    @patch('builtins.print')
    def test_do_add(self, mock_print):
        self.ic.do_add("2 3")
        mock_print.assert_called_with(5)

    @patch('builtins.print')
    def test_do_sub(self, mock_print):
        self.ic.do_sub("2 3")
        mock_print.assert_called_with(-1)

    @patch('builtins.print')
    def test_do_mul(self, mock_print):
        self.ic.do_mul("2 3")
        mock_print.assert_called_with(6)

    @patch('builtins.print')
    def test_do_div(self, mock_print):
        self.ic.do_div("8 4")
        mock_print.assert_called_with(2)

    @patch('builtins.print')
    def test_do_rem(self, mock_print):
        self.ic.do_rem("10 6")
        mock_print.assert_called_with(4)

    @patch('builtins.print')
    def test_do_sqrt(self, mock_print):
        self.ic.do_sqrt("16")
        mock_print.assert_called_with(4)

    @patch('builtins.print')
    def test_do_bit_and(self, mock_print):
        self.ic.do_bit_and("5 4")
        mock_print.assert_called_with(4)

    @patch('builtins.print')
    def test_do_bit_or(self, mock_print):
        self.ic.do_bit_or("6 9")
        mock_print.assert_called_with(15)

    @patch('builtins.print')
    def test_do_bit_xor(self, mock_print):
        self.ic.do_bit_xor("9 11")
        mock_print.assert_called_with(2)

    @patch('builtins.print')
    def test_do_bit_not(self, mock_print):
        self.ic.do_bit_not("11")
        mock_print.assert_called_with(-12)

    @patch('builtins.print')
    def test_do_shift_left(self, mock_print):
        self.ic.do_bit_shift_left("5 3")
        mock_print.assert_called_with(40)

    @patch('builtins.print')
    def test_do_shift_right(self, mock_print):
        self.ic.do_bit_shift_right("10 3")
        mock_print.assert_called_with(1)

    def test_zero_division(self):
        try:
            self.ic.do_div("5 0")
        except ZeroDivisionError as exc:
            assert False, "Exception not handled {}".format(exc)

    def test_zero_modulo(self):
        try:
            self.ic.do_rem("5 0")
        except ZeroDivisionError as exc:
            assert False, "Exception not handled {}".format(exc)

    def test_invalid_input(self):
        try:
            icalc.parse("add a 3")
        except ValueError as exc:
            assert False, "Exception not handled: {}".format(exc)
