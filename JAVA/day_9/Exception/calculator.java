package Exception;


class myException extends Exception{  
	 myException(String s){  
	  super(s);  
	 }  
	}  


public class calculator {
	static int caldouble(int value)throws myException{
		if (value<0) {
			throw new myException("negative numbers not allowed ");
		}
		else if (value==0){
			throw new myException("zero is not allowed");
		}
		else {
			throw new myException("always welcome for  positive");
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		try {
			caldouble(-3);
		}
		catch(Exception e)
		{
		System.out.println(e);	
		}

	}

}
