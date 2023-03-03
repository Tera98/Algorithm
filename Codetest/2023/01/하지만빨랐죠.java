import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int tmp = 1;
            
//            double max = Math.min(a, b);
//            max = Math.sqrt(max);
//            if(a==b) tmp = a;
//
//            for (int j = 1; j <= max; j++) {
//                if (a % j == 0 && b % j == 0) {
//                    tmp = Math.max(tmp, j);
//                }
//            }

            tmp = Solution.uclid(a, b);

            if (tmp == 1) {
                bw.write("Perfect\n");
                bw.flush();
            } else {
                bw.write("Not even close\n");
                bw.flush();
            }
        }
        bw.close();
    }

    static int uclid(int a, int b) {
        if (a > b) {
            return a % b != 0 ? uclid(b, a % b) : b;
        } else {
            return b % a != 0 ? uclid(a, b % a) : a;
        }
    }
}
