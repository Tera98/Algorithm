import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int testLength = Integer.parseInt(st.nextToken());
        int testNum = Integer.parseInt(st.nextToken());
        var arr = new int[testLength];
        for (int i = 0; i < testLength; i++) arr[i] = i + 1;
        for (int i = 0; i < testNum; i++) {
            str = br.readLine();
            st = new StringTokenizer(str);
            int a = Integer.parseInt(st.nextToken()) - 1, b = Integer.parseInt(st.nextToken()) - 1;
            int tmp = 0;
            tmp = arr[a];
            arr[a] = arr[b];
            arr[b] = tmp;
        }
        for (int i = 0; i < testLength; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
