from input import get_input
from validation import validate
from processing import cfg_to_pda
from display import display

data = get_input()

is_valid, message = validate(data)
if is_valid:
    print(message)
    display(cfg_to_pda(data))
else:
    print(message)
