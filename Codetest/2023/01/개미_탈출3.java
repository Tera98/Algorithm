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
            int infi = a.indexOf("G");
            int charNum1, charNum2, charNum = 0;
            
        
            if ((start - des) < 0 ){
                charNum1 = a.substring(start,des).length() - 
                a.substring(start,des).replace("#", "").length();
                
            }else{
                charNum1 = a.substring(des,start).length() - 
                a.substring(des,start).replace("#", "").length();
            }
            
            if ((start - infi) < 0 ){
                charNum2 = a.substring(start,infi).length() - 
                a.substring(start,infi).replace("#", "").length();
                
            }else{
                charNum2 = a.substring(infi,start).length() - 
                a.substring(infi,start).replace("#", "").length();
            }
            
            charNum = charNum1 < charNum2 ? charNum1 : charNum2;
            
            if(charNum>m){
                System.out.println("HELP!");
            }else{
                System.out.println("HAHA!");
            }
        }
    }
}
