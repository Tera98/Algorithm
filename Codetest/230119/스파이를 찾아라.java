import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int testNum = Integer.parseInt(br.readLine());
        List<Integer> output = new ArrayList<>();
        for (int i = 0; i < testNum; i++) {

            int caseLength = Integer.parseInt(br.readLine());
            String str = br.readLine();
            StringTokenizer st = new StringTokenizer(str);
            List<Integer> list = new ArrayList<>();

            for (int j = 0; j < caseLength; j++) list.add(Integer.parseInt(st.nextToken()));
            int index = -1;

            for (int j = 0; j < caseLength - 2; j++) {
                if (!list.subList(j + 1, list.size()).contains(list.get(j))) {
                    index = j;
                }
            }
            if (index == -1) {
                if (list.get(0) == list.get(caseLength - 1)) index = caseLength - 2;
                else index = caseLength - 1;
            }
            output.add(index+1);
        }
        for (Integer integer : output) {
            bw.write(integer + "\n");
            bw.flush();
        }
        bw.close();
    }
}
