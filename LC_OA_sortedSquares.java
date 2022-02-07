class Solution {
    public int[] sortedSquares(int[] nums) {
        for (int i=0; i<nums.length; i++)
            nums[i] = nums[i]*nums[i];
        
        Arrays.sort(nums);
        return nums;
    }
}

// Input: nums = [-4,-1,0,3,10]
// Output: [0,1,9,16,100]

