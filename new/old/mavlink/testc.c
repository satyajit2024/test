#include <stdio.h>
// #include <winsock.h>

void newdc_function()
{
    printf("Inside newdc_function\n");
}
int main()
{
    // socket(AF_INET, SOCK_STREAM, 0);

    struct testc
    {
        int a;
        int b;
        int c;

        void (*newdc)();

    } hello;

    hello.a = 1;
    hello.b = 2;
    hello.c = 3;
    printf("hello.a: %d\n", hello.a);
    printf("hello.b: %d\n", hello.b);
    printf("hello.c: %d\n", hello.c);
    hello.newdc = newdc_function;
    hello.newdc();
    return 0;
}

