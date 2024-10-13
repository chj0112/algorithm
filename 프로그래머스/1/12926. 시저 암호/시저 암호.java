class Solution {
    public String solution(String s, int n) {
        char[] c = s.toCharArray();
        for (int i = 0; i < c.length; i++) {
            if (c[i] >= 'a' && c[i] <= 'z') {
                c[i] += n;
                if (c[i] > 'z') c[i] -= 26;
            } else if (c[i] >= 'A' && c[i] <= 'Z') {
                c[i] += n;
                if (c[i] > 'Z') c[i] -= 26;
            }
        }
        return String.valueOf(c);
    }
}