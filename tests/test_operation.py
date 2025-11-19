from src.operations import get_last_operations, format_operation


def test_get_last_operations():
    ops = [
        {"state": "EXECUTED", "date": "2020-01-01T00:00:00"},
        {"state": "CANCELED", "date": "2022-01-01T00:00:00"},
        {"state": "EXECUTED", "date": "2021-01-01T00:00:00"},
    ]

    result = get_last_operations(ops)
    assert len(result) == 2
    assert result[0]["date"] == "2021-01-01T00:00:00"


def test_format_operation():
    op = {
        "date": "2019-08-26T10:50:58.294041",
        "description": "Перевод",
        "from": "Счет 123456789",
        "to": "Счет 987654321",
        "operationAmount": {"amount": "100", "currency": {"name": "руб."}}
    }

    text = format_operation(op)
    assert "26.08.2019" in text
    assert "**6789" in text