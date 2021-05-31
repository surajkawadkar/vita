class prime{
public static void main(String args[]){
int num=20;
int i=2;
int flag=0;
while(num>=i){
	if (num%i/2==0){
		flag=0;
	}
	else{
		flag=1;
	}
	i+=1;
	}
	if(flag==1){
		System.out.println(" prime number");
	}
	else{
		System.out.println(" not a prime number");
	}

}
}