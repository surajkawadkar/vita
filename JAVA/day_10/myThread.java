package threading;

class child extends Thread{
	public void run() {
		for(int i =1;i<=5;i++) {
			System.out.println("child thread"+i);
		}
	}
}
public class myThread extends Thread{ //we can extends child class instead of Thread because child class extending thread 

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		//myThread s1 = new myThread();
		child s2= new child();
		s2.start();
		for(int i =1;i<=5;i++) {
			System.out.println("main thread"+i);
		}
		
		//s1.start();
	}

}
