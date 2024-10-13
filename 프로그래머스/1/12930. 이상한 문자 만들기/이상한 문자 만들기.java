class Solution {
    public String solution(String s) {
        String[] words = s.split(" ", -1);
        for (int i = 0; i < words.length; i++) {
            char[] c = words[i].toCharArray();
            for (int j = 0; j < c.length; j++) {
                if (j % 2 == 0) c[j] = String.valueOf(c[j]).toUpperCase().charAt(0);
                else c[j] = String.valueOf(c[j]).toLowerCase().charAt(0);
            }
            words[i] = String.valueOf(c);
        }
        return String.join(" ", words);
    }
}