// Program purpose: Find the multiples of 3 and 5
#include <iostream>

int main()
{
	int answer = 0;
	for (int x=0; x<1000; x++) // Uses X to check numbers up to 1000.
	{ 
		if (x % 5 == 0 || x % 3 == 0) 
		{ 
			answer += x; 
		}
	}
	std::cout << "The sum of all multiples of 3 and 5 is " << answer << ".\n\n";
	return 0;  
}

