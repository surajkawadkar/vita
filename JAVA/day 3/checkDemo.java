/*
3)	Define a class “Check” in which declare member variables using  different
 accessibility modifiers i.e.  <default>, private ,public and protected. 
   Define a function “disp”  which should be public.
     Define a class “CheckDemo” in which you will write “main()” function.
      Create an instance of  the class “Check” and  show how many
  variables can be accessed directly and how many indirectly



*/
class check{
int num1=10; //default
private int num2=20;//private
public int num3=30; //public
protected int num4=40; //protected
public void disp(){
    System.out .println(num1);
    System.out .println(num2);
    System.out .println(num3);
    System.out .println(num4);
}
}






class checkDemo{
    public static void main(String args[]){
        check s1 = new check();
        System.out.println(s1.num1);
        //System.out.println(s1.num2); direct cannot access because or private modifier 
        System.out.println(s1.num3);
        System.out.println(s1.num4);
        System.out.println("disp method");

    s1.disp();
    }
}


// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 3>javac checkDemo.java

// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 3>java checkDemo
// 10
// 30
// 40
// disp method
// 10
// 20
// 30
// 40