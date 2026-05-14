def get_input():
    num_vars = int(input("Number of variables: "))
    data = {}

    for i in range(num_vars):
        variable = input(f"var[{i + 1}]: ")
        rules = input("rules (space sep): ").split(" ")
        data[variable] = rules
    
    return data
