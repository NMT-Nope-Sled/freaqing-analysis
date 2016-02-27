# Author: Riley Myers <wmyers559@users.noreply.github.com>

import re

def sanitize_input(text, strip=True, lower=True):
    """
    Sanitize plaintext input - lowercase it and remove spaces - in preparation
    for frequency analysis
    """
    tmp = text[0:]

    if strip:
        tmp = re.sub(r'\s+', '', tmp)
        #tmp.translate(tmp.maketrans({None))
    
    if lower:
        tmp = tmp.lower()

    return tmp


print(sanitize_input("He llo           World      "))
