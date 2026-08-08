def create_character(name, strength, intelligence, charisma):
    full_dot = "●"
    empty_dot = "○"
    
    # 1. Validate if name is a string
    if not isinstance(name, str):
        return "The character name should be a string"
    
    # 2. Validate if name is not empty
    if name == "":
        return "The character should have a name"
    
    # 3. Validate if name is not longer than 10 characters
    if len(name) > 10:
        return "The character name is too long"
    
    # 4. Validate if name does not contain spaces
    if " " in name:
        return "The character name should not contain spaces"
    
    # 5. Validate if stats are integers
    if not (isinstance(strength, int) and isinstance(intelligence, int) and isinstance(charisma, int)):
        return "All stats should be integers"
    
    # 6. Validate if stats are at least 1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    
    # 7. Validate if stats are at most 4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    
    # 8. Validate if the sum of all stats equals 7
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"
    
    # 9. Format and return the final string output
    str_dots = full_dot * strength + empty_dot * (10 - strength)
    int_dots = full_dot * intelligence + empty_dot * (10 - intelligence)
    cha_dots = full_dot * charisma + empty_dot * (10 - charisma)
    
    return f"{name}\nSTR {str_dots}\nINT {int_dots}\nCHA {cha_dots}"
