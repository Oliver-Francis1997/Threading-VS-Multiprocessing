from concurrent.futures import ThreadPoolExecutor
from os import cpu_count
from time import perf_counter

def PrimeCheck(x):
    if x > 1:
        for i in range(2,x):
            if(x % i) == 0:
                return False
        return True
    return False

def ThreadVer(maxNum):
    with ThreadPoolExecutor(max_workers=cpu_count()) as e:
        l = list(range(1,maxNum+1))
        results = e.map(PrimeCheck, l)
        return sum(results)

def main():
    maxNum = 500000

    startTime = perf_counter()
    primeNums = ThreadVer(maxNum)
    endTime = perf_counter()
    print(f'counting for threaded version took {round(endTime-startTime, 2)}s and there are {primeNums} prime numbers between 1-{maxNum}')

if __name__ == '__main__':
    main()