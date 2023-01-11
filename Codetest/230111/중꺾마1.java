import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int testNum = sc.nextInt();

        for (int i = 0; i < testNum; i++) {

            int nDays = sc.nextInt();
            int money = sc.nextInt();
            int kDay = sc.nextInt();
            ArrayList<Integer> list = new ArrayList<Integer>();
            int day = 0;
            for (int j = 0; j < nDays; j++) list.add(sc.nextInt());
            int j = kDay;
            while (j <= nDays) {
                if (list.get(j - 1) - list.get(kDay - 1) >= money) {
                    day = j;
                    break;
                }
                j++;
            }
            System.out.println(day != 0 ? day : "JB");
        }
    }
}
