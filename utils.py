# utils.py — shared utility functions


def validate_email(email: str) -> bool:
    """Validate an email address.

    Returns True if the email contains exactly one '@' and at least one '.'
    after the '@'. Returns False otherwise.
    """
    if email.count('@') != 1:
        return False
    local, _, domain = email.partition('@')
    if '.' not in domain:
        return False
    return True
