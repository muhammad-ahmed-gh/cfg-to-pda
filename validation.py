def validate(data):
    """
    Validates the consistency of the provided CFG data.
    Returns (True, None) if valid, or (False, error_message) if invalid.
    """
    variables = set(data['variables'])
    terminals = set(data['terminals'])
    start_var = data['start_variable']
    productions = data['productions']

    # 1. Check if Start Variable is valid
    if start_var not in variables:
        return False, f"Validation Error: Start variable '{start_var}' is not in the list of variables."

    # 2. Check if all variables have production entries (even if empty)
    for var in variables:
        if var not in productions:
            return False, f"Validation Error: Variable '{var}' has no defined production rules."

    # 3. Check every symbol in every production rule
    for var, rules in productions.items():
        for rule in rules:
            for symbol in rule:
                # Check if symbol is a terminal, a variable, or 'epsilon'
                if symbol not in variables and symbol not in terminals and symbol.lower() != 'epsilon':
                    return False, f"Validation Error: Symbol '{symbol}' in {var} -> {' '.join(rule)} is undefined."

    return True, "CFG is valid and ready for conversion."