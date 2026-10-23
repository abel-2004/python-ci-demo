from app.calculator import add, divide


def run() -> None:
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 / 4 = {divide(10, 4)}")


if __name__ == "__main__":
    run()
