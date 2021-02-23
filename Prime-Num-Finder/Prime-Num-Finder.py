from time import perf_counter


def PrimeCheck(x):
    if x > 1:
        for i in range(2,x):
            if(x % i) == 0:
                return False
        return True
    return False

def BaseVer(maxNum):
    primeCount = 0
    for i in range(1, maxNum):
        if PrimeCheck(i):
            primeCount += 1
    return primeCount

def main():
    maxNum = 500000

    startTime = perf_counter()
    primeNums = BaseVer(maxNum)
    endTime = perf_counter()
    print(f'counting for single loop took {round(endTime-startTime, 2)}s and there are {primeNums} prime numbers between 1-{maxNum}')

if __name__ == '__main__':
    main()