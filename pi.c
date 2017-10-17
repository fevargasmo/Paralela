#include "omp.h"
#include "math.h"
#include <stdio.h>

void main()
{   
    int numThreads = 8;
    double pi = 0.0;
    double numIt = 1000000000;
    double numPart = numIt/numThreads;
    double piTmp[numThreads];
    omp_set_num_threads(numThreads);
    #pragma omp parallel
    {
        int n = omp_get_thread_num();
        piTmp[n] = 0.0;
        double inf = n*numPart;
        double sup = inf+numPart-1;
        for(double j = inf; j < sup; j++ )
        {
            piTmp[n] += ((pow(-1,j))/(2*j+1));
        }
    }
    for(int i = 0; i < numThreads; i++)
        pi += piTmp[i]*4;
    printf("pi = %.100f\n",pi);
}