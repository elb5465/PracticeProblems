class Solution {
    public int[] twoSum(int[] nums, int target) {
        // bruteForce - O(n^2): for i in nums, for j in nums, if i+j == target, return [i, j] 
        
        // More efficient - O(2n): create map to store index of all nums
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for (int i=0; i<nums.length; i++) 
            map.put(nums[i], i);

        // iterate and look for diff = target-curr num, if in map, return current index and mapEntry index
        for (int i=0; i<nums.length; i++){
            int diff = target-nums[i];
            if (map.containsKey(diff) && map.get(diff)!=i) {
                return new int[]{map.get(diff), i};

            }
        }
        return new int[]{};
    }


    public int[] twoSum(int[] nums, int target) {
        // Even slightly more efficient - O(n): one pass through
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();

        // iterate and look for diff = target-curr num, if in map, return current index and mapEntry index
        for (int i=0; i<nums.length; i++){
            
            int diff = target-nums[i];
            
            if (map.containsKey(nums[i])) 
                return new int[]{map.get(nums[i]), i};
            
            // putting the diffs in the map, so when we find one that would sum, we know we have a match
            else
                map.put(diff, i);
        }
        
        return new int[]{};
    }
    
}
