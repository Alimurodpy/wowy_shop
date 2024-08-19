def integer_only(text) -> str:
    """
    Remove all characters except digits
    ex: +998(91) 333 33 33  ->  99891333333 
    """
    return ''.join([i for i in text if i.isdigit()])

def check_phone(phone):
    phone = integer_only(phone)
    return len(phone) == 13