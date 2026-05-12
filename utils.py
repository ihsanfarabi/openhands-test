import re

_NON_ALPHANUM: re.Pattern[str] = re.compile(r"[^a-z0-9]")


def is_palindrome(s: str) -> bool:
    """Return True if s reads the same forwards and backwards.

    Comparison is case-insensitive and ignores non-alphanumeric characters.
    """
    normalized = _NON_ALPHANUM.sub("", s.lower())
    return normalized == normalized[::-1]
