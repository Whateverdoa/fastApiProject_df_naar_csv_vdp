from calculations.calculations import amount_with_percentage


def test_percentage():
    aantal = 100
    percentage = 10
    test = amount_with_percentage(aantal, percentage)
    result = 110
    assert test == result
