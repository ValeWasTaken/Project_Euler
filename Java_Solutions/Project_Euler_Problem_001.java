public class Project_Euler_Problem_001 {
	public static void main(String args[]){
		int answer = 0;
		for (int x=0; x<1000; x++)
		{
			if (x % 5 == 0 || x % 3 == 0)
			{
				answer += x;
			}
		}
		System.out.println("The sum of all multiples of 3 and 5 is " + answer + ".\n\n"); // answer should be 233168.
	}
}
