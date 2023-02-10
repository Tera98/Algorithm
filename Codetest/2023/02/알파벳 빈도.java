import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int testLength = Integer.parseInt(st.nextToken()), testNum = Integer.parseInt(st.nextToken());
        str = br.readLine();
        var arr = new int[testLength];
        for (int i = 0; i < testLength; i++) {
            if (str.charAt(i) == 'e') {
                arr[i] = 1;
            } else {
                arr[i] = 0;
            }
        }
        int[] output = new int[testNum];
        int count = 0;
        for (int i = 0; i < testNum; i++) {
            str = br.readLine();
            st = new StringTokenizer(str);
            int startIndex = Integer.parseInt(st.nextToken()), finIndex = Integer.parseInt(st.nextToken());
            for (int j = startIndex; j <= finIndex; j++) output[count] += arr[j - 1];
            count += 1;
        }
        for (int i = 0; i < testNum; i++) {
            bw.write(output[i] + "\n");
            bw.flush();
        }
        bw.close();
    }
}
