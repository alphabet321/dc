#include <stdio.h>
#include <math.h>

int main()
{
    int n;
    printf("Enter n: ");
    scanf("%d", &n);

    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        int temp = i;
        int num_digits = 0;
        while (temp > 0)
        {
            num_digits++;
            temp /= 10;
        }
        temp = i;
        int digit_sum = 0;
        while (temp > 0)
        {
            int digit = temp % 10;
            digit_sum += pow(digit, num_digits);
            temp /= 10;
        }
        if (digit_sum == i)
        {
            sum += i;
        }
    }

    printf("Sum of Armstrong numbers till %d: %d\n", n, sum);

    return 0;
}