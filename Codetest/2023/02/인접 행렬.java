import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        var st = new StringTokenizer(str);
        int matrixLength = Integer.parseInt(st.nextToken());
        int testNum = Integer.parseInt(st.nextToken());

        var arr = new int[matrixLength][matrixLength];
        for (int i = 0; i < testNum; i++) {
            str = br.readLine();
            st = new StringTokenizer(str);
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            if (arr[x][y] == 0) {
                arr[x][y] = 1;
                arr[y][x] = 1;
            }
        }
        for (int i = 0; i < matrixLength; i++) {
            for (int j = 0; j < matrixLength; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
    }
}
