#include "iut.h"

double y;
double u;

static double x;

static const double K = 1.0;
static const double T = 1.50;
static const double dt = 0.01;

void init(void){
    u = 0.0;
    y = 0.0;
    x = 0.0;
}

void step(void){
    x = y;
    y = x + (K*u - x)*dt/T;
}

double f_u(double t){
    if(t < 7.0)
        return 0.0;
    else
        return 1.0;
}

int mode(double t){
    if(t < 3.0)
        return 0;
    else if(t < 6.0)
        return 1;
    else if(t < 10.0)
        return 2;
    else
        return 0;
}
