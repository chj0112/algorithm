class Solution {
    public String solution(int a, int b) {
        String answer = "";
        String[] day = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int[] mon = {31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int x = 4;
        for (int i = 0; i < a - 1; i++) {
            x += mon[i];
        }
        x += b;
        answer = day[x % 7];
        return answer;
    }
}