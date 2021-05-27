
// 2) Define a class "MyClass" and make sure clients can instantiate it , 
// a) without any argument
// b) with one int argument
//c) with two int arguments


class myClass{
    
    myClass(){
        System.out.println("this is default constructor"); //print when object is instaniate
    }
    myClass(int num1){
         System.out.println("this is parameterize constructor with 1 argument"); //print when object is instaniate
        this.num1=num1;
                
    }

    private int num1;
    void setNum1(int num1){
        this.num1=num1;
    }
    int getNum1(){
        return num1;
    }

    myClass(int num2, int num3){
        System.out.println("this is parameterize constructor with 2 argument");//print when object is instaniate
        this.num2=num2;
        this.num3=num3;
    }
    private int num2;
    private int num3;
    void setNum2(int num2, int num3){
        this.num2=num2;
        this.num3=num3;
    }
    void getNum2(){
        
       System.out.println("one param= "+this.num2+"two param= "+this.num3);
    }
}
class construc{
    public static void main(String args[]){
        myClass s1= new myClass();
        myClass s2= new myClass(12);
        myClass s3= new myClass(11,12);
        System.out.println("one param= "+s2.getNum1());
         s3.getNum2();
    }
}


// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 2>javac construc.java

// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 2>java construc
// this is default constructor
// this is parameterize constructor with 1 argument
// this is parameterize constructor with 2 argument
// one param= 12
// one param= 11two param= 12
