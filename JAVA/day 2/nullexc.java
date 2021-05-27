class abc{
    void display(){

    System.out.println("fjaklds"); }
   
}

class nullexc{
    public static void main(String args[]){
        abc s1 = new abc();
        s1=null;
        s1.dispay();
    }
}