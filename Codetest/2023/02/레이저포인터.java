import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        var bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int Ax = Integer.parseInt(st.nextToken());
        int Ay = Integer.parseInt(st.nextToken());
        int Bx = Integer.parseInt(st.nextToken());
        int By = Integer.parseInt(st.nextToken());
        if(Ax == Bx || Ay == By) bw.write("0");
        else bw.write("1");
        bw.flush();
        bw.close();
    }
}
