from datetime import datetime


def mask_card(card: str) -> str:
    name, number = card.rsplit(" ", 1)
    first6 = number[:6]
    last4 = number[-4:]
    return f"{name} {first6[:4]} {first6[4:]}** **** {last4}"


def mask_account(account: str) -> str:
    name, number = account.split()
    return f"{name} **{number[-4:]}"


def format_date(date_str: str) -> str:
    return datetime.fromisoformat(date_str).strftime("%d.%m.%Y")