class Solution {
    public int[] solution(long n) {
        StringBuilder sb = new StringBuilder(String.valueOf(n));
        sb.reverse();
        return sb.chars().map(e -> e - '0').toArray();
    }
}