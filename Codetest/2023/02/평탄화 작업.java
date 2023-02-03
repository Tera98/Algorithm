import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        String str = br.readLine();
        var st = new StringTokenizer(str);
        var arr = new ArrayList<Integer>();
        for (int i = 0; i < n; i++) arr.add(Integer.parseInt(st.nextToken()));
        int min = Collections.min(arr);
        int output = 0;
        for (int i = 0; i < n; i++) output += arr.get(i) - min;

        bw.write(output+"");
        bw.flush();
        bw.close();
    }
}
