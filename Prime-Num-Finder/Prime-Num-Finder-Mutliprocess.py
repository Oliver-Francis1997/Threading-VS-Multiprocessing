from multiprocessing import Pool
from time import perf_counter

def PrimeCheck(x):
    if x > 1:
        for i in range(2,x):
            if(x % i) == 0:
                return False
        return True
    return False

def ProcessVer(maxNum):
    # If processes is None then the number returned by os.cpu_count() is used.
    with Pool() as p:
        l = list(range(1,maxNum+1))
        results = p.map(PrimeCheck, l)
        return sum(results)

def main():
    maxNum = 500000

    startTime = perf_counter()
    primeNums = ProcessVer(maxNum)
    endTime = perf_counter()
    print(f'counting for multiprocess version took {round(endTime-startTime, 2)}s and there are {primeNums} prime numbers between 1-{maxNum}')

if __name__ == '__main__':
    main()