from decorators import fibonacci, fibonacci_cache
from generators import fibonacci_gen, prime_gen
from iterators import Zip, Chain, Product, Open


def decorators_test():
    num = 30
    print("Cache using: ", fibonacci_cache(num), "\n")
    print("Function without cache decorator: ", fibonacci(num))


def iterators_test():
    zip_iter = Zip([1, 2, 3, 4], ("a", "b", "v", "g", "d"), "sdfsdfsd")
    print("Zip: ")
    for obj in zip_iter:
        print(obj, " ")

    chaine = Chain([1, 2, 3, 4], ("a", "b", "v"), "sdfsg")
    print("Chain: ")
    for obj in chaine:
        print(obj, end=" ")

    product = Product([1, 2, 3], ("a", "b", "v"), "ms")
    print("\nProduct: ")
    for prod in product:
        print(prod)


def generator_test():
    f = fibonacci_gen(10)
    print("Fibonacci: ", end="")
    for n in f:
        print(n, end=" ")
    print("\nPrime: ", end="")
    p = prime_gen(10)
    for n in p:
        print(n, end=" ")
    print("\n", "=" * 50)


def context_manager_test():
    with Open("file.txt", "w") as file:
        file.write("Lorem Ipsum")


def main():
    decorators_test()
    generator_test()
    iterators_test()
    context_manager_test()


if __name__ == '__main__':
    main()
