// Asked by Spotify (According to Glassdoor)
class Solution {
    Boolean debug = false;
    
    public int longestConsecutive(int[] nums) {
        if (nums.length <=1) return nums.length;
        
        int cnt = 1;
        int maxCount = -10000;
        Arrays.sort(nums);
        int prev = nums[0];
        
        for (int i=1; i<nums.length; i++){
            if (nums[i]==prev+1)    cnt ++;
            else if (nums[i]==prev) // do nothing
            else                    cnt = 1;
    
            prev = nums[i];            
            maxCount = Math.max(maxCount, cnt);
        }
        
        return maxCount;
    }
    
    public void print(String someString){
        if (this.debug==true)
            System.out.println(someString);
    }
}
