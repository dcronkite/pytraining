import pytest
import pandas as pd

from example import add_two, convert_sas_date, ShoppingCart


def test_simple():
    assert 1 == 1


def test_fail():
    with pytest.raises(ValueError):
        raise ValueError


@pytest.mark.parametrize(('num', 'exp'), [
    (2, 4),
    (-2, 0)
])
def test_add_two(num, exp):
    result = add_two(2)
    assert result == 4


@pytest.mark.parametrize(('sasdate', 'exp', 'unit'), [
    (1775376002.0, '2016-04-04 08:00:02', 's'),
    (14686, '2000-03-17 00:00:00', 'd')
])
def test_sas_datetime(sasdate, exp, unit):
    df = pd.DataFrame({'sasdate': [sasdate]})
    result = convert_sas_date(df['sasdate'], unit)
    assert str(result.iloc[0]) == exp


def test_cart():
    sc = ShoppingCart(tax_rate=0)
    sc.add_item('bike', 15, 2)
    assert sc.get_cost() == 30
    sc.add_coupon('bike', 3)
    assert sc.get_cost() == 27
    sc.remove_item('bike')
    assert sc.get_cost() == 0
