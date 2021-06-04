package concepts;

public class items {
	String itemid;
	String name;
	int cost;
	public items(String itemid, String name, int cost) {
		this.itemid=itemid;
		this.name= name;
		this.cost=cost;
		
	}
	void display() {
		System.out.println("item name is "+this.itemid+ " name is  "+this.name+ "  cost is "+this.cost);
	}
	public static void main(String args[]) {
		//System.out.println("fdsf");
		items s1= new items("abc55","suraj",5355);
		s1.display();
		
	}

}
