class Solution {
    Boolean debug = true;
    
    public void print(String someString){
        if (this.debug==true) System.out.println(someString);
    }
    
    // O(n) == O(n) + O(n)
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> set = new HashSet<Integer>(nums.length);
        for (int num : nums) set.add(num);
        
        int maxStreak = 0;
        
        // looking for start of a consecutive sequence...
        for (int n: nums){
            // if num has no prev consecutive, then it is the start
            if (!set.contains(n-1)){
                int curr = n;
                int streak = 0;
                
                // inc curr until not found in set
                while (set.contains(curr)){
                    curr ++;
                    streak ++;
                }
                maxStreak = Math.max(maxStreak, streak);
            }
        }
        return maxStreak;
    }
    
    
    //O(n logn + n) bc of sorting + loop
    public int longestConsecutive(int[] nums) {
        if (nums.length <=1) return nums.length;
        
        int cnt = 1;
        int maxCount = -10000;
        Arrays.sort(nums);
        int prev = nums[0];
        
        for (int i=1; i<nums.length; i++){
            if (nums[i]==prev+1)    cnt ++;
            else if (nums[i]==prev) {}// do nothing
            else                    cnt = 1;
    
            prev = nums[i];            
            maxCount = Math.max(maxCount, cnt);
        }
        
        return maxCount;
    }



        
    // O(n logn?)
    public int longestConsecutive(int[] nums) {
        if (nums.length <=1) return nums.length;
        
        // adding to minHeap INSERTS in O(logn), meaning O(nlogn) to sort anyway...
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
        for (int n : nums) pq.offer(n);
        
        int prev = Integer.MIN_VALUE;
        int maxStreak = 0; 
        int streak = 1;
        
        while (pq.size() != 0){
            int curr = pq.poll();
            print("" + curr);
            
            if (curr == prev+1) {
                print("err");
                streak++;
            }
            else if (curr==prev) {} // do nothing for duplicates
            
            else        
                streak = 1; // if streak broken..
                
            maxStreak = Math.max(maxStreak, streak);
            prev = curr;
            
            print("streak: "+streak);
            print("max: "+maxStreak);
        }

        return maxStreak;
    }
}
