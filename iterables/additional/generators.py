def fibonacci_gen(length):
    """ Generate a sequence of fibonacci numbers."""
    previous, current = 1, 1
    while length > 0:
        yield previous
        previous, current = current, previous + current
        length -= 1


def prime_gen(length):
    """ Generate a sequence of prime numbers."""
    D = {}
    counter = 0
    temp = 2
    while counter < length:
        if temp not in D:
            counter += 1
            yield temp
            D[temp * temp] = [temp]
        else:
            for p in D[temp]:
                D.setdefault(p + temp, []).append(p)
            del D[temp]
        temp += 1
