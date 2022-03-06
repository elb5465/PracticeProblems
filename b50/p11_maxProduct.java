// https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity

// same logic as max subarray problem, except now you keep track of the min as well, and switch when you come across a negative.

class Solution {
    public int maxProduct(int[] nums) {
        
        int max = Integer.MIN_VALUE;
        int cmax = 1; 
        int cmin = 1;
        
        for(int i=0; i<nums.length; i++){
            // swap max and min vars if negative
            if(nums[i] < 0){ 
                int tmp = cmax; 
                cmax = cmin; 
                cmin = tmp;
            }
            
            cmax = Math.max(cmax*nums[i], nums[i]);
            cmin = Math.min(cmin*nums[i], nums[i]);
            
            max = Math.max(max, cmax);
        }
        
        return max;
    }
}
