def longest(sentence):
    words=sentence.split()
    max_len=0
    longest=''
    for word in words:
        if len(word) >max_len:
            max_len=len(word)
            longest=word
    return longest

output=longest("my first week at chiefNet")
print(output)