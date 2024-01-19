// Includes

int* Test1()
{
    int x = 10;
    return &x;
}

int main()
{
    int* ret = Test1();

    printf("%d", *ret);

    //Print the data

    return 0;
}