import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.UUID;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int testLength = Integer.parseInt(st.nextToken()), testNum = Integer.parseInt(st.nextToken());
        str = br.readLine();
        st = new StringTokenizer(str);
        var arr = new int[testLength];
        for (int i = 0; i < testLength; i++) arr[i] = Integer.parseInt(st.nextToken());
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
