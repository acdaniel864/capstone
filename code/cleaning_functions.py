import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cleaning_functions as cf
from unidecode import unidecode

def uniform_strings(x): 
    '''
    Removes accents, removed all non-alphanumeric characters, outputs new string in title case
    '''
    x = unidecode(x).lower()
    output_string = ''
    for char in x: 
        if char.isspace() == True:
            output_string += char
        elif char.isalnum() == True:
            output_string += char
    output_string = re.sub(' +', ' ', output_string)
    return output_string.title().strip()


def remove_varietal(x, varietals):
    '''
    Removes varietal name it finds + year (4 digits) and returns cleaned and capitalised producer name.
    Returns 'review' if no varietal is found.
    '''
    original_x = x  # Store original input for comparison
    x = uniform_strings(x).strip().lower()
    varietals_to_extract = [varietal for varietal in varietals if varietal in x]
    #print(f"All initial varietals: {varietals_to_extract}") 
    count = 0
    for i in range(0, len(varietals_to_extract)):
        for varietal in varietals_to_extract:
            # if year still in the string
                    # if <grape><string><year>
            if re.search(rf'{varietal}\s\w*\s\d{{4}}', x)!= None:
                #print(f"X before resub {count} is: {x}") 
                x = re.sub(rf'{varietal}\s\w*\s\d{{4}}\w*','', x)
                count += 1
                #print(f"String after {count} re subs is: {x}")

            elif re.search(rf'\d{{4}}', x) != None:
                # replace varietal names and years
                #print(f"X before resub {count} is: {x}") 
                x = re.sub(rf'{varietal}\s\d{{4}}\w*', '', x)
                count += 1
                #print(f"String after {count} re subs is: {x}")
            
            else: # replace varietal name only 
                #print(f"X before resub {count} is: {x}") 
                x = re.sub(rf'{varietal}', '', x)
                count += 1
                #print(f"String after {count} re subs is: {x}")
        
    if x == uniform_strings(original_x).strip().lower() or len(varietals_to_extract) == 0:
        # if no changes were made to x
        return 'review' 
    else:
        # return cleaned and capitalised producer name
        return ' '.join(word.title() for word in x.split()).strip()
    
