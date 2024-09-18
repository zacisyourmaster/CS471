from typing import Callable
import random


def f(x) -> float:
    return 2 - (x**2)

def g(x) -> float:
    return (
        (0.0051 * (x**5))
        - (0.1367 * (x**4))
        + (1.24 * (x**3))
        - (4.456 * (x**2))
        + (5.66 * x)
        - 0.287
    )

def hill_climbing(
    func: Callable, bounds: list, step_size: float, init_state:float = None) -> tuple:
    """This function keeps track of one current state and on each iteration moves to the neighboring state with highest value,
    that is, it heads in the direction that provides the steepest ascent.
    It terminates when it reaches a 'peak' where no neighbor has a higher value.
    Args:
        func (Callable): The function to maximize.
        bounds (list): The lower and upper bounds for the search [l_bound, r_bound].
        step_size (float): The step size for moving left or right.
        init_state (float, optional): The initial state (starting point).
        
    Returns:
        tuple: A tuple containing the x-value and the corresponding maximum value of the function.
    """
    l_bound, r_bound = bounds
    x = init_state if init_state is not None else l_bound + (r_bound - l_bound) / 2
    curr = x
    while True:
        l_neighbor = curr - step_size
        r_neighbor = curr + step_size

        if l_neighbor >= l_bound and func(l_neighbor) > func(curr):
            curr = l_neighbor
        elif r_neighbor <= r_bound and func(r_neighbor) > func(curr):
            curr = r_neighbor
        else:
            break
    return (curr, func(curr))


if __name__ == "__main__":
    print("Question 1")
    print("a.")
    max_value = hill_climbing(f, [-5, 5], 0.5)
    print(f"  Max Value: {max_value[1]} ({max_value[0]},{max_value[1]})")

    print("b.")
    max_value = hill_climbing(f, [-5, 5], 0.01)
    print(f"  Max Value: {max_value[1]} ({max_value[0]},{max_value[1]})")

    print("-" * 50)

    print("Question 2")
    print("a.")
    values = []
    restarts = 20

    for _ in range(restarts):
        x = random.randint(0, 20) / 2
        v = hill_climbing(g, [0, 10], 0.5, x)
        values.append(v)

    max_value = max(values, key=lambda d: d[1])
    print(f"  Max Value: {max_value[1]} ({max_value[0]},{max_value[1]})")

    print("b.")
    hc_max = hill_climbing(g, [0, 10], 0.5)
    print(f"Hill Climb: {hc_max[1]}")
    print(f"Random Restart Hill Climb: {max_value[1]}")
