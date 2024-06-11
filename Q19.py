punc_string = "Hello, everyone! How are you doing"
import string
without_punc_string = ""
for char in punc_string:
    if char not in string.punctuation:
        without_punc_string +=  char
print(without_punc_string)