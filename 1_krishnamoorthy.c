#include <stdio.h>

// Function to calculate the factorial of a number
int factorial(int n)
{
    int fact = 1;
    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }
    return fact;
}

// Function to check if a number is a Krishnamoorthy number
int isKrishnamoorthy(int n)
{
    int sum = 0;
    int temp = n;
    while (temp > 0)
    {
        sum += factorial(temp % 10);
        temp /= 10;
    }
    return sum == n;
}

int main()
{
    int n, sum = 0;
    printf("Enter the value of n: ");
    scanf("%d", &n);
    printf("The Krishnamoorthy numbers from 1 to %d are:\n", n);
    for (int i = 1; i <= n; i++)
    {
        if (isKrishnamoorthy(i))
        {
            printf("%d ", i);
            sum += i;
        }
    }
    printf("\n");
    printf("The sum of Krishnamoorthy series up to %d is %d\n", n, sum);
    return 0;
}
