def validate_month(month):
    """
    Validates if the month is an integer between 1 and 12 inclusive.
    """
    try:
        month_int = int(month)
        return 1 <= month_int <= 12
    except (ValueError, TypeError):
        return False


def validate_usage(usage):
    """
    Validates if the usage is a non-negative number.
    """
    try:
        usage_float = float(usage)
        return usage_float >= 0.0
    except (ValueError, TypeError):
        return False
