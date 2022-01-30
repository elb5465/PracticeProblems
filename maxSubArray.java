class Solution {
    public int maxSubArray(int[] nums) {
        // bruteforce
        // iterate through every combination of contiguous subarrays and calc sums
        // At least O(n^2), bc window size adjustments take multiple pass-throughs
        
        // dp
        // check sub problem for 0 nums, 1 num, max of curr compared to a running total + curr
        int l = nums.length;
        int lMax = 0;
        int gMax = -100000000;

        if (l==0) return 0;
        if (l==1) return nums[0];
        
        for (int i=0; i<l; i++){
            lMax = Math.max(nums[i], nums[i]+lMax);
            gMax = Math.max(gMax, lMax);
        }
        
        return gMax;
    }
}
