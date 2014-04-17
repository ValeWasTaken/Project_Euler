#include "stdafx.h" // For Visual Studio
#include <iostream>

int main()
{
	// Start of "Square of sums" block
	int n = 0;
	for (int x = 0; x < 101; x++)
	{
		n += x;
	}
	int final_num = n*n;
	std::cout << "The square of the sum of the first 100 natural numbers is: " << final_num << std::endl; // Expected output: 25502500

	// Start of "Sum of squares" block
	int num = 0;
	for (int y = 0; y < 101; y++)
	{
		num += (y*y);
	}
	std::cout << "The sum of the squares of the first 100 natural numbers is: " << num << std::endl; // Expected output: 338350

	// Final calculation
	int difference = final_num - num;
	std::cout << "The difference between the two sums is: " << difference << std::endl; // Expected output: 25164150
	system("pause");
}
