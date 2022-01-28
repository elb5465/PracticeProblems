class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length <=1) return nums.length;
        
        // sort in O(n) 
        // using minHeap so we can go from lowest to highest
        // CANT USE BC DOESNT STORE DUPLICATES
            // PriorityQueue<Integer> pq = new PriorityQueue<>();
            // for (int i : nums) pq.offer(i);
      
        // O(n logn)
        Arrays.sort(nums);
        
        int cnt = 1;
        int max = 1;
        
        for (int i=1; i<nums.length; i++){
            if (nums[i]-nums[i-1] == 1)  {cnt++;}
            else if (nums[i]==nums[i-1]) {}
            else                         {cnt = 1;}
            
            max = Math.max(max, cnt);
        }
        return max;
    }
}
