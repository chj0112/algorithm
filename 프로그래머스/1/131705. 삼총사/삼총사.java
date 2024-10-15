import java.util.*;

class Solution {
    int answer = 0;
    public int solution(int[] number) {
        dfs(0, new int[] {}, number);
        return answer;
    }
    public void dfs(int k, int[] arr, int[] num) {
        if (arr.length == 3) {
            if (Arrays.stream(arr).sum() == 0) {
                answer++;
            }
            return;
        }
        for (int i = k; i < num.length; i++) {
            int[] newArr = new int[arr.length + 1];
            for (int j = 0; j < arr.length; j++) {
                newArr[j] = arr[j];
            }
            newArr[arr.length] = num[i];
            dfs(i + 1, newArr, num);
        }
    }
}