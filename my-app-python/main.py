from datetime import datetime


if __name__ == '__main__':
    dataIni = datetime.now()
    try:   
        n = {}
        n["i"] = 0
        for j in range(5):
            for i in range(1000000000):
                 n["i"] += i

        #print n
    except Exception, ex:
        print ex

    print 'Time spent routine integration-hierarchies: ' + str(datetime.now() - dataIni)