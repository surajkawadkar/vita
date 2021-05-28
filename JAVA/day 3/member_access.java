// 1)	Define 2 classes “First” and “Second” with member variables , 
// member functions and constructors of  your choice. Now define a class “Two” in which define main function .
//In main function create various instances of First and Second  and call their individual member functions.
class first{
    int num;
    void  setNum(int num){
        this.num=num;

    }
    int getNum(){
        return this.num;
    }

}

class second{
    String name ;
    void  setName(String name){
        this.name=name;

    }
    String getName(){
        return this.name;
    }

}

class member_access{
    public static void main(String arg[]){
        first s1= new first();
        second s2= new second();
        s1.setNum(78);
        s2.setName("black");
        System.out.println(s1.getNum()+"and name is "+s2.getName());
    }
}


// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 3>javac member_access.java

// E:\Courses\VITA\VITA-PROGRAMS\JAVA\day 3>java member_access
// 78and name is black