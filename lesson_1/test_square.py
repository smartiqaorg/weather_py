from square import square
import pytest


class TestSquare:

    # ---- Fixtures -----
    def setup(self):
        print('Setup method...')

    def teardown(self):
        print('Teardown method')

    def setup_class(self):
        print('Setup class')

    def teardown_class(self):
        print('Teardown class')

    # ------ Tests ------
    def test_type_error(self):
        with pytest.raises(TypeError):
            square('str')

    def test_zero(self):
        assert(square(0) == [])

    def test_one(self):
        assert(square(1) == [0])

    def test_two(self):
        assert(square(2) == [0, 1])

    def test_ten(self):
        assert(square(10) == [0, 1, 4, 9, 16, 25, 36, 49, 64, 81])

    def test_value_error(self):
        with pytest.raises(ValueError):
            square (-1)

    def test_five(self):
        assert (square(5) == [0, 1, 4, 9, 16])

    @pytest.mark.skip
    def test_failed(self):
        assert (square(3) == 24)

    @pytest.mark.parametrize("num", [1, 5, 10, 15])
    def test_length(self, num):
        print(f'Running parametrized test for num={num}...')
        assert(len(square(num)) == num)
        print('Parametrized test finished')
