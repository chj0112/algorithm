import java.util.*;

class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        List<Integer> l = new ArrayList<>();
        int min = 2001;
        for (int i = 0; i < score.length; i++) {
            if (i < k) {
                l.add(score[i]);
                min = Math.min(min, score[i]);
            } else if (min < score[i]) {
                l.remove(Integer.valueOf(min));
                l.add(score[i]);
                min = l.stream().mapToInt(e -> e).min().getAsInt();
            }
            answer[i] = min;
        }
        return answer;
    }
}