import java.util.*;

class Solution {
    public long solution(long n) {
        long answer = 0;
        Integer[] arr = String.valueOf(n).chars().map(e -> (int) e - '0').boxed().toArray(Integer[]::new);
        Arrays.sort(arr, Comparator.reverseOrder());
        for (Integer i : arr) {
            answer *= 10;
            answer += i;
        }
        return answer;
    }
}