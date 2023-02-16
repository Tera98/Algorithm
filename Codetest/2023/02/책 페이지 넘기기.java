import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        int testNum = Integer.parseInt(br.readLine());
        var stackA = new Stack<>();
        var stackB = new Stack<>();
        for (int i = (str.length() - 1); i >= 1; i--) stackB.push(str.charAt(i));
        stackA.push(str.charAt(0));
        char left = str.charAt(0);
        char right = str.charAt(str.length() - 1);
        String output = "";

        for (int i = 0; i < testNum; i++) {

            String testStr = br.readLine();

            if (testStr.charAt(0) == 'm') {
                if (testStr.charAt(5) == 'l' && stackA.size() > 1) {
                    stackB.push(stackA.pop());
                } else if (testStr.charAt(5) == 'r' && stackB.size() > 1) {
                    stackA.push(stackB.pop());
                }
            } else {
                if (testStr.charAt(5) == 'l' && stackA.size() > 1) {
                    stackA.pop();
                } else if (testStr.charAt(5) == 'r' && stackB.size() > 1) {
                    stackB.pop();
                }
            }
        }
        System.out.println(stackA.pop() + " " + stackB.pop());
    }
}
