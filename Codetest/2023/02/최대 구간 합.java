import java.io.*;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution {
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
        int size;
        if (testLength % 2 == 0) {
            size = (testLength + 1) * testLength / 2;
        } else {
            size = (testLength + 2) * (testLength + 1) / 2 - testLength - 1;
        }
        int[] output1 = new int[size];
        int count = 0;
        for (int i = 0; i < testLength; i++) {
            for (int j = 0; j <= i; j++) {
                output[count] += arr[j];
            }
            count += 1;
        }
        count = 0;
        for (int i = 0; i < testLength; i++) {
            for (int j = 0; j < testLength; j++) {
                if (i <= j) {
                    if (i == 0) {
                        output1[count] = output[j];
                    } else {
                        output1[count] = output[j] - output[i - 1];
                    }
                    count += 1;
                }
            }
        }
        bw.write(Arrays.stream(output1).max().getAsInt() + " ");
        bw.flush();
        bw.close();
    }
}
