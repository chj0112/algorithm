class Solution {
    public String solution(String s) {
        String answer = "";
        int l = s.length();
        answer = l % 2 == 0 ? s.substring(l / 2 - 1, l / 2 + 1) : String.valueOf(s.charAt(l / 2));
        return answer;
    }
}