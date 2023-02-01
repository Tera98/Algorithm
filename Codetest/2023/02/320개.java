import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        var st = new StringTokenizer(str);
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < n; i++) arr.add(Math.abs(Integer.parseInt(st.nextToken()) - 320));
        bw.write(arr.indexOf(Collections.min(arr)) + 1 + "");
        bw.flush();
        bw.close();
    }
}
