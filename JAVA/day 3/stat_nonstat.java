// 2)	Create a class with static and non-static member variables.
//  Define static and non-static member functions. Create instance of 
//  this class and call both static and non-static member functions

class A{
    static int num=20;
    int num2=10;
    static void display(){

        System.out.println("static function ");
    }

    void display2(){
        System.out.println("non static function ");
    }
}

class stat_nonstat{
    public static void main(String args[]){
        A s1 =new A(); //create instance of class
        System.out.println(A.num); //called static instance variable using class.variable
        A.display(); //use class name to call static method
        System.out.println(s1.num2); //use referemce to call non static  variable
        s1.display2(); //use ref to call nonstatic method
        
    }
}


// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 3>javac stat_nonstat.java

// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 3>java stat_nonstat
// 20
// static function
// 10
// non static function