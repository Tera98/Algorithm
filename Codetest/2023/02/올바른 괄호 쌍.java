import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        var stack = new Stack<>();
        String output = "YES";
        for (int i = 0; i < str.length(); i++) {
            if (str.charAt(i) == '(') {
                stack.push(1);
            } else if (str.charAt(i) == ')') {
                if (!stack.isEmpty()) {
                    stack.pop();
                } else output = "NO";
            }
        }
        if (!stack.isEmpty()) output = "NO";
        System.out.println(output);
    }
}
