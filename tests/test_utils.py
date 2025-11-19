from src.utils import mask_card, mask_account, format_date


def test_mask_card():
    assert mask_card("Visa 1234567890123456") == "Visa 1234 56** **** 3456"


def test_mask_account():
    assert mask_account("Счет 123456789") == "Счет **6789"


def test_format_date():
    assert format_date("2019-01-01T12:00:00.000000") == "01.01.2019"