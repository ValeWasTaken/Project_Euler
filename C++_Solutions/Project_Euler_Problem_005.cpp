#include "stdafx.h"
#include <iostream>
using namespace std;

int main()
{
	int currentMax = 0;
	bool solution = false;

	do
	{
		solution = false;
		currentMax += 20;

		for (int iii = 11; iii < 20; iii++)
		{
			if (currentMax % iii)
			{
				solution = true;
				break;
			}
		}
	} while (solution);

	cout << "Smallest Multiple is " << currentMax << "\n";
	char z;
	cin >> z;
}
