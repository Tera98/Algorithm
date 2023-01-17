import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int t = Integer.parseInt(br.readLine());
        List<String> output = new ArrayList<>();

        for (int i = 0; i < t; i++) {

            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            List<String> list = new ArrayList<>();
            for (int j = 0; j < n; j++) list.add(br.readLine());
            int k = Integer.parseInt(br.readLine());
            String input = br.readLine();
            int startX = 0, startY = 0, lossHp = 0;

            for (int j = 0; j < n; j++) {
                if (list.get(j).contains("@")) {
                    startX = list.get(j).indexOf("@") + 1;
                    startY = j + 1;
                }
            }
            for (int j = 0; j < k; j++) {
                if (input.charAt(j) == 'L' && startX > 1) {
                    if (list.get(startY - 1).charAt(startX - 2) == '#' && list.get(startY - 1).charAt(startX - 1) == '^') {
                        lossHp += 1;
                    } else if (list.get(startY - 1).charAt(startX - 2) == '^') {
                        lossHp += 1;
                        startX -= 1;
                    } else if (list.get(startY - 1).charAt(startX - 2) != '#') {
                        startX -= 1;
                    }
                } else if (input.charAt(j) == 'R' && startX < m) {
                    if (list.get(startY - 1).charAt(startX) == '#' && list.get(startY - 1).charAt(startX - 1) == '^') {
                        lossHp += 1;
                    } else if (list.get(startY - 1).charAt(startX) == '^') {
                        lossHp += 1;
                        startX += 1;
                    } else if (list.get(startY - 1).charAt(startX) != '#') {
                        startX += 1;
                    }
                } else if (input.charAt(j) == 'U' && startY > 1) {
                    if (list.get(startY - 2).charAt(startX - 1) == '#' && list.get(startY - 1).charAt(startX - 1) == '^') {
                        lossHp += 1;
                    } else if (list.get(startY - 2).charAt(startX - 1) == '^') {
                        lossHp += 1;
                        startY -= 1;
                    } else if (list.get(startY - 2).charAt(startX - 1) != '#') {
                        startY -= 1;
                    }
                } else if (input.charAt(j) == 'D' && startY < n) {
                    if (list.get(startY).charAt(startX - 1) == '#' && list.get(startY - 1).charAt(startX - 1) == '^') {
                        lossHp += 1;
                    } else if (list.get(startY).charAt(startX - 1) == '^') {
                        lossHp += 1;
                        startY += 1;
                    } else if (list.get(startY).charAt(startX - 1) != '#') {
                        startY += 1;
                    }
                }
            }
            output.add(startY + " " + startX + " " + lossHp);
        }
        for (int i = 0; i < t; i++) {
            bw.write(output.get(i) + "\n");
            bw.flush();
        }
        bw.close();
    }
}
