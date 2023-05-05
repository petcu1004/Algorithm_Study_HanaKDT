import java.util.*;

class Solution {
    public String solution(String s) {
        String[] strs = s.split(" ");
        int[] nums = Arrays.asList(strs).stream().mapToInt(Integer::parseInt).sorted().toArray();
        
        return nums[0] + " " + nums[nums.length-1];
    }
}