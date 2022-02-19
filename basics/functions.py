def list_benefits():
    return [
        "More organized code", "More readable code", "Easier code reuse",
        "Allowing programmers to share and connect code together"
    ]


def build_sentence(benefit):
    return f"{benefit} is a benefit of functions!"


def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


def foo(a, b, c, *args):
    return len(args)


def bar(a, b, c, **kwargs):
    return kwargs["magicnumber"] == 7


def main():
    # 1 task
    name_the_benefits_of_functions()

    print()

    # 2 task
    if foo(1, 2, 3, 4) == 1:
        print("Good.")
    if foo(1, 2, 3, 4, 5) == 2:
        print("Better.")
    if not bar(1, 2, 3, magicnumber=6):
        print("Great.")
    if bar(1, 2, 3, magicnumber=7):
        print("Awesome!")


if __name__ == "__main__":
    main()
