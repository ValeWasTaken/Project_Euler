public class Project_Euler_Problem_005 
{
	public static void main(String args[])
	{
		int num = 1;
		boolean solutionFound = false;
		
		while(!solutionFound)
		{
			int count = 0;
			for(int x = 1; x < 21; x++)
			{
				if(num % x != 0)
				{
					count += 1;
					break;
				}
			}
			if(count == 0)
			{
				System.out.println("Smallest multiple is " + num);
				solutionFound = true;
			}
			num++;
		}
	}
}
