from collections import defaultdict
import pickle
import shelve

# Accepts multiple pickled files in a list and processes it 
def preprocess(pickled, shelf):
    '''Accepts multiple pickled files in a list and processes it'''
    mapped = defaultdict(set)   #key values of this dict will be of default type, set
    s = shelve.open(shelf)
    
    for pickled_file in pickled:
        f = open(pickled_file, 'br')

        data_list = pickle.load(f)

        for file_path, quotes in data_list:
            words = quotes.split()
            for word in words:
                mapped[word].add(file_path)
                s[word] = mapped[word]
        f.close()
