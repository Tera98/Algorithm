import java.io.*;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String str = br.readLine();
        StringTokenizer st = new StringTokenizer(str);
        String a = st.nextToken();
        String b = st.nextToken();

        for (int i = 0; i < a.length(); i++) {
            String tmp = a.substring(i,i+1);
            b = b.replace(tmp,"");
        }
        if(b.length() == 0){
            bw.write("True\n");
            bw.flush();
        }else{
            bw.write("False\n");
            bw.flush();    
        }
        bw.close();
    }
}
