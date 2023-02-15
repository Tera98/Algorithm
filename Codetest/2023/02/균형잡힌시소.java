import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int testLength = Integer.parseInt(st.nextToken());
        var arr = new int[testLength + 1];
        str = br.readLine();
        st = new StringTokenizer(str);
        for (int i = 0; i < testLength; i++) arr[i] = Integer.parseInt(st.nextToken());
        var sum = new int[testLength + 1];
        sum[0] = 0;
        for (int i = 1; i <= testLength; i++) {
            sum[i] = sum[i - 1] + arr[i - 1];
        }
        boolean output = false;
        for (int i = 1; i <= testLength; i++) {
            int sumLeft = sum[i - 1];
            int sumRight = sum[testLength] - sum[i];
            if (sumLeft == sumRight) {
                System.out.println(i);
                output = true;
            }
        }
        if (!output) {
            System.out.println(-1);
        }
    }
}
