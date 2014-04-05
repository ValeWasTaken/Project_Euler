public class Project_Euler_Problem_004 
{
	public static void main(String args[]) 
	{ 
		int largest_palindrome = 100000; // This can be changed to many numbers, even zero. I put 100,000 just as a safety net.
		for (int i = 999; i > 100; i--) 
		{
			for (int j = 999; j > 100; j--) 
			{ 
				int k = i * j;
				String z = String.valueOf(k);
				if (new StringBuffer(z).reverse().toString().equals(z) && k > largest_palindrome) 
				{ 
					largest_palindrome = k;
				} 
			} 
		} 
		System.out.println("The largest palindrome is: " + largest_palindrome);
	}
}

/*
Notes:
- This program can be modified fairly easily to find palindromes for other numbers.
To do so follow the below steps:

1. Change the initial value of 'largest_palindrome' [located on line 5] if need be. 
	(Ex: For finding a negative palindrome or the highest 2 digit palindrome.)

2. Change the value of 'i' and 'j' to the max value you want to multiply by.
I chose '999' for both because that is the highest 3 digit number.

3. Change the value 'i' and 'j' need to be greater than to the minimum number you want to multiply by.
I chose '100' for both because that is the lowest 3 digit number.

4. (Optional) Switch the values of 'i' and 'j' with what they cannot be less than, change '--' to '++',
Then change the greater than symbol to less than. You would do this to find the lowest X digit palindrome faster.
I provided an example below (Which could be used for this problem):

for (int i = 100; i < 1000; i++)
{
	for (int j = 100; j < 1000; j++)
	{ ... 
*/
