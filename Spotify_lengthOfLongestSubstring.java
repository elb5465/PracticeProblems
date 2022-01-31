class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        
        int max = 0;
        int left = 0;
        
        for (int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            
            // keep index of all chars in map
            // move left pointer 1 to the right if same char found
            if (map.containsKey(c))
                left = Math.max(left, map.get(c)+1);
            
            // overwrite or add new entry of curr chars
            map.put(c, i);
            
            // just take the diff between curr idx and left ptr 
            // (adding one bc it's zero indexed)
            max = Math.max(max, i-left+1);
        }
        
        return max;
    }
}
