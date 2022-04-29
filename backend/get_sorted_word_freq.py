from collections import defaultdict
import re

# Returns a dictionary of words in str mapping to their number of occurrences in descending order
def getSortedWordFrequency(str):
    wordToCount = defaultdict(int)  # maps each word in str to its number of occurences
    countToWords = defaultdict(set) # maps each occurence number to the set of words in str with that number of occurrences

    # Remove all punctuation marks and leaves only word chars, spaces, and hyphens with regex
    cleanedStr = re.sub(r'[^\w\s\-]', '', str) 

    # Iterate through each word in str
    # Note: Hyphenated words such as "ten-year-old" are considered to be 1 word
    for word in cleanedStr.split():
        # If first occurence of word, add it to the set of words corresponding to occurence number of 1
        if word not in wordToCount:
            countToWords[1].add(word)

        # Else move the word to the set that corresponds to an occurence count that's 1 greater
        else:
            prev_count = wordToCount[word]
            countToWords[prev_count].remove(word)
            countToWords[prev_count+1].add(word)
        
        wordToCount[word] += 1

    result = dict()
    # countToWords' keys are already sorted in incrementing order b/c
    # standard dict type maintains insertion order by default
    for count in reversed(list(countToWords.keys())):
        for word in countToWords[count]:
            result[word] = count

    return result
    
if __name__ == '__main__':
    inputs = ['hello', 'hi there!', 'this is a test of the emergency broadcast system. this is only a test dog dog dog']
    # inputs = ['hello!', 'my, name. is, chill-cdc. my name is linh']
    for i in inputs:
        print(getSortedWordFrequency(i))
        print()
