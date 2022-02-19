class Solution {
    public int maxSubArray(int[] nums) {
        // dp
        // check sub problem for 0 nums, 1 num, max of curr compared to a running total + curr
        int l = nums.length;
        int lMax = 0;
        int gMax = Integer.MIN_VALUE;

        if (l==0) return 0;
        if (l==1) return nums[0];
        
        for (int i=0; i<l; i++){
            lMax = Math.max(nums[i], nums[i]+lMax);
            gMax = Math.max(gMax, lMax);
        }
        
        return gMax;
    }
}
