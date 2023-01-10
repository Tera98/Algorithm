import java.util.Scanner;   // 시간 복잡도를 줄여야 함

public class Solution {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int testNum = sc.nextInt();

        for (int i = 0; i < testNum; i++) {

            int lenString = sc.nextInt();
            int tryCount = sc.nextInt();
            String str = sc.next();
            int result = 0;
            
            for (int j = 0; j < tryCount; j++) {

                int index1 = sc.nextInt();
                int index2 = sc.nextInt();
                String targetStr = str.substring(index1 - 1, index2);
                boolean output = false;
                int k = 1, count = 0;

                if (targetStr.charAt(0) == 'U') output = true;

                while (k < targetStr.length() && output) {
                    if (targetStr.charAt(k) != 'm') {
                        output = false;
                    } else count += 1;
                    k++;
                }
                
                if(output && count >= 2){
                    result += 1;
                }
            }
            System.out.println(result);
        }
    }
}
