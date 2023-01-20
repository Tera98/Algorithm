import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter((System.out)));
        String input = br.readLine();
        int count = 0;
        for (int i = 0; i < input.length(); i++) {
            String subInput = input.substring(i);
            if (subInput.charAt(0) == '0') count += 1;
        }
        if (count == 4) {
            bw.write(5 + "\n");
            bw.flush();
        } else {
            bw.write((4 - count) + "");
            bw.flush();
        }
        bw.close();
    }
}
