'''Homework 1 Python Questions

This is an individual homework
Implement the following functions.

Do not add any more import lines to this file than the ones
already here without asking for permission on Piazza.
Use the regular expression tools built into Python; do NOT use bash.
'''

import re

def check_for_foo_or_bar(text):
   '''Checks whether the input string meets the following condition.

   The string must have both the word 'foo' and the word 'bar' in it,
   whitespace- or punctuation-delimited from other words.
   (not, e.g., words like 'foobar' or 'bart' that merely contain
    the word 'bar');

   See the Python regular expression documentation:
   https://docs.python.org/3.4/library/re.html#match-objects

   Return:
     True if the condition is met, false otherwise.
   '''

   pass


def replace_rgb(text):
   '''Replaces all RGB or hex colors with the word 'COLOR'
   
   Possible formats for a color string:
   #0f0
   #0b013a
   #37EfaA
   rgb(1, 1, 1)
   rgb(255,19,32)
   rgb(00,01, 18)
   rgb(0.1, 0.5,1.0)

   There is no need to try to recognize rgba or other formats not listed 
   above. There is also no need to validate the ranges of the rgb values.

   However, you should make sure all numbers are indeed valid numbers.
   For example, '#xyzxyz' should return false as these are not valid hex digits.
   Similarly, 'rgb(c00l, 255, 255)' should return false.

   Only replace matching colors which are at the beginning or end of the line,
   or are space separated from the text around them. For example, due to the 
   trailing period:

   'I like rgb(1, 2, 3) and rgb(2, 3, 4).' becomes 'I like COLOR and rgb(2, 3, 4).'

   # See the Python regular expression documentation:
   https://docs.python.org/3.4/library/re.html#re.sub

   Returns:
     The text with all RGB or hex colors replaces with the word 'COLOR'
   '''

   pass


def edit_distance(str1, str2):
  '''Computes the minimum edit distance between the two strings.

  Use a cost of 1 for all operations.

  See Section 2.4 in Jurafsky and Martin for algorithm details.
  Do NOT use recursion.

  Returns:
    An integer representing the string edit distance
    between str1 and str2
  '''

  pass


def wine_text_processing(wine_file_path, stopwords_file_path):
  '''Process the two files to answer the following questions and output results to stdout.

  1. What is the distribution over star ratings?
  2. What are the 10 most common words used across all of the reviews, and how many times
     is each used?
  3. How many times does the word 'a' appear?
  4. How many times does the word 'fruit' appear?
  5. How many times does the word 'mineral' appear?
  6. Common words (like 'a') are not as interesting as uncommon words (like 'mineral').
     In natural language processing, we call these common words "stop words" and often
     remove them before we process text. stopwords.txt gives you a list of some very
     common words. Remove these stopwords from your reviews. Also, try converting all the
     words to lower case (since we probably don't want to count 'fruit' and 'Fruit' as two
     different words). Now what are the 10 most common words across all of the reviews,
     and how many times is each used?
  7. You should continue to use the preprocessed reviews for the following questions
     (lower-cased, no stopwords).  What are the 10 most used words among the 5 star
     reviews, and how many times is each used? 
  8. What are the 10 most used words among the 1 star reviews, and how many times is
     each used? 
  9. Gather two sets of reviews: 1) Those that use the word "red" and 2) those that use the word
     "white". What are the 10 most frequent words in the "red" reviews which do NOT appear in the
     "white" reviews?
  10. What are the 10 most frequent words in the "white" reviews which do NOT appear in the "red"
      reviews?

  No return value.
  '''

  pass

