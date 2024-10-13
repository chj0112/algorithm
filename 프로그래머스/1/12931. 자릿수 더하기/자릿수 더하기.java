import java.util.*;

public class Solution {
    public int solution(int n) {
        String s = String.valueOf(n);
        return s.chars().map(e -> e - '0').reduce((x, y) -> x + y).getAsInt();
    }
}