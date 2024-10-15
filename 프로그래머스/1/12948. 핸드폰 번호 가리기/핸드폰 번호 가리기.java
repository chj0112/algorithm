class Solution {
    public String solution(String phone_number) {
        char[] c = phone_number.toCharArray();
        for (int i = 0; i < c.length; i++) {
            if (c.length - i > 4) c[i] = '*';
        }
        return String.valueOf(c);
    }
}