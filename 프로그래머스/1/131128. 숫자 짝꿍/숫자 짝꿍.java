import java.util.*;

class Solution {
    public String solution(String X, String Y) {
        int[] arr = new int[10];
        List<Integer> l = new ArrayList<>();
        for (char c : X.toCharArray()) {
            arr[Character.getNumericValue(c)]++;
        }
        for (char c : Y.toCharArray()) {
            int v = Character.getNumericValue(c);
            if (arr[v] > 0) {
                l.add(v);
                arr[v]--;
            }
        }
        if (l.isEmpty()) return "-1";
        l.sort(Comparator.reverseOrder());
        if (l.get(0) == 0) return "0";
        StringBuilder sb = new StringBuilder();
        l.forEach(e -> sb.append(e));
        return sb.toString();
    }
}