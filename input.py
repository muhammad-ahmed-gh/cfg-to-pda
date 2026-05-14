def get_input():
    # 1. Get Variables (V)
    v_input = input("Enter Variables separated by spaces (e.g., S A B): ").upper()
    variables = v_input.split()

    # 2. Get Terminals (Sigma)
    # Updated instructions to mention 'e'
    t_input = input("Enter Terminals separated by spaces (use 'e' for epsilon, e.g., a b 0 1 e): ")
    # Automatically convert 'e' to 'epsilon' in the terminals list
    terminals = ['epsilon' if t == 'e' else t for t in t_input.split()]

    # 3. Get Start Variable (S)
    start_variable = input("Enter the Start Variable: ").strip()

    # 4. Get Productions (R)
    print("\nEnter production rules.")
    print("Format: Variable -> derivation1 | derivation2")
    # Updated instructions to show 'e' instead of 'epsilon'
    print("Use spaces between symbols and 'e' for epsilon (e.g., S -> a S b | e).") 
    print("Type 'done' when finished.")

    # Initialize the dictionary to hold productions for each variable
    productions = {}
    for var in variables:
        productions[var] = []

    # Loop to collect all production rules
    while True:
        rule_input = input("> ").strip()
        
        if rule_input.lower() == 'done':
            break
            
        if '->' in rule_input:
            # Split into left-hand side and right-hand side
            left_side, right_side = rule_input.split('->', 1)
            left_side = left_side.strip()
            
            if left_side in variables:
                # Split multiple derivations by '|'
                derivations = right_side.split('|')
                
                for derivation in derivations:
                    # Split each derivation into individual symbols
                    symbols = derivation.split()
                    
                    # --- NEW LOGIC: Convert 'e' to 'epsilon' ---
                    symbols = ['epsilon' if sym == 'e' else sym for sym in symbols]
                    
                    if symbols:
                        productions[left_side].append(symbols)
            else:
                print(f"Error: {left_side} is not in your Variables list.")
        else:
            print("Invalid format. Use '->'.")

    # Bundle everything into a dictionary to return as 'data'
    cfg_data = {
        'variables': variables,
        'terminals': terminals,
        'start_variable': start_variable,
        'productions': productions
    }
    
    return cfg_data