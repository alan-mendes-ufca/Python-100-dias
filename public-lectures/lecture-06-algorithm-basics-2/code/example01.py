def fac(num):
    if not isinstance(num, int) or num < 0:
        raise ValueError('num must be a non-negative integer')
    result = 1
    for factor in range(2, num + 1):
        result *= factor
    return result


def main():
    num = 1000
    result = fac(num)
    print(f'{num}! has {len(str(result))} digits')


if __name__ == '__main__':
    main()
# for i in range(1000):
#     print(f'{i}:'.rjust(3), fac(i))
