# utils.py — shared utility functions


def validate_email(email: str) -> bool:
    """Return True if email contains exactly one '@' and at least one '.' after the '@'."""
    at_index = email.find('@')
    if at_index == -1:
        return False
    if email.find('@', at_index + 1) != -1:
        return False
    if '.' not in email[at_index + 1:]:
        return False
    return True

