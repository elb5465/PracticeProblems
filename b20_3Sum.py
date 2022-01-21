class Solution {
    Boolean debug = false;
    
    public int longestConsecutive(int[] nums) {
        if (nums.length <=1) return nums.length;
        
        int cnt = 1;
        int maxCount = -10000;
        Arrays.sort(nums);
        int prev = nums[0];
        
        for (int num : nums){
            if (num==prev+1)    cnt ++;
            else if (num==prev) {}// do nothing
            else                cnt = 1;
    
            prev = num;            
            maxCount = Math.max(maxCount, cnt);
        }
        
        return maxCount;
    }
    
    public void print(String someString){
        if (this.debug==true)
            System.out.println(someString);
    }
}
