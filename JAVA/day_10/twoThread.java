package threading;
class A {
	synchronized public void sync() throws Exception
	{
		for(int i=0;i<5;i++)
		{	
//			if(i==2) {
//				wait(); 
//				Thread.notify();
//			}
			System.out.println("synchonized "+i);
		}
	}
}
	

public class twoThread implements Runnable{
	 public void run()
	{
		for(int i=0;i<5;i++)
		{	
			System.out.println("thread "+i);
		}
	}


	public static void main(String[] args) throws Exception
	{ 
		// TODO Auto-generated method stub
		
A s1 = new A();
twoThread s2 = new twoThread();

//Thread obj = new Thread(s1);
Thread obj2 = new Thread(s2);
s1.sync();


obj2.start();

	}

}

