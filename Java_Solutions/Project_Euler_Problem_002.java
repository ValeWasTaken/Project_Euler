public class Project_Euler_Problem_002 {
	public static void main(String args[]){
		int a = 0, b = 1, c = 0, d = 0;
		while (c < 3500000)
		{
			c = a + b;
			a = b;
			b = c;
			if (c % 2 == 0)
			{
				d += c;
			}
		}
		System.out.println("The sum of all EVEN fibonacci values under 4 million is: " + d);
	}
}
