import re


def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards.

    Comparison is case-insensitive and ignores non-alphanumeric characters.
    """
    normalized = re.sub(r"[^a-z0-9]", "", s.lower())
    return normalized == normalized[::-1]
