'''
structures.py

Simple functions performing operations on basic Python data structures.  
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list". 
def first_and_last(the_list):
    '''gives the first and last value in the list'''
    return [the_list[0], the_list[-1]]
'''print (first_and_last([0,1,2,3,4,5,6]))'''


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list". 
# If "end" is greater then "beginning" or any og the indices is out of the
# list, raise a "ValueError" exception. 
def part_reverse(the_list, beginning, end):
    '''give the reverse of the list between the beginning and the end'''
    try:
        new_list=the_list[beginning:end]
        new_list.reverse()
    except:
        raise ValueError
    return new_list# hint this is incomplete
'''
print (part_reverse([0,1,2,3,4,5,6],5,2))'''

# write a function that at the "index" of "the_list" inserts three times the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4]. 
def repeat_at_index(the_list, index):
    '''repeats the value at index in the list 3 times'''
    the_list.insert(index,the_list[index])
    the_list.insert(index,the_list[index])
    return the_list
'''
print (repeat_at_index([0,1,2,3,4,5,6],4))'''

# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    '''checks if a word is a palindrome'''
    word=word.lower()
    word=list(word)
    status = word==word[::-1]
    return status

'''print (palindrome_word('Madam'))'''

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not. 
def palindrome_sentence(sentence):
    '''check if a sentence is a palindrome'''
    import string
    sentence=sentence.translate(str.maketrans(dict.fromkeys(string.punctuation)))
    sentence=sentence.lower()
    sentence=sentence.replace(" ", "")
    sentence=list(sentence)
    status=sentence==sentence[::-1]
    return status
'''print (palindrome_word("Was it a car or a cat I saw"))'''

# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence.
def concatenate_sentences(sentence1, sentence2):
    '''put 2 sentences together'''
    import string
    sentence1=sentence1.strip()
    sentence2=sentence2.strip()
    status = sentence1[0].isupper()
    status = sentence2[0].isupper()
    status = sentence1[-1] in string.punctuation
    status = sentence2[-1] in string.punctuation
    while status:
        full = ''.join(sentence1)+' '+''.join(sentence2)
        return full
        break
'''print(concatenate_sentences("First sentence.", "Second sentence."))'''


# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    '''check if key exists in dictionary'''
    if key in dictionary:
        status = True
    else:
        status = False
    return status

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    '''check if value exists in dictionary'''
    if value in dictionary.values():
        status = True
    else:
        status = False
    return status

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    '''merges 2 dictionaries together'''
    newdict = dictionary1.copy()
    newdict.update(dictionary2)
    return newdict
