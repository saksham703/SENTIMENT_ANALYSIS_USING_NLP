"""
NLTK is a leading platform for building Python programs to work with human language data.
It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet,
along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing,
and semantic reasoning, wrappers for industrial-strength NLP libraries, and an active discussion forum.

Thanks to a hands-on guide introducing programming fundamentals alongside topics in computational linguistics,
plus comprehensive API documentation, NLTK is suitable for linguists, engineers, students, educators, researchers,
 and industry users alike. NLTK is available for Windows, Mac OS X, and Linux. Best of all, NLTK is a free, open source,
  community-driven project.

NLTK has been called “a wonderful tool for teaching, and working in, computational linguistics using Python,” and “an
 amazing library to play with natural language.”

Natural Language Processing with Python provides a practical introduction to programming for language processing.
 Written by the creators of NLTK, it guides the reader through the fundamentals of writing Python programs, working with corpora,
  categorizing text, analyzing linguistic structure, and more. The online version of the book has been been updated
   for Python 3 and NLTK 3. (The original Python 2 version is still available at https://www.nltk.org/book_1ed.)

"""


import nltk

"""
TextBlob is a Python (2 and 3) library for processing textual data. It provides a simple API for diving into common
 natural language processing (NLP) tasks such as part-of-speech tagging, noun phrase extraction, sentiment analysis,
  classification, translation, and more.
  TextBlob is a python library and offers a simple API to access its methods and perform basic NLP tasks. 

A good thing about TextBlob is that they are just like python strings.
 So, you can transform and play with it same like we did in python. Below, 
 I have shown you below some basic tasks. Don’t worry about the syntax, 
 it is just to give you an intuition about how much-related TextBlob is to Python strings.
"""

from textblob import TextBlob

"""
Developers often have a need to interact with users, either to get data or to provide some sort of result. 
Most programs today use a dialog box as a way of asking the user to provide some type of input. While Python provides us 
with two inbuilt functions to read the input from the keyboard.

input ( prompt )
raw_input ( prompt )

input ( ) : This function first takes the input from the user and then evaluates the expression,
 which means Python automatically identifies whether user entered a string or a number or list. 
 If the input provided is not correct then either syntax error or exception is raised by python.
 
"""
y=input("Type your sentence: ")
edu=TextBlob(y)
x=edu.sentiment.polarity

# Checking polarity of sentence



    # check the condition if x is less than 0

    # print that the sentence is negetive

if x < 0:

    print("Negative")

    # check the condition if x is equal to 0

    # print that the sentence is neutral

elif x==0:

     print("Neutral")

     # check the condition if x is greater than 0

     # print that the is positive

elif x>0 and x<=1:

    print("positive")
