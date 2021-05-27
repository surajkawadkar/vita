//1)create a class "Shape" with 2 attributes, "width" and "height". Make sure one can not access these attributes directly.
//provide accessor methods on these attributes and allow them to call from outside of your class.
class shape_w_h{
    int height;
    int width;
    void setWidth(int width){
    this.width=width;
    }

    void setHeight(int height){
    this.height=height;
    }
    int getWidth(){
        return this.width;
    }

    int getHeight(){
        return this.height;
    }
    
}


class shape{  //main class
    public static void main(String args[]){  //main method
    shape_w_h s1 = new shape_w_h();
    s1.setWidth(23);
    s1.setHeight(5);
    System.out.println("width is "+s1.getWidth()+"height is "+s1.getHeight());

    }
}