class saving_account{
    int accid;
    String name;
    double balance;
    final int rate=8; //static mmner ot class variable if static changes to final cannot change firther

    void setAccid(int accid){
        this.accid=accid;
    }
    int accid(){
        return accid;
    }
    void setName(String name){
        this.name=name;
    }
    String getName(){
        return name;
    }
    void setBalance(double balance){
        this.balance=balance;
    }
    double getBalance(){
        return balance;
    }
}
class methodoverloading{
    public static void main(String args[]){
        saving_account s1= new saving_account();
         s1.setAccid(123456);
         s1.setName("suraj");
        s1.setBalance(1235.12);
        s1.getName();
        s1.getBalance();
        s1.getName();

      
        System.out.println(s1.getName()+"\t"+s1.getBalance()+"\t"+s1.accid());

    }
}