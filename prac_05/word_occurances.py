"""
Word Occurrences
Estimate: 60 minutes
Actual:    minutes

Write a program to count the occurrences of words in a string. The program should ask the user for a string, then print
the counts of how many of each word are in the string.
"""

text = "this is a collection of words of nice words this is a fun thing it is"
text = list(text.split(" "))    # turn text into a list
word_to_count = {}      # set up dictionary
for word in text:       # for each word in the list text
    word_to_count[word] = word_to_count.get(word, 0) + 1    # return a value for key (list), if no key set to 0, add 1
for word, count in word_to_count.items():   # set up variables for dictionary {"word": int(count)) in "for" loop
    print(f"{word}: {int(count)}")       # print out each loop
