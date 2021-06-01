package logicalQ;
import java.util.Scanner;
public class checkVowel {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		char ch;
		System.out.println("ehter the chaaracter");
		Scanner sc =new Scanner(System.in);
		ch =sc.nextLine().charAt(0);
		if (ch=='u'||ch=='o'||ch=='i'||ch=='e'||ch=='a') {
			System.out.println("Vowel");
		}
		else {
			System.out.println("consonant");
		}
	}

}
