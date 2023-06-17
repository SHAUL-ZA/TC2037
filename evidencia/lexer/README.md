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

## **Parallel Lexer Analysis**
## **Runs**

### **V1.0**

|Run#          | Time(s)/Average|Speedup|  
| -----------  | ----------- | ----------- |
| 5            |     4.9766  | 1.0         |


<br>

### **V2.0**

- For each file a new thread is created.
If the number of files exceeds the number of processor threads, it will have to wait for a running thread to finish processing the remaining file.

|Run#          | Time(s)/Average|Speedup|
| -----------  | ----------- | ----------- |
| 5            |    10.5738  |    0.47     |


<hr>

## **Results**

In version 1.0, execution was performed by passing a path as a parameter that contained the folder and file to be processed. In version 2.0, only the folder path containing all the files is passed as a parameter, and each file is assigned to an available thread.

To simulate the test where everything runs on a single thread, the scripts from the 20 test files were consolidated into a single script so that this single file could be assigned to a single thread and the execution time could be measured.

Typically, parallel processing is expected to be more efficient as it divides a large task into smaller tasks. However, in this scenario, the execution time is observed to be twice as long as the single-threaded test. There could be multiple factors contributing to this observation, such as unknown input file sizes, as mentioned in algorithmic complexity, or the fact that one file is larger than another, causing threads to finish at different times. Additionally, if the number of files exceeds the number of threads that can run simultaneously, the system's scheduler will allocate available threads and wait for others to finish tasks before assigning them a file to process. It is worth mentioning that thread execution is not solely dedicated to the program, as the computer utilizes them for other operational tasks.

Overall, the performance of parallel execution depends on various factors, such as file sizes, thread availability, and the nature of the workload. It is essential to consider these factors and optimize the parallelization approach accordingly to achieve better execution times.

## **Instructions**
In order to run this code, there are some prerequisites you must fulfill:
- version: "0.1.0": meaning you must be running the version 0.1.0 of this elixir project
- elixir: "~> 1.14": meaning you must be using an elixir version greater than 1.14

Once that is fulfilled, to run this project, you must use this specific command on your CLI:
- `iex -S mix`

After that, the Interactive Elixir Shell is entered, once there you have to input this command:
- `Lexer.marker("test_file_location", "<html_name.html>")`

Now, the test files are located in this path:
- `test/Python_test_files/`

From there you have an extremely simple test file to showcase a syntax error that can be caught by our code or you can go to a directory containing projects from an open source repository:
- The test file: `testError.py`
- The open source repository: `From_github/`

Within the _From_Github_ path, there are 3 test files, each one of them is a project from an open source repository, the files are:
- `test1.py`
- `test2.py`
- `test3.py`

So the different paths you can use to test the code are:
- `test/Python_test_files/testError.py`
- `test/Python_test_files/From_github/test1.py`
- `test/Python_test_files/From_github/test2.py`
- `test/Python_test_files/From_github/test3.py`

And the name of the html file can be anything you want, for example:
- `example.html`

So the command you would input in the Interactive Elixir Shell would be:
- `Lexer.marker("test/Python_test_files/testError.py", "example.html")`

Or simply use the all.py file to test all the code at once:
- `Lexer.single_marker("test/Python_test_files/All_tests/all.py", "all.html"`

### Now to run the parallel version of the code, you must do the following:
you must use this specific command on your CLI:
- `iex -S mix`

After that, the Interactive Elixir Shell is entered, once there you have to input this command:
- `Lexer.markers("test/Python_test_files/From_github")`