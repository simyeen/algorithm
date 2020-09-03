# max 이하 숫자의 숫자들에 대한 소수 판별 체
def get_prime_bool(max):
    sieve = [False, False] + [True] * (max-1)

    max_root = int(max ** 0.5)
    for i in range(2, max_root+1):
        if sieve[i]:
            for j in range(2*i, max+1, i):
                sieve[j] = False

    return sieve


def get_prime_num(max):
    sieve = get_prime_bool(max)
    max_root = int(max ** 0.5)
    nums = []
    for i in range(2, max_root + 1):
        if sieve[i]:
            nums.append(i)
    return nums


primes = get_prime_num(10000000)

n = int(input())
root_n = n ** 0.5
for p in primes:
    if p > root_n and n > 1:
        print(n)
        break
    while n % p == 0:
        n = n // p
        print(p)
