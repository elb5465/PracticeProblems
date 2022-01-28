class Solution {
    public int findKthLargest(int[] nums, int k) {
        
        // starts as min heap (smallest num at root), so reverse to be maxheap (max at root)
        PriorityQueue<Integer> pq = new PriorityQueue<Integer>(nums.length, Collections.reverseOrder());
        
        // adding numbers will to pq will sort them automatically
        for (int num :  nums) { pq.add(num); }
        
        // just need to pop off all but 1 from k and return the final removed node
        while (k>1){
            pq.poll();
            k --;
        }
        
        
        return pq.poll();
        }
}
