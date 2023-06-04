# python_multiprocessing

Uses the [multiprocessing package](https://docs.python.org/3/library/multiprocessing.html) to run many processes in parallel.

Check the `example.py` code to get started.

To run the example simply use python interactive mode: `python -i example.py`

And run both the linear and the parallelized function:
```
>>> a = check_collatz_linear(10**6)
Execution of check_collatz_linear took: 0:00:09.387807

>>> b = check_collatz_until(10**6)
Execution of check_collatz_until took: 0:00:01.196699

```