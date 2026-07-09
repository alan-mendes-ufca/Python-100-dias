"""Exemplo de co-rotina."""
import asyncio

from example15 import is_prime


def num_generator(m, n):
    """Gere números no intervalo fornecido."""
    yield from range(m, n + 1)


async def prime_filter(m, n):
    """Filtre números primos."""
    primes = []
    for i in num_generator(m, n):
        if is_prime(i):
            print('Prime =>', i)
            primes.append(i)

        await asyncio.sleep(0.001)
    return tuple(primes)


async def square_mapper(m, n):
    """Mapeie números em quadrados."""
    squares = []
    for i in num_generator(m, n):
        print('Square =>', i * i)
        squares.append(i * i)

        await asyncio.sleep(0.001)
    return squares


async def main():
    """Ponto de entrada do programa."""
    result = await asyncio.gather(
        prime_filter(2, 100), square_mapper(1, 100)
    )
    print(result)


if __name__ == '__main__':
    asyncio.run(main())
