def format_result(operation: str, a: float, b: float, result: float) -> str:
    return f"{a} {operation} {b} = {result}"


def validate_input(value) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        raise ValueError(f"Invalid input: {value}")
