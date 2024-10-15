class Solution {
    public boolean solution(int x) {
        return x % String.valueOf(x).chars().map(e -> e - '0').sum() == 0;
    }
}