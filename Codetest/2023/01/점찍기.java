class Solution {
    public static long solution(int k, int d) {
        long answer = 0;
        for (int i = 0; i <= d / k; i++) answer += (long) Math.pow(Math.pow(d, 2) - Math.pow(i * k, 2), 0.5) / k + 1;
        return answer;
    }
}
