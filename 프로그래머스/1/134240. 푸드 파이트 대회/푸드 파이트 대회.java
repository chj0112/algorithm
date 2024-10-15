import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public String solution(int[] food) {
        LinkedList<Integer> ll = new LinkedList<>();
        for (int i = 1; i < food.length; i++) {
            for (int j = 0; j < (food[i] / 2) * 2; j++) {
                ll.add(ll.size() / 2, i);
            }
        }
        ll.add(ll.size() / 2, 0);
        return ll.stream().map(String::valueOf).collect(Collectors.joining());
    }
}