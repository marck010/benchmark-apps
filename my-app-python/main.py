from datetime import datetime


if __name__ == '__main__':
    dataIni = datetime.now()
    n = {}
    n["i"] = 0

    for j in range(10):
        for i in range(1000000000):
                n["i"] += i


    print ('Elapsed Time: ' + str(datetime.now() - dataIni))