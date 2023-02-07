import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int testLength = Integer.parseInt(st.nextToken());
        str = br.readLine();
        st = new StringTokenizer(str);
        var arr = new int[testLength];
        for (int i = 0; i < testLength; i++) arr[i] = Integer.parseInt(st.nextToken());
        int[] output = new int[testLength];
        int count = 0;
        for (int i = 0; i < testLength; i++) {
            for (int j = 0; j <= i; j++) {
                output[count] += arr[j];
            }
            count += 1;
        }
        for (int i = 0; i < testLength; i++) {
            bw.write(output[i] + " ");
            bw.flush();
        }
        bw.close();
    }
}
