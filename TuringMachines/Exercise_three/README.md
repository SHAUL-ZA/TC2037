# **Turing Machines**
## *Authors*
    Pablo Bolio Pradilla - A01782428

    Shaul Zayat Askenazi - A01783240

<hr>

## Exercise three
Subtraction of unitary numbers. The first number will always be greater than or equal to the second.

### Explanation
A unary subtraction of strings consisting only of 1's is performed.

Examples:

| Input       | Result      |
| ----------- | ----------- |
| 111-11      | 1           |
| 11111-111   | 11          |
| 1-1         | ' '         |

<br>

## Diagram
### status of acceptance: "ok"
<img src="./ExerciseThree_diagram.png" alt="StateMachine">

## Code
```
input: '1111-11'
blank: ' '
start state: q0
table:
  q0:
    '1': R
    '-': {R: 'q1'}
    ' ': {R: 'invalid'}
  q1:
    '1': R
    ' ': {L: 'q2'}
  q2:
    '1': {write: ' ', L: 'q3'}
    '-': {write: ' ', L: 'ok'}
  q3:
    '1': L
    '-': {L: 'q4'}
  q4:
    '1': L
    ' ': {R: 'q5'}
  q5:
    '1': {write: ' ', R: 'q0'}
  ok:
  invalid:
  ```

