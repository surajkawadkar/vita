
// 3) Define a class "Emp" with private static member "int cnt".
// How will u make sure that outsiders can read the value of cnt ?

class static_cnt{
    private static int cnt=89;

    public static void main(String[] args){
        //cnt=99;   this also work
        System.out.println(cnt);
    }
}