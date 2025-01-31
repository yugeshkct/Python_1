def non_repeating(s):
    count = {}
    for char in s:
        count[char] = count.get(char,0)+1
    for char in s:
            return char
    return None

print(non_repeating("madam"))
