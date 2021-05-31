package oops;
class parent{
	void display() {
		System.out.println("parent class");
	}
	
}

class child extends parent{
	int num;
	void display(int k) {
		num=k;
		System.out.println(num);
	}
	
}
public class inheritance_overloading {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		child s1 = new child();
		s1.display();
		s1.display(5);
	}

}
