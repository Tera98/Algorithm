import java.io.*;           // 미완성
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();
        List<Integer> add = new ArrayList<>();
        List<Integer> sub = new ArrayList<>();

        String n = br.readLine();
        StringTokenizer st = new StringTokenizer(n);
        while (st.hasMoreTokens()) list1.add(Integer.parseInt(st.nextToken()));

        n = br.readLine();
        st = new StringTokenizer(n);
        while (st.hasMoreTokens()) list2.add(Integer.parseInt(st.nextToken()));
        Collections.reverse(list1);
        Collections.reverse(list2);

        // 덧셈, 뺄셈 연산
        if (list1.size() >= list2.size()) {
            for (int i = 0; i < list2.size(); i++) {
                if (i % 2 == 0) {
                    add.add(list1.get(i));
                    sub.add(list1.get(i));
                } else {
                    add.add(list1.get(i) + list2.get(i));
                    sub.add(list1.get(i) - list2.get(i));
                }
            }
            for (int i = list2.size(); i < list1.size(); i++) {
                add.add(list1.get(i));
                sub.add(list1.get(i));
            }
        } else {
            for (int i = 0; i < list1.size(); i++) {
                if (i % 2 == 0) {
                    add.add(list1.get(i));
                    sub.add(list1.get(i));
                } else {
                    add.add(list1.get(i) + list2.get(i));
                    sub.add(list1.get(i) - list2.get(i));
                }
            }
            for (int i = list1.size(); i < list2.size(); i++) {
                if (i % 2 == 0) {
                    add.add(list2.get(i));
                    sub.add(list2.get(i));
                } else {
                    add.add(list2.get(i));
                    sub.add(list2.get(i) * (-1));
                }
            }
        }
        // 0인 차수 제거
        int j = 0;
        while (j < add.size()) {
            if (j % 2 == 1) {
                if (add.get(j) == 0) {
                    add.remove(j - 1);
                    add.remove(j - 1);
                    j = 0;
                }
            }
            j++;
        }
        j = 0;
        while (j < sub.size()) {
            if (j % 2 == 1) {
                if (sub.get(j) == 0) {
                    sub.remove(j - 1);
                    sub.remove(j - 1);
                    j = 0;
                }
            }
            j++;
        }
        // 출력 부분
        Collections.reverse(add);
        Collections.reverse(sub);
        for (int i = 0; i < add.size(); i++) {
            bw.write(add.get(i) + " ");
            bw.flush();
        }
        bw.write("\n");
        bw.flush();
        for (int i = 0; i < sub.size(); i++) {
            bw.write(sub.get(i) + " ");
            bw.flush();
        }
        bw.write("\n");
        bw.flush();
        bw.close();
    }
}
