package logicalQ;
import java.util.Scanner;
public class searchArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int size,flag=0;
		int num,i, check;
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter the size of an array");
		size = sc.nextInt();
		
		
		int arr[];
		arr= new int[size];
		System.out.println("enter"+size+"elemets in array");
		for (i =0;i<arr.length;i++) {
			num= sc.nextInt();
			arr[i]=num;
		}
		System.out.println("Enter the number to be checked");
		check= sc.nextInt();
		
		for (i=0;i<arr.length;i++) {
			if (check==arr[i]) {
				flag=1;
				
			}
			else {
				
				
			}
		}
		if (flag==1) {
			System.out.println("it is present in an arry");
		}
		else {
			System.out.println("Not found");
		}
	}

}
