import calculator


class TestCalculator:

    def test_addition(self):
        assert 4 == calculator.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator.subtract(4, 2)

    def test_multiply(self):
        assert 100 == calculator.multiply(10, 10)

    def test_division(self):
        assert 12 == calculator.division(24, 2)
