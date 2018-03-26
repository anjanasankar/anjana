int  nextPower_2 ( unsigned  int  x )
{
int  counter  =  0 ;
while ( x > 0 )
{
count ++ ;
x  =  x  >>  1 ;
}
return  (1 << counter) ;
}
