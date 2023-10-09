#!/usr/bin/python3

def my_function():
    pass

def is_winner(x, nums):
    def sieve_of_eratosthenes(limit):
        primes = [True] * (limit + 1)
        primes[0] = primes[1] = False
        p = 2
        while p * p <= limit:
            if primes[p]:
                for i in range(p * p, limit + 1, p):
                    primes[i] = False
            p += 1
        return [i for i, is_prime in enumerate(primes) if is_prime]

    def game_winner(n):
        primes = sieve_of_eratosthenes(n)
        num_primes = len(primes)
        if num_primes % 2 == 0:
            return "Ben"
        else:
            return "Maria"

    winners = [game_winner(n) for n in nums]
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
