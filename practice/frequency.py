def frequency(words):
    new_freq={}
    for char in words:
        if char in new_freq:
            new_freq[char] +=1
        else:
            new_freq[char] =1
    return new_freq
output=frequency("this is yugesh from salem")
print(output)