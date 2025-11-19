import json
from .utils import mask_card, mask_account, format_date


def load_operations(path: str) -> list:
    """Загрузка операций из JSON-файла."""
    with open(path, "r") as file:
        return json.load(file)


def format_operation(op: dict) -> str:
    """Форматирование одной операции."""
    date = format_date(op["date"])
    description = op["description"]

    # маскировка from
    if "from" in op:
        from_raw = op["from"]
        from_masked = mask_account(from_raw) if from_raw.startswith("Счет") else mask_card(from_raw)
    else:
        from_masked = ""

    # маскировка to
    to_raw = op["to"]
    to_masked = mask_account(to_raw) if to_raw.startswith("Счет") else mask_card(to_raw)

    amount = op["operationAmount"]["amount"]
    currency = op["operationAmount"]["currency"]["name"]

    if from_masked:
        arrow = f"{from_masked} -> {to_masked}"
    else:
        arrow = to_masked

    return f"{date} {description}\n{arrow}\n{amount} {currency}"


def get_last_operations(operations: list, count: int = 5) -> list:
    """Фильтрация и сортировка операций."""
    executed = [op for op in operations if op.get("state") == "EXECUTED"]
    executed.sort(key=lambda x: x["date"], reverse=True)
    return executed[:count]