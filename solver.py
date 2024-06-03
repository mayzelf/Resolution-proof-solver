import re

def remove_lit_and_neg_lit(input_string):
    # Remove curly braces and split string by commas
    input_string = input_string.strip('{}')
    literals = input_string.split(',')
    
    # Initialize sets to store positive and negative literals
    positive_literals = set()
    negative_literals = set()
    
    # Separate positive and negative literals
    for literal in literals:
        literal = literal.strip()
        if literal.startswith('!'):
            negative_literals.add(literal[1:])
        else:
            positive_literals.add(literal)
    
    # Find pairs and remove them (x, !x)
    contradictions = positive_literals.intersection(negative_literals)
    simplified_literals = {f'!{literal}' for literal in negative_literals if literal not in contradictions}
    simplified_literals.update({literal for literal in positive_literals if literal not in contradictions})
    
    # Convert set back to string format
    result = '{' + ','.join(sorted(simplified_literals)) + '}'
    
    return result

def remove_duplicates(s):
    # split string into list of literals
    literals = s[1:-1].split(',')
    
    seen = set()
    unique_literals = []
    for literal in literals:
        if literal not in seen:
            unique_literals.append(literal)
            seen.add(literal)
    
    # Convert list of literals back to string
    result = "{" + ",".join(unique_literals) + "}"
    
    return result

# regular expression pattern
pattern = r"\(!*\w(?:\s+or\s+!*\w)*\)(?:\s*and\s*\(!*\w(?:\s+or\s+!*\w)*\))*"

while True:
    user_input = input("Enter a string: ")

    # Check if string matches pattern
    if re.fullmatch(pattern, user_input):
        print("The string is in the correct format.")
        break
    else:
        print("The string is not in the correct format. Please try again.")

# Split string at "and"
split_strings = user_input.split("and")
for string in split_strings:
    #print(string.strip())

    # Replace brackets
    split_strings = [string.replace("(", "{").replace(")", "}") for string in split_strings]

    # Replace "or"
    split_strings = [string.replace("or", ",") for string in split_strings]

    # Remove spaces
    split_strings = [string.replace(" ", "") for string in split_strings]

    # Remove double negations
    split_strings = [string.replace("!!", "") for string in split_strings]

for string in split_strings:
    print(string)
   

class BreakIt(Exception): pass

try:
    for string1 in split_strings:
        for string2 in split_strings:
            if string1 != string2:
                # Split each string into a list of literals
                literals1 = string1[1:-1].split(',')
                literals2 = string2[1:-1].split(',')
                count = 0
                for literal1 in literals1:
                    if f"!{literal1}" in literals2:
                        count += 1
                for literal2 in literals2:
                    if f"!{literal2}" in literals1:
                        count += 1

                #print(f"{string1} and {string2} => {count}")
                if count == 1:
                    # Merge literals
                    merged_literals = literals1 + literals2

                    # Convert list of literals back to string
                    merged = "{" + ",".join(merged_literals) + "}"

                    merged = remove_duplicates(merged)

                    #print(f"{string1} and {string2} merged to => {merged}")

                    merged = remove_lit_and_neg_lit(merged)

                    print(f"{string1} and {string2} => {merged}")

                    if merged not in split_strings:
                        split_strings.append(merged)

                    if merged == '{}':
                        raise BreakIt
except BreakIt:
    pass
