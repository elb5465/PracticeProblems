class Solution {
    public boolean canJump(int[] nums) {
        int max = 0;
        
        for (int i=0; i<nums.length; i++){
            // check if the current index is out of reach of the highest max
            if (i > max) return false;
          
            // o.w. take the max of curr max and the (index + current num)
            max = Math.max(nums[i] + i, max);
        }
        
        return true;
    }
}
