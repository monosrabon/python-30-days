# Optional helpers for formatting results

def format_results(results):
    """
    Takes a list of rolled dice results and returns a formatted string.
    Example: [3, 5] -> "You rolled: 3, 5 (Total: 8)"
    """
    total = sum(results)
    result_str = ", ".join(map(str, results))
    return f"You rolled: {result_str} (Total: {total})"
