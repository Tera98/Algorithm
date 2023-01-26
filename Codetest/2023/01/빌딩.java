import java.io.*;
import java.util.Arrays;
import java.util.OptionalInt;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        int[] array = new int[n];
        for (int i = 0; i < n; i++) array[i] = Integer.parseInt(st.nextToken());
        int leftCount = 0, leftHeight = 0, rightCount = 0, rightHeight = 0;
        OptionalInt max = Arrays.stream(array).max();

        for (int i = 0; i < n; i++) {
            if (leftHeight < array[i]) {
                leftHeight = array[i];
                leftCount += 1;
            }
            if(leftHeight == max.getAsInt()) break;
        }
        for (int i = n - 1; i >= 0; i--) {
            if (rightHeight < array[i]) {
                rightHeight = array[i];
                rightCount += 1;
            }
            if(rightHeight == max.getAsInt()) break;
        }
        bw.write(leftCount + " " + rightCount);
        bw.flush();
        bw.close();
    }
}
