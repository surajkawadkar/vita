package logicalQ;
import java.util.Scanner;
public class divisible {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int num;
		System.out.println("Enter the number");
		Scanner sc = new Scanner(System.in);
		num=sc.nextInt();
		if (num%7==0) {
			System.out.println("divisibe by 7");
		}
		else {
			System.out.println("not divisible by 7");
		}
	}

}
