def cached(func):
    def wrapper(*args):
        if str(args) in wrapper.__dict__:
            return wrapper.__dict__[str(args)]
        else:
            wrapper.__dict__.update({str(args): func(*args)})
            return wrapper.__dict__[str(args)]

    return wrapper


@cached
def fibbonaci(n):
    if n == 1 or 0 == n:
        return 1
    elif n < 0:
        return list()
    return fibbonaci(n-1) + fibbonaci(n-2)


def main():
    print(fibbonaci(0))
    print(fibbonaci(2))
    print(fibbonaci(12))


if __name__ == "__main__":
    main()
