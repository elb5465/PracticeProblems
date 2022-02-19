class Solution {
    
  
    // O(3n) using hashmap 
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> map = new HashMap<>();
        
        for (char c : s.toCharArray()){
           map.put(c, map.getOrDefault(c, 0) + 1);
        }
        
        for (char c : t.toCharArray()){
            if (map.containsKey(c))
                map.put(c, map.get(c) - 1);
            else
                return false;
        }
        
        for (Map.Entry e : map.entrySet()){
            if ((int) e.getValue() != 0)
                return false;
        }
            
        return true;
    }
    
    
    // Slower version, O(n logn) using built-in sort 
    public boolean isAnagram(String s, String t) {
        char[] sChar = s.toCharArray();
        char[] tChar = t.toCharArray();

        Arrays.sort(sChar);
        Arrays.sort(tChar);

        return Arrays.equals(sChar, tChar);   
    }
}
            
