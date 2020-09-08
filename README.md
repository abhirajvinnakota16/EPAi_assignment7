# Assignment 7

This assignment has the functions that were written majorly using list comprehensions, reduce function, partial function, filter, map and zip functions as well as the lambda function.

## 'fib()'
This function generates the fibonacci series unpto 10000th number and then checks the list of numbers provided to it and returns the list of fibonacci numbers in that list.  

## 'two_one()'
This function is a list comprehension that accepts 2 lists of numbers. Adds every even number in the first list to every odd number in the second list and returns a list of numbers.

## 'two_two()'
This function accepts a string and strips itself of the vovels and returns a list of the remianing characters, using list comprehension.

## 'two_three()'
This function uses a list comprehension that imitates a ReLu function, on the list of numbers that it accepts.

## 'two_four()'
This function uses a list comprehension that imitates a Sigmoid function, on the list of numbers that it accepts.

## 'two_five()'
This function accepts a string of ASCII printable characters and returns a lost of each of these characters shifted by a value of 5, using a combination of lambda functions and list comprehensions.

## 'word_search()'
This function accepts approx. 200 worded text, processes it and then checks it against a list of words banned by Google, classified as abusive words. It uses multiple list comprehensions at every step. 

## 'four_one()'
This function uses a reduce function to accept a list of numbers and return the sum of all its even numbers

## 'four_two()'
This function uses a reduce function to accept a list of characters and returns the character with the highest ASCII value. 

## 'four_three()'
This function uses a reduce function to accept a list of numbers and adds every third numbers in it.

## 'num_plate_ka()'
This function generates 15 number plates with KA as their first 2 letters. It uses multiple list comprehensions as well as a couple of functions from the random module to achieve this.

## 'num_plate()'
This function generates 15 number plates using the same structure as the previous code. However, it does not code the first 2 letters as well as the last 4 letters, rather accepts from the user. On top of this, a partial function has been used wherein the input is accepted for the first 2 letters while the last 4 letters are hard coded as well. 

The basic tests have been written as well as one test for each of the functions to ensure they are functioning properly.