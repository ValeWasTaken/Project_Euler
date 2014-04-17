#include "stdafx.h"
#include <iostream>

int main()
{
	int a = 0, b = 1, c = 0, d = 0; // Defines variables for the rest of the program
	while (c < 3500000) // While value "c" is less than 3.5mil, execute below code.
	{
		c = a + b; // Calculates fibonacci sequence starting at 0,1,1,..
		std::cout << c << std::endl; // Displays current number in sequence being counted.
		a = b; // Continues Fibonacci sequence
		b = c;
		if (c % 2 == 0)
		{
			d += c;
		}
	}
	std::cout << "The sum of all EVEN fibonacci values under 4million is: " << d << std::endl;

	system("pause");
	return 0;
}
