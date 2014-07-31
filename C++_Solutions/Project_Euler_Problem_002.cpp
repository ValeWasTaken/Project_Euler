#include <iostream>

int main()
{
	int a = 0, b = 1, c = 0, d = 0;
	while (c < 3500000)
	{
		c = a + b; // Calculates fibonacci sequence starting at 0,1,1,..
		std::cout << c << std::endl;
		a = b; 
		b = c;
		if (c % 2 == 0)
		{d += c;}
	}
	std::cout << "The sum of all EVEN fibonacci values under 4million is: " << d << std::endl;
	return 0;
}
