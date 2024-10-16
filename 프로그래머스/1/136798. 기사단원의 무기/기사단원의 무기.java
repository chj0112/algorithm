import java.util.*;

class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        int[] arr = new int[number];
        for (int i = 1; i <= number; i++) {
            int tmp = 0;
            for (int j = 1; j <= Math.sqrt(i); j++) {
                if (i % j == 0) {
                    tmp += 2;
                    if (j == Math.sqrt(i)) tmp--;
                }
            }
            arr[i - 1] = tmp;
        }
        answer = Arrays.stream(arr).map(o -> o > limit ? o = power : o).sum();
        return answer;
    }
}