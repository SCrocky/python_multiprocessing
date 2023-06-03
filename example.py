import multiprocessing
from typing import List


def collatz(n: int, msg: str) -> str:
    """
    A simple function that checks the Collatz Conjecture for an int n and then returns a message.
    :param n: The int for which to check
    :param msg: The message to print at the end, it is used to demonstrate usage of `starmap`.
    :return:
    """
    final_msg = f"Checked for {n}: {msg}"
    # Eliminating obvious cases
    if n <= 1:
        return final_msg
    # Looping while conjecture is false
    while n > 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
    return final_msg


def check_collatz_until(n: int) -> List[str]:
    """
    Checks Collatz conjecture until an integer n
    :param n: The highest value to check for
    :return:
    """
    # Creating our inputs for the solving function
    task_list = []
    for i in range(1, n + 1):
        task_list.append(
            (i, "Collatz was right!")
        )
    # Using Pool without arguments uses CPU count as default: https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool
    with multiprocessing.Pool() as pool:
        # Used for functions with multiple arguments: https://docs.python.org/3/library/multiprocessing.html#multiprocessing.pool.Pool.starmap
        # Can be replaced by `map` if functions have single arguments.
        results = pool.starmap(collatz, task_list)
    # `results` will contain the list of the `collatz` function results
    return results
