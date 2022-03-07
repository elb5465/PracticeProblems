class Solution {
    public int search(int[] nums, int target) {
        int r = nums.length-1;
        int l = 0;
        
        while (l <= r){
            int m = (l+r) / 2;
            
            if (target==nums[m])
                return m;
            
            // check left portion
            if (nums[l] <= nums[m]){
                if (nums[m]<target || target<nums[l])
                    l = m+1;
                else
                    r = m-1;
            }
                
            // else in right portion
            else{
                if (target<nums[m] || nums[r]<target)
                    r = m-1;
                else
                    l = m+1;
            }    
        }
        return -1;
        
    }
    
