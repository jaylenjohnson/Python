from datetime import datetime
from functools import wraps
import shelve

#Decorator prints the execution time of the applied function(s)
def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        dt1 = datetime.now()
        output = func(*args, **kwargs)
        dt2 = datetime.now()
        print("Execution time:", dt2.microsecond-dt1.microsecond)
        return output
    return wrapper

# Determines the boolean type and returns all the keywords entered by user
def detect_query_type(query):
    '''Determines the boolean type and returns all the keywords entered by user'''

    qtype = 'and'   #default query type

    query = query.lower()

    and_in_there = ' and ' in query
    or_in_there = ' or ' in query

    #set qtype to 'or' if that is present and the only query
    if or_in_there and not and_in_there:
        qtype = 'or'

    #remove duplicate words
    keywords = set(query.split())

    if and_in_there:
        keywords.remove('and')

    if or_in_there:
        keywords.remove('or')

    return qtype, keywords

# Performs search 
@time_execution
def search(shelf, qtype, keywords):
    s = shelve.open(shelf)

    print("Performing {} search for {}".format(qtype.upper(), keywords))

    for i,word in enumerate(keywords):
        if i == 0:
            try:
                output = s[word]
            except KeyError:
                output = set()
        else:
            if word in s:
                if qtype == 'and':
                    output = output.intersection(s[word])
                elif qtype == 'or':
                    output = output.union(s[word])

    output = list(output)
    output.sort()

    return output
    #for found in output:
    #    print("Found at ", found, ': ' + data_list[found])