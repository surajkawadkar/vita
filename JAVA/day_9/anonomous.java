class A{
    void display(){
        System.out.println("class a display");
    }
}

class anonomous{
    public static void main(String[] args){
        
        A ob =new A()
        {                    //anonomous class implementation 
                    void display(){
                        System.out.println("anonomous class display");
                    }
        }; //anonomous class implemetation end
        ob.display();  //call method using object
    }
}