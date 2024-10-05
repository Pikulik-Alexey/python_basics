# Юнит тесты
import calculator_logic as c


def test_add():
    assert c.add(10, 5) == 15
    assert c.add(-1, 1) == 0
    assert c.add(-2, -2) == -4


def test_subtract():
    assert c.subtract(10, 5) == 5
    assert c.subtract(-1, 1) == -2
    assert c.subtract(-10, -10) == 0


def test_multiplication():
    assert c.multiplication(10, 5) == 50
    assert c.multiplication(-1, 1) == -1
    assert c.multiplication(-2, -2) == 4


def test_division():
    assert c.division(10, 5) == 2
    assert c.division(-1, 1) == -1
    assert c.division(-2, -2) == 1


test_add()
test_subtract()
test_multiplication()
test_division()
print('Тесты пройдены успешно')
