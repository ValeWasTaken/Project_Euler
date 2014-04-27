public class Project_Euler_Problem_006
{
	public static void main(String args[])
	{
		// Start of "Square of sums" block
		int n = 0;
		for (int x = 0; x < 101; x++)
		{
			n += x;
		}
		int final_num = n*n;
		System.out.println("The square of the sum of the first 100 natural numbers is: " + final_num); // Expected output: 25502500
		
		// Start of "Sum of squares" block
		int num = 0;
		for (int y = 0; y < 101; y++)
		{
			num += (y*y);
		}
		System.out.println("The sum of the squares of the first 100 natural numbers is: " + num); // Expected output: 338350
		
		// Final calculation
		int difference = final_num - num;
		System.out.println("The difference between the two sums is: " + difference); // Expected output: 25164150
	}
}
