// Define 3 classes A , B and C
// in all these classes create static and nonstatic variables as well as methods.
// 	Now Define a class "Demo" ,in which define "main" function. From this main function try to access all the members of A ,B  and C.

class A{
    static int num1=40;
    int num2=2;
    static void display(){
     System.out.println("A class display");

}
}
class B{
    static int num1=10;
    int num2=23;
    static void display(){
     System.out.println("B class display");

}
}
class C{
    static int num1=20;
    int num2=11;
    static void display(){
     System.out.println("C class display");

}
}

class stat_nonstat{
    public static void main (String args[]){
        A s1=new A();
        B s2 = new B();
        C s3=new C();
        System.out.println(s1.num1);
        System.out.println(s1.num2);
        s1.display();

         System.out.println(s2.num1);
        System.out.println(s2.num2);
        s2.display();

         System.out.println(s3.num1);
        System.out.println(s3.num2);
        s3.display();

    }
}



// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 2>javac stat_nonstat.java

// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 2>java stat_nonstat
// 40
// 2
// A class display
// 10
// 23
// B class display
// 20
// 11
// C class display
