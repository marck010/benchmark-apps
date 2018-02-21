from datetime import datetime

if __name__ == '__main__':
    dataIni = datetime.now()
    n = 0
    j = 0
    i = 0
    while j < 10:
        while i < 1000000000:
                i += 1 
        j += 1
        

    print ('Elapsed Time: ' + str(datetime.now() - dataIni))