import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name1 = sc.next();
        int a = sc.nextInt();
        String name2 = sc.next();
        int b = sc.nextInt();

        System.out.println(a > b ? name1 : name2);
    }
}
