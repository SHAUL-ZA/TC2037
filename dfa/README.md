# **DFA**

#### Pablo Bolio Pradilla - A01782428
#### Shaul Zayat Askenazi - A01783240

## _Documentation_

---


## Instructions:
Create a function that receives a string in which there are aritemetical expressions and must return a list with each of the tokens found and indicate the type of data they have.

## Token Types

Tokens accepted in our expressions:
- Int
- Float
- Operators
   - Assign
   - Sum
   - Subtract
   - Multiplication
   - Division
   - Power
- Identifiers
   - Variables
- Special symbols 
   - (
   - )
- Comments (optional)
   - //until the end of the line

## Main Function

The program consists of a main function that must keep the name arithmetic-lexer(string expression) whose string represents the arithmetic expression to verify 

## Rules for specific cases

- 1. Variables
   - They must begin with a letter, either upper or lower case.


    - They can only consist of letters, numbers and underscore.

- 2. Real numbers

    - They can be positive or negative.

    - May or may not have a decimal part.

    - The exp notation can be used with e or E but then can only contain an integer value.

- 3. Comments (optional)

    - //until the end of the line.

# Manual

in the command line the function must be called inside a parenthesis followed by quotation marks where the arithmetic expression to be evaluated:

(arithmetic-lexer "string") 

## Output

In the output, each token within the string is obtained indicating to which data type it belongs.

# Technical information

The program was written in the Racket language version 8.8, so as a user it is necessary to have installed the Dr.Racket environment and to have the latest version of the language. 