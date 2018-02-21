#include <stdio.h>
#include <time.h>

void main() {
    time_t t = time(NULL);
    struct tm tm = *localtime(&t);
    int sec;
    int n = 0;
    
    for (int j = 0; j < 10; j++)
    {
        for (int i = 0; i < 1000000000; i++)
        {
            n += i;
        }
    }

    time_t t1 = time(NULL);
    
    struct tm tmf = *localtime(&t1);
    
    printf("Elapsed Time: %d:%d:%d - %d:%d:%d \n", tm.tm_hour, tm.tm_min, tm.tm_sec, tmf.tm_hour, tmf.tm_min, tmf.tm_sec );
}
