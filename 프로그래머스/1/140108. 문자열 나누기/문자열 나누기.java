class Solution {
    public int solution(String s) {
        int answer = 0;
        int x = 0, y = 0;
        char c = 0;
        for (int i = 0; i < s.length(); i++) {
            if (x == 0 && y == 0) {
                c = s.charAt(i);
                x++;
            } else {
                if (c == s.charAt(i)) x++;
                else y++;
            }
            if (x == y) {
                answer++;
                x = 0;
                y = 0;
            }
        }
        if (x != 0 || y != 0) answer++;
        return answer;
    }
}