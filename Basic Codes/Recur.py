def Sum(x) :
    if(x == 0) : return 0 ;
    return x + Sum(x-1);

def Fact(x) :
    if( x == 0 ) : return 1 ;
    return x * Fact(x-1);

def Fib(x) :
    if( x == 0 ) : return 1 ;
    if( x == 1 ) : return 1 ;
    return Fib(x-1) + Fib(x-2);

x = int( input() ) ;

print( "Sum upto 1.."+ str(x) + " is : "+ str(Sum(x)) );

print( str(x) + " ! = " + str(Fact(x)) ) ;

print( str(x) + "Th Fibonacci = " + str(Fib(x)) ) ;
