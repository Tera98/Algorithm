import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int testNum = sc.nextInt();

        for (int i = 0; i < testNum; i++) {
            int lenString = sc.nextInt();
            String str = sc.next();
            int index1 = sc.nextInt();
            int index2 = sc.nextInt();
            String targetStr = str.substring(index1 - 1, index2);
            boolean output = false;
            int count = 0;
            if (targetStr.charAt(0) == 'U') output = true;

            for (int j = 1; j < targetStr.length(); j++) {
                if (targetStr.charAt(j) != 'm') output = false;
                else count += 1;
            }

            System.out.println(output && count >= 2 ? "YES" : "NO");

        }

    }
}
