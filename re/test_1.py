"""
Trying out python regex module
Reference : https://github.com/CoreyMSchafer/code_snippets/blob/master/Python-Regular-Expressions/simple.py
"""

import re


def find_matches(pattern,search_text):
    """find regex objects of corresponding pattern matches"""
    re_matches = [match for match in pattern.finditer(search_text)]
    return re_matches

def print_matches(match_list, search_text):
    """print from a list of regex object"""
    for match_obj in match_list:
        span = match_obj.span()
        print(search_text[span[0]:span[1]])

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# find matches for string with word boundary
pattern = re.compile(r'\bMr') #r''-> raw string
match_obj = find_matches(pattern,text_to_search)

# find matches for specific format
pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') #'.' matches any character
match_obj = find_matches(pattern,text_to_search)

# read data.txt
with open('./re/data.txt','r') as f:
    contents = f.read()

    # search phone numbers
    pattern = re.compile(r'[3-9]\d{2}[-.*]\d{3}[-.*]\d{4}') 
    pattern_not = re.compile(r'[^3-9]\d{2}.\d{3}.\d{4}') 
    match_obj_list = find_matches(pattern, text_to_search)
    print_matches(match_obj_list,text_to_search)

    print('not...')
    match_obj_list = find_matches(pattern_not, text_to_search)
    print_matches(match_obj_list,text_to_search)

    print('names...')

    pattern = re.compile(r'Mr\.?\s[A-Z]\w*')
    match_obj_list = find_matches(pattern, text_to_search)
    print_matches(match_obj_list,text_to_search)

    print('all names...')
    pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
    match_obj_list = find_matches(pattern, text_to_search)
    print_matches(match_obj_list,text_to_search)

    f.close()

emails = """
CoreyMSchafer@gmail.com ....
corey.schafer@university.edu
corey-321-schafer@my-work.net
"""

# [uppercase or lowercase alphabets]match one or more till '@' hits] [uppercase or lowercase alphabets one or more match till .com hits]
pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.com') 
match_obj_list = find_matches(pattern, emails)
print_matches(match_obj_list,emails)

# whole line (needs fix...)
text_to_search_ = text_to_search.split('\n')
pattern = re.compile(r'[a-zA-Z]+@[a-zA-Z]+\.(com|edu|net)')

for text in text_to_search_:
    match_obj = find_matches(pattern,text)
    print_matches(match_obj,text)


urls ='''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)

for match in matches:
    print(match.group(0)) # entire match
    print(match.group(2)) # 2nd option

# sub elements
subbed_urls = pattern.sub(r'\2\3', urls) # sub with group(2) and group(3)
print(subbed_urls)

pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

# find all method (just return matches as list of strings)
print(pattern.findall(text_to_search))

# search method (returns first match)
print(pattern.search(text_to_search))

# flags
sentence = 'Start a sequence and then bring it to an end'
pattern = re.compile(r'start', re.IGNORECASE)
print(pattern.findall(sentence))