class Solution {
    public void moveZeroes(int[] nums) {
        int m=0; 
      
      // [0,1,0,1]
      // [1,0,0,1] 1-m1 = 0 
      // [1,0,0,1] m2
      // [1,1,0,0] 3-2 = 1 
        
        for(int i=0;i<nums.length;i++){
            
            if (nums[i]==0)
                m++;
                
            else if (m!=0){
                nums[i-m] = nums[i];
                nums[i] = 0;
            }
        }
                    
    }
}
