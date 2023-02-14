import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        var br = new BufferedReader(new InputStreamReader(System.in));
        int a = Integer.parseInt(br.readLine());
        var stack = new Stack<>();
        for (int i = 0; i < a; i++) {
            var st = new StringTokenizer(br.readLine());
            String tmp = st.nextToken();
            if (tmp.equals("push")) stack.push(st.nextToken());
            else if (tmp.equals("pop")) {
                if (stack.isEmpty()) System.out.println(-1);
                else System.out.println(stack.pop());
            }
        }
    }
}
