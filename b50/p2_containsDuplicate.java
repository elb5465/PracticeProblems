class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Use hashSet to search if contained in O(1) time
        HashSet<Integer> set = new HashSet<>();
        
        // if already in set, then there's a dup, o.w. no dup
        for (int n : nums){
            if (set.contains(n))
                return true;
            else
                set.add(n);
        }
        
        return false;
    }
}
