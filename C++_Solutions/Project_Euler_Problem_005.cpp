#include <iostream>

int main()
{
	int currentMax = 0;
	bool solution = false;

	do
	{
		solution = false;
		currentMax += 20;

		for (int i = 11; i < 20; i++)
		{
			if (currentMax % i)
			{
				solution = true;
				break;
			}
		}
	} while (solution);
	
	std::cout << "Smallest Multiple is " << currentMax << "\n\n";
	return 0;
}
