# Spoken to Written English:

Hello there, Aganitha Team! This is my submission for your programming exercise, to be submitted by 27th Oct 2019.

## How to run this code:

There's 2 folders IPYNB and PYCHARM, each containing one file containing code, and another containing the rules.
Both need to be in the same folder to work.

You can dump the contents of the IPYNB folder into a Jupyter notebook, or run the 'Aganitha Assignment 1.ipynb' 
in Google Colab, and upload (drag-drop) the 'Replacement Rulebook.txt' into the sidebar as shown in the .jpg
files in root directory. Run with Python 3 kernel.

If you use PyCharm or a similar IDE, you can simply open the entire folder as a project, and start by running 
'Aganitha Assignment 1.py'. The code uses regex and csv, so please install them if required. This file can run
using Python 3.7 interpreter.

## Features of this Code:

This code uses three functions to process the text input to output.

**Repeater:** 

Made to convert 'Triple A' and 'double x' to 'AAA' and 'xx' respectively. Also, humans usually follow
double or triple with a single letter while speaking, so I added a check that'll make sure that common phrases using these
words arent affected. 

Eg: "Staff are entitled to double time for each statutory holiday worked" won't change by this code. But "We're working
on a Triple A grade product" will be affected.

**Translator:**

This is where all your rules will be applied. 'Replacement Rulebook.txt' is a csv file with equal to sign as a separator,
this code checks for item in LHS of = and then replaces it with RHS of =. You can add your own rules as long as the LHS is in
UPPER CASE.

Eg: DOLLARS=$ in the .txt will make "I earn 30 dollars" to "I earn 30 $"

**Text2Num:**

This converts all text numbers in yout input to numeric form. It'll work on:

Years ('nineteen ninety seven'= 1997)

Pincodes ('one three eight five'= 1385)

Numbers ('eighty five thousand three hundred and twenty two'= 85322)

It's not perfect since there are times when the numbers won't be correct especially for complex examples where there's 
some hundreds of thousands, the word 'and' also plays a buggy role. But this is the best I could do.

**UI:**

I took the time to make the code user friendly by allowing the code to run until stopped by the user. 
Type Y or N to continue or exit the code makes it a lot more approachable and needed different ways to execute 
in .ipynb and .py. You can also exit by typing 'exit'.

*Examples of spoken english are already in the file 'Spoken English Examples.txt' that use as many of the functions as possible to showcase what my code can do.*
