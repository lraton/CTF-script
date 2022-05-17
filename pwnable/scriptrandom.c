#include <stdio.h>
#include <stdlib.h>

int main(){
        unsigned int  solve;
        unsigned int  random;
        random=rand();
       
        solve= 0xdeadbeef^random;
        printf("%u",solve);
        return 0;
}

