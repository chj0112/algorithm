class Solution {
    public String solution(int n) {
        char[] c = new char[n];
        for (int i = 0; i < n; i ++) {
            if (i % 2 == 0) c[i] = '수';
            else c[i] = '박';
        }
        return String.valueOf(c);
    }
}