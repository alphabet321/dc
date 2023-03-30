#include <stdio.h>
#include <math.h>

int main()
{
    int binary, decimal = 0, place = 0;

    printf("Enter a binary number: ");
    scanf("%d", &binary);

    while (binary > 0)
    {
        int digit = binary % 10;
        decimal += digit * pow(2, place);
        place++;
        binary /= 10;
    }

    printf("Decimal equivalent: %d\n", decimal);

    return 0;
}