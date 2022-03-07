class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // option 1: 
        // sort every string in the list (n * nlogn)
        
        // option 2 (much better):
        // total the alphanumeric value of every str, save to a hashmap<String, Integer>
        
        if (strs.length == 0) return new ArrayList();
        
        Map<String, List> map = new HashMap<String, List>();
        
        int[] count = new int[26];
        
        for (String s : strs){
            Arrays.fill(count, 0);
            for (char c : s.toCharArray()) count[c-'a']++;
            
            String key = "";
            for (int i=0; i<count.length; i++) key+="#"+count[i];
            
            // System.out.println(key);
            // if the bucket entry doesn't exist, create a new one for it and add that string, o.w. just add the str to appropriate bucket
            if (!map.containsKey(key)) 
                map.put(key, new ArrayList());
            
            map.get(key).add(s);
        }
        
        return new ArrayList(map.values());
    }
}
