import java.util.ArrayList;
import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int t = sc.nextInt();

        for (int i = 0; i < t; i++) {

            int n = sc.nextInt();       int m = sc.nextInt();
            String a = sc.next();
            int atkJ = sc.nextInt();    int hpJ = sc.nextInt();
            int atkM = sc.nextInt();    int hpM = sc.nextInt();

            int start = a.indexOf("@"); int monster = a.indexOf("&");
            int wallNum = 0, output = 0;
            ArrayList<Integer> list = new ArrayList<>();

            int index = a.indexOf("O");
            while (index != -1) {
                list.add(index);
                index = a.indexOf("O", index + 1);
            }

            boolean killed = true;

            while (hpM > 0) {
                if (hpM <= atkJ) {
                    hpM = 0;
                } else {
                    hpM -= atkJ;
                    hpJ -= atkM;
                }
                if (hpJ <= 0) {
                    killed = false;
                }
            }

            for (Integer integer : list) {

                if ((start - integer) <= 0) {
                    wallNum = a.substring(start, integer).length() -
                            a.substring(start, integer).replace("#", "").length();
                } else {
                    wallNum = a.substring(integer, start).length() -
                            a.substring(integer, start).replace("#", "").length();
                }

                if ((monster < start && monster > integer) || (monster > start && monster < integer)) {
                    if (wallNum <= m && killed) output += 1;
                } else {
                    if (wallNum <= m) output += 1;
                }
            }

            if (output > 0) {
                System.out.println("HAHA!");
            } else {
                System.out.println("HELP!");
            }
        }
    }
}


