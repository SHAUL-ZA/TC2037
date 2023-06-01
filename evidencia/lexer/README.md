# **Syntax Highlighter**
## *Authors*
    Pablo Bolio Pradilla - A01782428

    Shaul Zayat Askenazi - A01783240

<hr>

### Introduction
The following code defines a syntax highlighter for the Python programming language. To make this possible, it required knowledge of both the language syntax and the regular expressions used by Python. It's worth mentioning that regular expressions are used to find and manipulate character strings based on a predefined set of rules.

Python has its own unique words to define language-specific elements, and the highlighter's goal is to detect these reserved words or expressions and apply highlighting to them.

### Functioning
The code reads each line of the language and separates the string into segments at each encountered space. Therefore, in each iteration, a string segment is analyzed and compared against the declared regular expressions. If a segment matches any of the expressions, an HTML &lt;span&gt; element is generated to indicate the element's category and highlight it with an assigned color.

### Big O complexity
It's important to note that the algorithmic complexity of this syntax highlighter is quadratic, specifically *O(nk)*, where *n* refers to all the lines of the language that need to be traversed and compared, and *k* refers to the number of regular expressions declared. Each element of the line being analyzed will iterate through all the expressions until a match is found. While regular expressions can have a finite input, the code being analyzed can have a dynamic length, potentially leading to an infinite input size, causing the program's execution time to directly depend on the input size *n*.

### Implications
When considering ethical implications, one can argue that a syntax highlighter is highly useful and represents a beneficial advancement for individuals working in the technology field. The highlighter allows for distinguishing between the programmer's code and the language-specific elements. Assigning colors to language expressions provides specificity about the purpose of each code snippet.

In conclusion, a syntax highlighter promotes optimal code development, enhances readability, reduces errors, and facilitates comprehension of the code being read.

<hr>

## **Instructions**
