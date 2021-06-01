package logicalQ;
import java.util.Scanner;
public class sumArray {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int i,num,size;
		int sum=0;
		Scanner sc = new Scanner(System.in);
		System.out.println("enter size of an array");
		size= sc.nextInt();
		int arr[];
		System.out.println("enter elements of an array");
		arr =new int[size];
		for (i=0;i<arr.length;i++) {
			num=sc.nextInt();
			arr[i]=num;
		}
		
		for (i=0;i<arr.length;i++) {
			sum+=arr[i];
		}
		System.out.println("Sum is "+sum);
		
		
		
		
	}

}
