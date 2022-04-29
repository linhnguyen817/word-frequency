from collections import defaultdict

def getSortedWordFrequency(str):
    wordToCount = defaultdict(int)
    countToWords = defaultdict(set)

    for word in str.split():
        if word not in wordToCount:
            wordToCount[word] += 1
            countToWords[1].add(word)
        else:
            prev_count = wordToCount[word]
            wordToCount[word] += 1
            countToWords[prev_count].remove(word)
            countToWords[prev_count+1].add(word)

    # countToWords' keys are already sorted in incrementing order b/c
    # standard dict type maintains insertion order by default
    for count in reversed(list(countToWords.keys())):
        for word in countToWords[count]:
            print(word, count)
    
if __name__ == '__main__':
    inputs = ['hello', 'hi there!', 'this is a test of the emergency broadcast system this is only a test dog dog dog']
    for i in inputs:
        getSortedWordFrequency(i)
        print()
