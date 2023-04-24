#|
  Pablo Bolio Pradilla - A01782428
  Shaul Zayat Askenazi - A01783240
|#
#lang racket
(require racket/trace)

(provide (all-defined-out))

; Declare the structure that describes a DFA
(struct dfa (func initial accept))

(define (arithmetic-lexer strng)
  " Call the function to validate using a specific DFA "
  (evaluate-dfa (dfa delta-arithmetic 'start '(int float exp var spa par_open par_close)) strng))

(define (evaluate-dfa dfa-to-evaluate strng)
  " This function will verify if a string is acceptable by a DFA "
  (let loop
    ; Convert the string into a list of characters
    ([chars (string->list strng)]
     ; Get the initial state of the DFA
     [state (dfa-initial dfa-to-evaluate)]
     ; The return list with all the tokens found
     [tokens '()]
     [lst '()])
    (cond
      ; When the list of chars if over, check if the final state is acceptable
      [(empty? chars)
       (cond 
        [(member state (dfa-accept dfa-to-evaluate))
         ; Add the last pending state to the list, and reverse it
         (reverse (cons (list (list->string (reverse lst)) state) tokens))]
        [(eq? state 'spa) (reverse tokens)]
        [else #f])]
      [(eq? state 'inv)
        #f]
      [else
        (let-values
          ; Call the transition function and get the new state and whether or not a token was found
          ([(new-state found) ((dfa-func dfa-to-evaluate) state (car chars))])
          (loop (cdr chars) 
                new-state
                ; The new list of tokens
                (if found (cons (list (list->string (reverse lst)) found) tokens) tokens) 
                (if found 
                  (if (eq? (car chars) #\space) 
                    '() 
                    (list (car chars)))
                  (if (eq? (car chars) #\space) 
                      lst 
                      (cons (car chars) lst)))))])))

(define (char-operator? char)
  " Identify caracters that represent arithmetic operators "
  (member char '(#\+ #\- #\* #\/ #\= #\^ #\( #\))))

(define (delta-arithmetic state char)
  (case state
    ['start (cond #|Start state|#
             [(char-numeric? char) (values 'int #f)]
             [(or (eq? char #\+) (eq? char #\-)) (values 'sign #f)]
             [(or (char-alphabetic? char) (eq? char #\_)) (values 'var #f)]
             [(eq? char #\() (values 'par_open #f)]
             [(eq? char #\space) (values 'spa #f)]
             [else (values 'inv #f)])]
    ['sign (cond #|Sign state|#
             [(char-numeric? char) (values 'int #f)]
             [else (values 'inv #f)])]
    ['int (cond #|Int state|#
             [(char-numeric? char) (values 'int #f)]
             [(eq? char #\.) (values 'dot #f)]
             [(or (eq? char #\e) (eq? char #\E)) (values 'e #f)]
             [(eq? char #\space) (values 'spa 'int)]
             [(eq? char #\+) (values 'op 'int)]
             [(eq? char #\-) (values 'op 'int)]
             [(eq? char #\*) (values 'op 'int)]
             [(eq? char #\/) (values 'op 'int)]
             [(eq? char #\=) (values 'op 'int)]
             [(eq? char #\^) (values 'op 'int)]
             [(eq? char #\)) (values 'par_close 'int)]
             [else (values 'inv #f)])]
    ['dot (cond #|Dot state|#
             [(char-numeric? char) (values 'float #f)]
             [else (values 'inv #f)])]
    ['float (cond #|Float state|#
             [(char-numeric? char) (values 'float #f)]
             [(or (eq? char #\e) (eq? char #\E)) (values 'e #f)]
             [(eq? char #\space) (values 'spa 'float)]
             [(eq? char #\+) (values 'op 'float)]
             [(eq? char #\-) (values 'op 'float)]
             [(eq? char #\*) (values 'op 'float)]
             [(eq? char #\/) (values 'op 'float)]
             [(eq? char #\=) (values 'op 'float)]
             [(eq? char #\^) (values 'op 'float)]
             [(eq? char #\)) (values 'par_close 'float)]
             [else (values 'inv #f)])]
    ['e (cond #|E state|#
             [(or (eq? char #\+) (eq? char #\-)) (values 'e_sign #f)]
             [(char-numeric? char) (values 'exp #f)]
             [else (values 'inv #f)])]
    ['e_sign (cond #|E_sign state|#
             [(char-numeric? char) (values 'exp #f)]
             [else (values 'inv #f)])]
    ['exp (cond #|Exp state|#
             [(char-numeric? char) (values 'exp #f)]
             [(eq? char #\space) (values 'spa 'exp)]
             [(eq? char #\+) (values 'op 'exp)]
             [(eq? char #\-) (values 'op 'exp)]
             [(eq? char #\*) (values 'op 'exp)]
             [(eq? char #\/) (values 'op 'exp)]
             [(eq? char #\=) (values 'op 'exp)]
             [(eq? char #\^) (values 'op 'exp)]
             [(eq? char #\)) (values 'par_close 'exp)]
             [else (values 'inv #f)])]
    ['var (cond #|Var state|#
             [(or (char-alphabetic? char) (eq? char #\_) (char-numeric? char)) (values 'var #f)]
             [(eq? char #\space) (values 'spa 'var)]
             [(eq? char #\+) (values 'op 'var)]
             [(eq? char #\-) (values 'op 'var)]
             [(eq? char #\*) (values 'op 'var)]
             [(eq? char #\/) (values 'op 'var)]
             [(eq? char #\=) (values 'op 'var)]
             [(eq? char #\^) (values 'op 'var)]
             [(eq? char #\)) (values 'par_close 'var)]
             [else (values 'inv #f)])]
    ['spa (cond #|Space state|#
             [(eq? char #\space) (values 'spa #f)]
             [(char-numeric? char) (values 'int #f)]
             [(or (char-alphabetic? char) (eq? char #\_)) (values 'var #f)]
             [(eq? char #\+) (values 'op #f)]
             [(eq? char #\-) (values 'op #f)]
             [(eq? char #\*) (values 'op #f)]
             [(eq? char #\/) (values 'op #f)]
             [(eq? char #\=) (values 'op #f)]
             [(eq? char #\^) (values 'op #f)]
             [(eq? char #\)) (values 'par_close #f)]
             [else (values 'inv #f)])]
    ['op (cond
       [(char-numeric? char) (values 'int 'op)]
       [(or (eq? char #\+) (eq? char #\-)) (values 'sign 'op)]
       [(char-alphabetic? char) (values 'var 'op)]
       [(eq? char #\_) (values 'var 'op)]
       [(eq? char #\space) (values 'op_spa 'op)]
       [else (values 'inv 'op)])]
    ['op_spa (cond
       [(char-numeric? char) (values 'int #f)]
       [(or (eq? char #\+) (eq? char #\-)) (values 'sign #f)]
       [(or (char-alphabetic? char) (eq? char #\_)) (values 'var #f)]
       [(eq? char #\space) (values 'op_spa #f)]
       [else (values 'inv #f)])]
    ['par_open (cond #|Opening Parenthesis state|#
             [(eq? char #\() (values 'par_open 'par_op)]
             [(eq? char #\space) (values 'spa 'par_open)]
             [(or (char-alphabetic? char) (eq? char #\_)) (values 'var 'par_open)]
             [(or (eq? char #\+) (eq? char #\-)) (values 'sign 'par_open)]
             [(char-numeric? char) (values 'int 'par_open)]
             [(eq? char #\)) (values 'par_close 'par_open)]
             [else (values 'inv #f)])]
    ['par_close (cond #|Closing Parenthesis state|#
             [(eq? char #\)) (values 'par_close 'par_close)]
             [(eq? char #\space) (values 'spa 'par_close)]
             [(eq? char #\+) (values 'op 'par_close)]
             [(eq? char #\-) (values 'op 'par_close)]
             [(eq? char #\*) (values 'op 'par_close)]
             [(eq? char #\/) (values 'op 'par_close)]
             [(eq? char #\=) (values 'op 'par_close)]
             [(eq? char #\^) (values 'op 'par_close)]
             [else (values 'inv #f)])]))