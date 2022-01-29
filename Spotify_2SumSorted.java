class Solution {
    public int[] twoSum(int[] nums, int target) {
        // bruteForce - O(n^2): for i in nums, for j in nums, if i+j == target, return [i, j] 
        
        // More efficient - O(n): create map to store index of all nums
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();

        // iterate and look for diff = target-curr num, if in map, return current index and mapEntry index
        for (int i=0; i<nums.length; i++){
            
            int diff = target-nums[i];
            
            if (map.containsKey(nums[i])) 
                return new int[]{map.get(nums[i])+1, i+1}; // 1-indexed, so add 1 to each
            
            else 
                map.put(diff, i);
        }
        return new int[]{};
    }
}
