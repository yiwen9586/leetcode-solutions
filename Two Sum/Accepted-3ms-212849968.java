// 
// Generated by fetch-leetcode-submission project on GitHub.
// https://github.com/gitzhou/fetch-leetcode-submission
// Contact Me: aaron67[AT]aaron67.cc
// 
// Two Sum
// https://leetcode.com/problems/two-sum/
// 

class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> numap = new HashMap<>();
        for(int i = 0; i < nums.length; i++){
            int left = target - nums[i];
            if(numap.containsKey(left))
                return new int[] {numap.get(left), i};
            numap.put(nums[i], i);
        }
        return null;
    }
}

