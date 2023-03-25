import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String[] songName = new String[n];
        int[] songLength = new int[n];
        int time = 0;
        for (int i = 0; i < n; i++) songName[i] = br.readLine();
        for (int i = 0; i < n; i++) {
            time += Integer.parseInt(br.readLine());
            songLength[i] = time;
        }
        int songNum = Integer.parseInt(br.readLine());

        int i = 0, j = 0;
        while (i < songNum) {
            time = Integer.parseInt(br.readLine());
            while (time > songLength[n - 1]) {
                time -= songLength[n - 1];
                j = 0;
            }
            while (true) {
                if (time <= songLength[j]) {
                    bw.write(songName[j] + "\n");
                    bw.flush();
                    i++;
                    break;
                } else j++;
            }
        }
        bw.close();
    }
}
