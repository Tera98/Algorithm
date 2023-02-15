import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int A = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());
        int sum = A + B;
        int max = Math.max(A, B);
        if (sum % 2 == 0) {
            bw.write("0" + " " + (max - sum / 2));
            bw.flush();
        } else {
            bw.write("1" + " " + (max - sum / 2 - 1));
            bw.flush();
        }
        bw.close();
    }
}
