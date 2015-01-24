# timus_helper

Helper for acm.timus.ru contestants.

Usage:
```
./timus.py <problem_id_number>
```

Script creates directory named the same as problem id number. In this directory there are sample inputs and outputs provided by problem authors.

## Tester
Sample tester is also created. Tester assumes, that executable file named `src` exists in problem directory. In this directory enter:

```
sh test.sh
```

To run all the tests and compare their outputs with samples. Warning: diff assumes there is a newline at the end of your output.
