import java.util.*;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        Stack<Integer> stack = new Stack<>();
        for (int n : ingredient) {
            if (n == 1) {
                if (stack.size() >= 3) {
                    int a = stack.pop();
                    int b = stack.pop();
                    int c = stack.pop();
                    if (a == 3 && b == 2 && c == 1) {
                        answer++;
                        continue;
                    } else {
                        stack.push(c);
                        stack.push(b);
                        stack.push(a);
                    }
                }
            }
            stack.push(n);
        }
        return answer;
    }
}