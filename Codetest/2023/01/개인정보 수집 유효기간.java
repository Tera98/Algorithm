import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Date;
import java.util.List;

class Solution {
    public static int[] solution(String today, String[] terms, String[] privacies) throws ParseException {
        int[] answer = {};
        List<Integer> list = new ArrayList<>();
        String[] arrDate = new String[privacies.length];
        String[] arrType = new String[privacies.length];
        int[] arrTypeDate = new int[privacies.length];

        for (int i = 0; i < privacies.length; i++) arrDate[i] = privacies[i].substring(0, 10);
        for (int i = 0; i < privacies.length; i++) arrType[i] = privacies[i].substring(11, 12);
        int k = 0, j = 0;
        while (j < arrType.length) {
            if (terms[k].contains(arrType[j])) {
                arrTypeDate[j] = Integer.parseInt(terms[k].substring(2));
                k = -1;
                j++;
            }
            k++;
        }

        int[] a = new int[arrDate.length];
        for (int i = 0; i < arrDate.length; i++) {
            a[i] = Integer.parseInt(arrDate[i].substring(0, 4)) * 12 * 28 + Integer.parseInt(arrDate[i].substring(5, 7)) * 28
                    + Integer.parseInt(arrDate[i].substring(8, 10));
        }

        int todayInt = Integer.parseInt(today.substring(0, 4)) * 12 * 28 + Integer.parseInt(today.substring(5, 7)) * 28
                + Integer.parseInt(today.substring(8, 10));

        for (int i = 0; i < arrTypeDate.length; i++) if (todayInt - arrTypeDate[i] * 28 >= a[i]) list.add(i + 1);

        Integer arr1[] = list.toArray(new Integer[list.size()]);
        answer = Arrays.stream(arr1).mapToInt(Integer::intValue).toArray();
        return answer;
    }
}
