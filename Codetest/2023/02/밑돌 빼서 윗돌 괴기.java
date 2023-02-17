import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int testLength = Integer.parseInt(st.nextToken());
        int testNum = Integer.parseInt(st.nextToken());
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 0; i < testLength; i++) queue.offer(i + 1);
        for (int i = 0; i < testNum; i++) {
            str = br.readLine();
            if (str.charAt(0) == 'r') queue.offer(queue.poll());
            else if (str.charAt(0) == 'd' && queue.size() > 1) queue.poll();
        }
        System.out.println(queue.peek());
    }
}
