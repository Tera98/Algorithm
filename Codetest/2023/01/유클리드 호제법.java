import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        System.out.println(Solution.uclid(a,b));
    }
    static int uclid(int a, int b){
        if (a > b) {
            return a % b != 0 ? uclid(b, a % b) : b;
        }else{
            return b % a != 0 ? uclid(a, b % a) : a;
        }
    }     
}
