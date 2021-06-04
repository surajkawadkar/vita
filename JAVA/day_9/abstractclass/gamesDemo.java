package abstractclass;

abstract class games{
	
	abstract void play();
	}

 class football extends games{
	
	 void play() {
		 System.out.println("inside football class --> CR7");
	 }
	}

 class cricket extends games{
	
	 void play() {
		 System.out.println("inside cricket class --> VK");
	 }
	}

 class tennis extends games{
	
	 void play() {
		 System.out.println("inside tennis class  --> rafael nadal");
	 }
	}


public abstract class gamesDemo {
	static void perform(games ref) {
		ref.play();
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		games arr[];
		int i;
		arr = new games[3];
		arr[0]=new football();
		arr[1]=new cricket();
		arr[2]= new tennis();
		
		for (i=0;i<arr.length;i++) {
			if (arr[i] instanceof cricket) {
				arr[i].play();
				
			}
		}
	}

}
