#ifndef pt1_h
#define pt1_h

extern double y;
extern double u;

void init(void);
void step(void);

double f_u(double t);
int mode(double t);

#endif /* pt1_h */
