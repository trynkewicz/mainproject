from .operations import load_operations, get_last_operations, format_operation


def main():
    ops = load_operations("operations.json")
    last_ops = get_last_operations(ops)

    for op in last_ops:
        print(format_operation(op))
        print()


if __name__ == "__main__":
    main()