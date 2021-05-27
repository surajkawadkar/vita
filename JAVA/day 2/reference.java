//  Define a class "DemoOb". 
// create an instance of it.
// now create a reference and assign the reference created in the above statement.
// 	Discuss what happens?
// Now since u have 2 references, take one of the reference and assign a new instance of the class.
// 	Discuss what happens?
// (For ur discussion, write necessary comments in the program)

class demoOb{
    void display(){ //member function
        System.out.println("this is display1 class");
    }
    void display2(){
        System.out.println("this is display2 class");
    }
    
}

class reference{
    public static void main(String[] args){
        demoOb s1=new demoOb(); //crete a instancec of demoonb class
        demoOb s2=s1;
        s1.display();
        s2.display();   
        s1.display2();
        s2.display2(); 

    }

}



// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 2>javac reference.java

// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 2>java  reference
// this is display1 class
// this is display1 class
// this is display2 class
// this is display2 class
