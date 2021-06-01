package logicalQ;
import java.util.Scanner; 

class marks{
	
	void studentGrade(int marks) {
		if (marks>75) {
			System.out.println("Distinction");
		}
		else if(marks>=60 && marks<=75) {
			System.out.println("First class");
		}
		else if(marks>=45 && marks<60) {
			System.out.println("Second class");
		}
		else if (marks >= 35 && marks<45) {
			System.out.println("pass class");
		}
		else {
			System.out.println("Fail");
		}
		
	}
	
	
}
public class grade {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		System.out.println("Enter the marks");
		Scanner sc = new Scanner(System.in);
		int marks;
		marks=sc.nextInt();
		
		marks s1 = new marks();
		s1.studentGrade(marks);
	}

}
