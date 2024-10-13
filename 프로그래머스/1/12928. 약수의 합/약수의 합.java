import java.util.*;

class Solution {
    public int solution(int n) {
        HashSet<Integer> set = new HashSet<>();
        for (int i = 1; i <= Math.sqrt(n); i++) {
            if (n % i == 0) {
                set.add(i);
                set.add(n / i);
            }
        }
        if (set.isEmpty()) set.add(0);
        return set.stream().reduce((x, y) -> x + y).get();
    }
}