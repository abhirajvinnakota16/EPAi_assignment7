import subprocess
import sys
import pytest
import code7
from code7 import *
import time
import os.path
import re
import inspect 
import random


README_CONTENT_CHECK_FOR = [
    'fib()',
    'two_one()',
    'two_two()',
    'two_three()',
    'two_four()',
    'two_five()',
    'word_search()',
    'four_one()',
    'four_two()',
    'four_three()',
    'num_plate_ka()',
    'num_plate()',
]

# Basic Functions 

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 10, "Make your README.md file interesting! Add atleast 500 words"


def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"


def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(code7, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


# Individual function tests
def test_fib():
    assert fib([1,2,3,4,5,6,7,8,9,10]) == [1, 2, 3, 5, 8], "Improper fibonnacci function"

def test_two_one():
    l1 = [0,1,2,3,4]
    l2 = [10,11,12,13,14]
    assert two_one(l1,l2) == [11, 13, 13, 15, 15, 17], "Improper odd/even (two_one) function"

def test_two_two():
    assert two_two('TSAI') == ['t', 's'], "Improper vowel (two_two) function"

def test_two_three():
    nums100 = [random.randint(-100,100) for i in range(100)]
    assert len(two_three(nums100)) == 100 , "Improper relu (two_three) function"

def test_two_four():
    nums100 = [random.randint(-100,100) for i in range(100)]
    assert len(two_four(nums100)) == 100 , "Improper sigmoid (two_four) function"

def test_two_five():
    assert two_five('tsai') == ['y', 'x', 'f', 'n'], "Improper character shift (two_five) function"


def test_word_search():
    text = "A quote from a co-worker of mine as we were driving through Oakland California one day \
            looking at a “Hood Rat” with his gold bling around his neck and in his mouth….Look at that STUPID \
            MotherFucker  .. He’s so Effing STUPID he doesn’t Effing know how Effing STUPID HE LOOKS that EFFING \
            DUMB MFer! This particular co-worker was of a melanin heavy constituency himself….I about wrecked \
            the company truck laughing as I told him he probably made the Guinness book on the highest \
            amount of explicatives used in a single sentance by a person"
    assert word_search(text) == ['motherfucker'], "Improper word search function"


def test_four_one():
    l =[1,2,3,4,5,6,7,8,9,10]
    assert four_one(l) == 30, 'Improper reduce (four_one) function'

def test_four_two():
    list_ascii = 'abcdefghijklmnopqrstuvwxyz'
    assert four_two(list_ascii) == 'z', 'Improper reduce (four_two) function'


def test_four_three():
    l =[1,2,3,4,5,6,7,8,9,10]
    assert four_three(l) == 18, 'Improper reduce (four_three) function'


def test_num_plate_ka():
    list1 = num_plate_ka()
    assert sum([0 for i in list1 if i[0:2] == 'KA']) == 0, 'Improper num plate function'


def test_num_plate():
    list1 = f('DL')
    assert sum([0 for i in list1 if i[0:2] == 'DL']) == 0, 'Improper num plate (DL) function'
