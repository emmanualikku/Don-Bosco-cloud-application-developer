x = ("emmanual", "ikku", "me", "daddy", "vava")

def fx(tup):
    if not tup:
        return None

    longest_string = ""

    for string in tup:
        if len(string) > len(longest_string):
            longest_string = string
            
    return longest_string

longest_string = fx(x)
print("The longest string is:", longest_string)
