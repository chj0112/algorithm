class Solution {
    public int[] solution(int n, int m) {
        int a = Math.min(n, m), b = Math.max(n, m);
        while (b % a != 0) {
            int temp = a;
            a = b % a;
            b = temp;
        }
        b = n * m / a;
        return new int[] {a, b};
    }
}