class Student{
    String name="suraj";
    int age;
    void setName(String str)  //STR IS   A LOCAL MEMBER
	{
		name=str;
	}
   String getName(){
    return name;
}
}


class demo{
    public static void main(String args[]){
        Student s =new Student();
        s.setName("suraj");
        System.out.println(s.getName());
        

    }
}