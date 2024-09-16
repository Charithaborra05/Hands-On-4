def fibonacci(num, memo=None):
    if memo is None:
        memo = {}

    if num in memo:
        return memo[num]

    if num == 0:
        return 0
    if num == 1:
        return 1

    memo[num] = fibonacci(num - 1, memo) + fibonacci(num - 2, memo)
    return memo[num]


# Debugging fibonacci(5)
def fibonacci_debug(num):
    trace_calls = []

    def helper_fib(x):
        trace_calls.append(f'fibonacci({x})')
        if x in memo:
            return memo[x]
        if x == 0:
            return 0
        if x == 1:
            return 1
        memo[x] = helper_fib(x - 1) + helper_fib(x - 2)
        return memo[x]

    memo = {}
    final_result = helper_fib(num)
    return trace_calls, final_result


trace_calls, final_result = fibonacci_debug(5)
print("Trace of Calls:", " -> ".join(trace_calls))
print("Final Result:", final_result)
