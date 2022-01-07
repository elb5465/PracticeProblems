class Solution {
    public static int rob(int[] nums){
        int l = nums.length;
        if (l==0)
            return 0;
        if (l==1)
            return nums[0];
        if (l==2)
            return Math.max(nums[0], nums[1]);
        
        // create list to keep track of totals at each house possible
        int[] dp = new int[l];
        dp[0] = nums[0];
        dp[1] = Math.max(nums[0], nums[1]);
      
        // iterate starting at 3rd house since we already have checks for when nums.length is 0,1 and 2 houses
        for (int i=2; i<dp.length; i++){
            dp[i] = Math.max(nums[i]+dp[i-2], dp[i-1]);
            System.out.println(dp[i]);
        }
        
        // return the last element since that will be the max robbed
        return dp[l-1];
        }
}
