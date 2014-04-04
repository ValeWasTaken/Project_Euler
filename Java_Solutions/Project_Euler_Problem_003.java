public class Project_Euler_Problem_003
{
	public static void main(String args[])
	{
		long num = 600851475143L;
		int x = 2;
		
		while (x*x < num)
		{
			while (num % x == 0)
			{
				num = num / x;
			}
			x++;
		}
		System.out.print(num);
	}
}
