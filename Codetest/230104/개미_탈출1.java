import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        int char_num = a.length() - a.replace("#", "").length();
        
        if(char_num>1){
            System.out.println("HELP!");
        } else{
            System.out.println("HAHA!");
        }
    }
}
