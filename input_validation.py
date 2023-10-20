import re  # regular Expressions
import string


def is_valid_email(email: str) -> bool:
    """
    Uses regular expression to validate email.

    Returns:
    True -- email is valid 
    False -- email is not valid
    """
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None


'''
langes passwort:
min 25 zeichen
mindestens groß und klein schreibung

kurzes passwort:
mindestens 8 zeichen
groß und klein schreibung
sonderzeichen
zahlen


'''


def is_valid_password(pwd: str):
    upper = None
    lower = None
    sonderzeichen = None
    zahl = None
    if len(pwd) >= 25:
        for _ in pwd:
            if _.isupper():
                upper = True
            elif _.islower():
                lower = True
        if upper is True and lower is True and len(pwd) >= 25:
            return True
        else:
            return False

    else:
        for _ in pwd:
            if _.isnumeric():
                zahl = True
            elif _.isupper():
                upper = True
            elif _ in string.punctuation:
                sonderzeichen = True
            elif _.islower():
                lower = True
        if upper is True and lower is True and sonderzeichen is True and zahl is True:
            return True
        else:
            return False


#is_valid_password("Test123!")
