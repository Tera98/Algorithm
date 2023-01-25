import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int[] array = new int[n];
        String[] output = new String[n];
        //substring 해서 sort 하고 이진탐색하면 조금더 빨라질까?
        for (int i = 0; i < n; i++) array[i] = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) if (array[i] > array[j]) count += 1;
            output[i] = count + " " + (n - 1 - count) + "\n";
        }

        for (int i = 0; i < n; i++) {
            bw.write(output[i]);
            bw.flush();
        }
        bw.close();
    }
}
