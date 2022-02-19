class Solution {
    public int[] twoSum(int[] nums, int target) {
        // store the nums with their associated indexes
        HashMap<Integer, Integer> map = new HashMap<>();
        
        for (int i=0; i<nums.length; i++){
            
            // check if (target - current) is in map already, if it is then return index of that and current
            if (map.containsKey(target-nums[i]))
                return new int[]{map.get(target-nums[i]), i};
            
            // otherwise, add the current to the map with curr index
            else
                map.put(nums[i], i);
        }
    }
}
