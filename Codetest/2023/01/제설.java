import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int[] array = new int[4];
        for (int i = 0; i < 4; i++) array[i] = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (Math.min(array[0], array[2]) <= i + 1 && Math.max(array[0], array[2]) >= i + 1 &&
                Math.min(array[1], array[3]) <= j + 1 && Math.max(array[1], array[3]) >= j + 1) {
                    bw.write(".");
                    bw.flush();
                } else {
                    bw.write("*");
                    bw.flush();
                }
            }
            bw.write("\n");
            bw.flush();
        }
        bw.close();
    }
}
