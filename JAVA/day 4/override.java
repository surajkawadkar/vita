package oops;
class base{
	void display() { 
		System.out.println("overridden method also known as parent method");
	}
}
class subClass extends base{
	void display() {
		System.out.println("ocerridding method ....child's class method");
	}
}
public class override {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		base s1 = new subClass();
		s1.display();

	}

}
