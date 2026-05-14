def get_input():
    # 1. Get Variables (V)
    v_input = input("Enter Variables separated by spaces (e.g., S A B): ").upper()  
    variables = v_input.split()  # Split the input string into a list of variables

    # 2. Get Terminals (Sigma)
    t_input = input("Enter Terminals separated by spaces (e.g., a b 0 1): ")
    terminals = t_input.split()

    # 3. Get Start Variable (S)
    start_variable = input("Enter the Start Variable: ").strip() 

    # 4. Get Productions (R)
    print("\nEnter production rules.")
    print("Format: Variable -> derivation1 | derivation2")
    print("Use spaces between symbols (e.g., S -> a S b | epsilon).")
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