package threading;
class AB extends Thread{
	char alph;
	synchronized public void run() //throws Exception
	{
		for(char i=65;i<75;i++)
		{	
			alph=i;
			System.out.println("synchonized "+alph);
		}
	}
}
	

public class rantalLock extends Thread{
	
	 public void run()
	{
		 char alph;
		for(char i=65;i<75;i++)
		{	
			alph=i;
			System.out.println("thread "+ alph);
		}
	}


	public static void main(String[] args) throws Exception
	{ 
		// TODO Auto-generated method stub
		
AB s1 = new AB();
rantalLock s2 = new rantalLock();

//Thread obj = new Thread(s1);
//Thread obj2 = new Thread(s2);
s1.start();


s2.start();

	}

}

