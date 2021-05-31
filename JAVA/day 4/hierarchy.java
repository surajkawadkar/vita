package oops;
class mobile{
	mobile(){
		System.out.println("mobile main class construcctor invoked");
	}
	void mobMethod() {
		System.out.println("\"base class method invoked");
		
	}
}

class samsung extends mobile{
	samsung(){
		System.out.println("samsumg logo");
	}
	void samsungMethod() {
		System.out.println("samsung features");
	}
}

class apple extends mobile{
	apple(){
		System.out.println("apple logo");
	}
	void appleMethod() {
		System.out.println("apple features");
	}
}
public class hierarchy {

	

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		apple s1 =new apple();
		samsung s2 = new samsung();
		s1.appleMethod();
		s2.samsungMethod();
	}

}
