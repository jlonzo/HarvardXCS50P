# HarvardXCS50P-
HarvardX CS50P Introduction to Programming with Python


## Problem Sets

### Unit 1: Functions, Variables

1. Indoor Voice
<p>In a file called indoor.py, implement a program in Python that prompts the user for input and then outputs that same input in lowercase.  
Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.</p>

2. Playback Speed
<p>In a file called playback.py, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with ... (i.e., three periods).</p>

3. Making Faces
<p>In a file called faces.py, implement a function called convert that accepts a str as input and returns that same input with any :) converted to 🙂 (otherwise known as a slightly smiling face) and any :( converted to 🙁 (otherwise known as a slightly frowning face). All other text should be returned unchanged.

Then, in that same file, implement a function called main that prompts the user for input, calls convert on that input, and prints the result. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input. Be sure to call main at the bottom of your file.</p>

4. Einstein
<p>In a file called einstein.py, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.</p>

5. Tip Calculator
<p> Implement two functions:  
	* dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), remove the leading $, and return the amount as a float. For instance, given 50.00 as input, it should return 50.0.  
	* percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
</p>

### Unit 2: Conditionals

1. Deep Thought
<p>In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or (case-insensitively) forty-two or forty two. Otherwise output No.</p>

2. Home Federal Savings Bank
<p>In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.</p>

3. File Extensions
<p>In a file called extensions.py, implement a program that prompts the user for the name of a file and then outputs that file’s media type if the file’s name ends, case-insensitively, in any of these suffixes:  
	* .gif
	* .jpg
    * .jpeg
    * .png
    * .pdf
    * .txt
    * .zip

If the file’s name ends with some other suffix or has no suffix at all, output application/octet-stream instead, which is a common default.</p>

4. Math Interpreter
<p>In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:  
	* x is an integer
	* y is +, -, *, or /
    * z is an integer

For instance, if the user inputs 1 + 1, your program should output 2.0. Assume that, if y is /, then z will not be 0.

Note that, just as python itself is an interpreter for Python, so will your interpreter.py be an interpreter for math!</p>

5. Meal Time
<p>In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.

Structure your program per the below, wherein convert is a function (that can be called by main) that converts time, a str in 24-hour format, to the corresponding number of hours as a float. For instance, given a time like "7:30" (i.e., 7 hours and 30 minutes), convert should return 7.5 (i.e., 7.5 hours).</p>

### Unit 3: Loops

1. camelCase
<p>In some languages, it’s common to use camel case (otherwise known as “mixed case”) for variables’ names when those names comprise multiple words, whereby the first letter of the first word is lowercase but the first letter of each subsequent word is uppercase. For instance, whereas a variable for a user’s name might be called name, a variable for a user’s first name might be called firstName, and a variable for a user’s preferred first name (e.g., nickname) might be called preferredFirstName.</p>

Python, by contrast, recommends snake case, whereby words are instead separated by underscores (_), with all letters in lowercase. For instance, those same variables would be called name, first_name, and preferred_first_name, respectively, in Python.

In a file called camel.py, implement a program that prompts the user for the name of a variable in camel case and outputs the corresponding name in snake case. Assume that the user’s input will indeed be in camel case.