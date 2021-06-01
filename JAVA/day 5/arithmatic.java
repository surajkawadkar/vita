package logicalQ;
import java.util.Scanner;
public class arithmatic {

	public static void main(String[] args) {
		char ch;
		double ans ;
		int  num1 ,num2;
		// TODO Auto-generated method stub
		Scanner sc =new Scanner(System.in);
		
		 System.out.println("enter the operator to be performerd");
		 ch = sc.nextLine().charAt(0);
		 System.out.println("enter 2 numbers");
		 num1 = sc.nextInt();
		 num2 = sc.nextInt();
		 
		 switch(ch) {
		 case '+':{
			ans= num1+num2;
					System.out.println("addition is "+ans);
					break;
		 }
		 case '-':{
				ans= num1-num2;
						System.out.println("subtraction is "+ans);
						break;
			 }
		 case '*':{
				ans= num1*num2;
						System.out.println("multiplication is "+ans);
						break;
			 }
		 case '%':{
				ans= num1%num2;
						System.out.println( "modulo is "+ans);
						break;
			 }
		 case '/':{
				ans= num1/(double)num2;
						System.out.println("division is "+ans);
						break;
			 }
		 default:
			 System.out.println("invalid operator  please check your eyes ");
			 
		 
		 }
		
		
	}

}
