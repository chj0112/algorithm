import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        List<Integer> list = new ArrayList<>();
        for (int n : arr) {
            if (n % divisor == 0) {
                list.add(n);
            }
        }
        if (list.isEmpty()) list.add(-1);
        return list.stream().mapToInt(x -> x).sorted().toArray();
    }
}