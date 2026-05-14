def validate(data):
    # 1. Check if the dictionary is empty
    if not data:
        return False, "Validation Error: No variables were defined."

    # 2. Identify the Start Variable (the first key entered)
    variables = list(data.keys())
    start_var = variables[0]
    
    # 3. Validate each rule
    for var, rules in data.items():
        for rule in rules:
            # Skip empty rules or explicit epsilon
            if not rule or rule.lower() == 'epsilon':
                continue
            
            # Check every character in the rule string
            for char in rule:
                # If the character is not a defined variable and not lowercase/digit (terminal)
                # This is a basic check to ensure you didn't typo a Variable name
                if char.isupper() and char not in data:
                    return False, f"Validation Error: Variable '{char}' used in rule '{var}->{rule}' is not defined."

    return True, f"Valid CFG. Start Variable is '{start_var}'."