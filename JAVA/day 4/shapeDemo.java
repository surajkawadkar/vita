package oops;
class shape{
	void draw() {
		System.out.println("shpae class");
		
	}
}

class circle extends shape{
	void draw() {
		System.out.println("shpae circle");
	}
}

class rectangle extends shape{
	void draw() {
		System.out.println("shpae rectangle");
	}
}

class polygon extends shape{
	void draw() {
		System.out.println("shpae polygon");
	}
}
public class shapeDemo {
	
	static void perform(shape ref) {
		ref.draw();
	}
	
	public static void main(String[] args) {
		perform(new circle());
		perform(new rectangle());
		perform(new polygon());

	}
}
