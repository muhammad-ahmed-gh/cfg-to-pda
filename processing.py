import json

''' example
cfg format
{
    "S": ["aTb", "b"],
    "T": ["Tb", "e"],
}

{
    "q0": [
        {"to": "q1", "text", ["e,e,$"]}
    ],
    "q1": [
        {"to": "q2", "text", ["e,e,S"]}
    ],
    "q2": [
        {"to": "q2", "text", ["e,S,b", "e,T,e", "a,a,e", "b,b,e"]},
        {"to": "q3", "text", ["e,S,b"]},
        {"to": "q5", "text", ["e,T,b"]},
        {"to": "q6", "text", ["e,$,e"]}
    ],
    "q3": [
        {"to": "q4", "text": ["e,e,T"]}
    ],
    "q4": [
        {"to": "q2", "text": ["e,e,a"]}
    ],
    "q5": [
        {"to": "q2", "text": ["e,e,T"]}
    ],
    "q6": []
}
'''

def cfg_to_pda(cfg):
    initial_state = list(cfg.keys())[0]
    num_states = 3
    terminals = set()
    result = {
        "q0": [
            {"to": "q1", "text": ["e,e,$"]}
        ],
        "q1": [
            {"to": "q2", "text": [f"e,e,{initial_state}"]}
        ],
        "q2": []
    }


    def new_state():
        nonlocal num_states
        num_states += 1
        return f"q{num_states - 1}"

    def add_transition(src, to, text):
        if src not in result:
            result[src] = [{"to": to, "text": [text]}]
        else:
            for transition in result[src]:
                if transition["to"] == to:
                    transition["text"].append(text)
                    return
            result[src].append({"to": to, "text": [text]})

    def add_terminals_transitions():
        for term in terminals:
            if term == "e":
                continue
            transition = f"{term},{term},e"
            add_transition(src="q2", to="q2", text=transition)

    def add_accept_state():
        add_transition("q2", new_state(), f"e,$,e")
        result[f"q{num_states - 1}"] = []

    def build_pda():
        for state in list(cfg.keys()):
            rules = cfg[state]
            for rule in rules:
                if len(rule) == 1:
                    transition = f"e,{state},{rule}"
                    add_transition(src="q2", to="q2", text=transition)

                    if(rule.islower()):
                        terminals.add(rule)
                else:
                    first_transition = f"e,{state},{rule[-1]}"
                    add_transition("q2", new_state(), first_transition)

                    for i in range(-2, -1 * len(rule), -1):
                        transition = f"e,e,{rule[i]}"
                        add_transition(f"q{num_states - 1}", new_state(), transition)

                    last_transition = f"e,e,{rule[0]}"
                    add_transition(src=f"q{num_states - 1}", to="q2", text=last_transition)

                    for c in rule:
                        if c.islower():
                            terminals.add(c)


    build_pda()
    add_terminals_transitions()
    add_accept_state()
    return result

# test_case1 = {
#     "S": ["aTb", "b"],
#     "T": ["Tb", "e"],
# }

# test_case2 = {
#     "S": ["AB"],
#     "A": ["aAb", "e"],
#     "B": ["cB", "e"]
# }

# print(json.dumps(
#     cfg_to_pda(test_case2),
#     indent=2
# ))