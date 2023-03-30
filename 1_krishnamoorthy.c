#include <stdio.h>

int main()
{
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    int sum = 0, term = 1;
    for (int i = 1; i <= n; i++)
    {
        sum += term;
        term *= i;
    }

    printf("Sum of Krishnamoorthy series numbers till %d: %d\n", n, sum);

    return 0;
}