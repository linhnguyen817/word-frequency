from collections import defaultdict

def get_word_freq(data):
    word_freq = defaultdict(int)
    for k in data.split():
        word_freq[k] += 1
    return word_freq

if __name__ == '__main__':
    inputs = ['hello', 'hi there!', 'this is a test of the emergency broadcast system this is only a test dog dog dog']
    for i in inputs:
        print(get_word_freq(i))




        