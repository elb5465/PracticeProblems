class Solution {
    public void sortColors(int[] nums) {
        int zeroIndex = 0;
        int twoIndex = nums.length - 1;
        int i = 0;
        
        while( i <= twoIndex ) {
            // dont inc i for 2 bc you don't know if you switched with 1 or 0
            if (nums[i] == 2){
                swap(nums, twoIndex, i); 
                twoIndex --;
            }

            // swap 0 at the curr index i with whatever is at index 'zeroIndex'
            else if (nums[i] == 0){
                swap(nums, zeroIndex, i);
                zeroIndex ++; i ++;
            }
            
            // if curr num is a 1 just inc i bc when nums[i] is a zero we will switch index i with zeroIndex.
            else
                i++;
            
            for (int n : nums)
                System.out.printf("%d ", n);
            System.out.println("");
        }
    }

    
    
    public void swap(int[] nums, int i, int j) {
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}
