# list method

def fib_list(num):
    # values for our first sequence
    start = 0
    finish = 1
    placeholder = 0
    fib_seq = []

    for i in range(num):  # perform operation "num" amount of times
        # first add 0 to the list for first sequence, 1 for second, 2 for third, etc
        fib_seq.append(start)
        # store start value as a placeholder value that can be use to "shift" forward our sequence
        placeholder = start
        # make the finish value our new start value to shift over "sliding door analogy"
        start = finish
        # add numbers together to perform the fiboacci sequence
        finish = placeholder + finish

    return print(fib_seq)


fib_list(20)

# generator method


def fib_gen(num):
    start = 0
    finish = 1
    placeholder = 0

    for i in range(num):
        yield start  # yield stops our code and store that value in memory
        placeholder = start
        start = finish
        finish = placeholder + finish


for i in fib_gen(20):

    print(f"{i} ", end="")
