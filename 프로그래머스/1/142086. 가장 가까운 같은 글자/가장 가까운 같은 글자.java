class Solution {
    public int[] solution(String s) {
        int[] answer = new int[s.length()];
        char c;
        for (int i = 0; i < s.length(); i++) {
            c = s.charAt(i);
            int count = 1;
            for (int j = i - 1; j >= 0; j--) {
                if (c == s.charAt(j)) {
                    answer[i] = count;
                    break;
                } else count++;
            }
            if (answer[i] == 0) answer[i] = -1;
        }
        return answer;
    }
}