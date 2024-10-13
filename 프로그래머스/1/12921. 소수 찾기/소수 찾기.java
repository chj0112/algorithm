class Solution {
    public int solution(int n) {
        int answer = 0;
        for (int i = 2; i <= n; i++) {
            int flag = 0;
            for (int j = 2; j <= Math.sqrt(i); j++) {
                if (i % j == 0) {
                    flag = 1;
                    break;
                }
            }
            if (flag == 0) {
                answer += 1;
            }
        }
        return answer;
    }
}