import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int t = sc.nextInt();
        
        for(int i = 0; i < t ; i++){
            
            int n = sc.nextInt();
            int m = sc.nextInt();
            String a = sc.next();
            
            int start = a.indexOf("@");
            int des = a.indexOf("O");
            int charNum = 0;
            
            if ((start - des) < 0 ){
                charNum = a.substring(start,des).length() - 
                a.substring(start,des).replace("#", "").length();
                
            }else{
                charNum = a.substring(des,start).length() - 
                a.substring(des,start).replace("#", "").length();
            }
            
            if(charNum>m){
                System.out.println("HELP!");
            }else{
                System.out.println("HAHA!");
            }
        }
    }
}
