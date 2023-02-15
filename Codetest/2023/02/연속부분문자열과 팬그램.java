import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        str = str.toLowerCase(Locale.ROOT);
        int testNum = Integer.parseInt(br.readLine());
        String output = "";
        for (int i = 0; i < testNum; i++) {
            String testStr = br.readLine();
            var st = new StringTokenizer(testStr);
            int a = Integer.parseInt(st.nextToken()), b= Integer.parseInt(st.nextToken());
            output += panGram(str.substring(a-1,b));
        }
        System.out.println(output);
    }

    public static int panGram(String str){
        List<Integer> arr = new ArrayList<>();
        for (int i = 0; i < str.length(); i++) {
            arr.add(str.codePointAt(i));
        }
        int output = 1;
        for (int i = 97; i < 123; i++) {
            if(!arr.contains(i)){
                output = 0;
            }
        }
        return output;
    }
}
