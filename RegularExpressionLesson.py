import re

# example = '''
# Austin is 16 years old and Oscar is 1 year old.
# Bob is gay, but Dom is bomb.
# '''
#
#
# ages = re.findall(r'\d{1,3}', example)
# names = re.findall(r'[A-Z][a-z]*', example)
# letter = re.findall(r'\w',example)
# print(ages)
# print(names)
# print(letter)


# with open('data.txt','r') as my_file:
#     contents = my_file.read()


# LIST OF COMMANDS
# findall - returns the string
# finditer - returns the index of the string
# [] - specific character/numbers/symbols that are allowed ex. [A-Za-z1-9]
# ? - put after a group of regex that makes it optional
# \d - numbers
# \s - space
# \w - character
# Command + / - comment block of code
# ^ - neglects the following group of characters (anything but THIS) ex. [^b]at
# * - 0+ occurrences
# + - 1+ occurences
# ? - 0 or 1 occurences
# {#} - limits the # of characters/numbers/symbols
# {#,#} - range of numbers (minimum, maximum)
# findall - returns a list of all the groups
# finditer - returns the iteration and word of the matched words
# sub - substitutes the string for the new regular expression
# group - returns the group index (depending on what the user inputted)
# match - search the first word of the string and checks if it is a match
# search - search the entire string for a match
# re.IGNORECASE - ignores uppercase and lowercase when looking for matchesex. pattern = re.compile(r"______", re.IGNORECASE)


# #Warm Up #1: Regex for email
# email = "Austingae@gmAil.com ryanpoop@hotmail.com sarahlee@yahoo.com these are email 12324"
# find_email = re.findall(r"\w*@\w*\.com", email)
# print(find_email)
# #Warm Up #2: Regex for IP Address
# ip_address = "76.169.113.47 21.182.293.23"
# find_ip_address = re.findall(r"\d{2}\.\d{3}\.\d{3}\.\d{2}", ip_address)
# print(find_ip_address)
# Exercise #3: Teacher's name
# teacher_names = "Mr. Rogers, Mr. Poops, Mrs. Julianne, Ms. R, Mr. Telephone"
# pattern = re.compile(r"(Mrs|Ms|Mr)\.\s([A-Z]\w*)")
# matches = pattern.finditer(teacher_names)
# for match in matches:
#     print(match.group(2))
# Exercise #4: Different email addresses
# email2 = '''
# austingae@gmail.com
# austingae@university.edu
# 900015105@fjuhsd.org
# bobnumb@stan-ford.net
# '''
# pattern = re.compile(r"[A-Za-z0-9]+@[A-Za-z0-9-]+\.(com|edu|org|net)")
# matches = pattern.finditer(email2)
# for match in matches:
#     print(match)
#Exercise #5: URL
URL = ''' duhapplebaby Https://www.google.com
https://www.youtube.com
http://www.123movies.com
https://www.nasa.gov
'''
pattern = re.compile(r"http(s)?://(www)?\.(\w+)(\.\w+)", re.IGNORECASE)

# subbed_url = pattern.sub(r"\3\4",URL)
# print(subbed_url)

matches = pattern.search(URL)
print(matches)

# To print out specific words in matches, you need to group those regular expressions and use match.group(index)
# pattern.sub(regular expression (ex. r"\3\4"), string) - substitutes the string with the regular expressions inputted


# '''
# 12/27 Summary:
# 1. I learned about regular expressions.
# 2. I learned about the overviews of how the internet works on Khan Academy.
# 3. Command + / to comment blocks of code
#
# Tomorrow:
# 0. Edit Hangman project. (OK!)
# 1. Finish https://www.youtube.com/watch?v=K8L6KVGG-7o (25.47 minutes in) (OK!)
# 2. Project: Use Python to get an article or website and use regular expressions to scrape data from it.
#
# 12/28 Summary:
#
# Tomorrow:
# '''
