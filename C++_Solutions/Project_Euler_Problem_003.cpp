#include <iostream>
    // Optionally, you could replace my "std::"s with "using namespace std;" here.
int main()
{
	long long int num = 600851475143; // Replace this with any largest prime number you want.
	long long int x = 2;
	while (x*x < num)
	{
		while (num % x == 0)
		{
			num /= x; 
		}
		x = x++;
	}
	std::cout << num;
	return 0;
}
