import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int[] songLength = new int[n];
        int time = 0;
        for (int i = 0; i < n; i++) {
            time += Integer.parseInt(st.nextToken());
            songLength[i] = time;
        }
        int testNum = Integer.parseInt(br.readLine());
        str = br.readLine();
        st = new StringTokenizer(str);

        int i = 0, j = 0, output = 0;
        while (i < testNum) {
            time = Integer.parseInt(st.nextToken());
            while (time > songLength[n - 1]) {
                time -= songLength[n - 1];
                j = 0;
            }
            while (true) {
                if (time <= songLength[j]) {
                    output = (output + (j + 1)) % 1000000007;
                    i++;
                    break;
                } else j++;
            }
        }
        System.out.println(output);
    }
}
