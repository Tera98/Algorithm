import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        int charNum = a.length() - a.replace("#", "").length();
        
        if(charNum>1){
            System.out.println("HELP!");
        } else{
            System.out.println("HAHA!");
        }
    }
}
