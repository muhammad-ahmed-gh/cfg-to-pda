
from graphviz import Digraph


def display(data):
      # 1. Initialize the graph
    dot = Digraph(comment='Pushdown Automaton', format='png', strict=True)
    
    # 2. Add these specific attributes
    dot.attr(rankdir='LR')
    dot.attr(concentrate='true') # Merges arrows going to the same place
    dot.attr(nodesep='1.0')      # Adds space between states
    dot.attr(margin='0.5')       # Adds a buffer around the edge of the image
    
    for state, transitions in data.items():
        if not transitions:
            dot.node(state, shape='doublecircle')
        else:
            dot.node(state, shape='circle')
    first_state = list(data.keys())[0]
    dot.node('start', label='', shape='none', width='0')
    dot.edge('start', first_state)

    for from_state, transitions in data.items():
        for trans in transitions:
            to_state = trans["to"]
            formatted_labels = []
            for label_str in trans["text"]:
                clean_label = label_str.replace('e', 'ε').replace(',', ', ')                
                parts = clean_label.rsplit(', ', 1)
                if len(parts) == 2:
                    formatted_labels.append(f"{parts[0]} → {parts[1]}")
                else:
                    formatted_labels.append(clean_label)

            final_label = "\n".join(formatted_labels)
            dot.edge(from_state, to_state, label=final_label)

    dot.render(view=True, cleanup=True)