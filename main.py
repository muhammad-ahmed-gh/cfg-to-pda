from input import get_input
from validation import validate
from processing import cfg_to_pda
from display import display

data = get_input()

if validate(data):
    display(cfg_to_pda(data))
else:    
    print("Invalid CFG. Please check your input and try again.")
