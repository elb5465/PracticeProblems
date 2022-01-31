class Solution {
    // doesn't trim beginning and ending spaces but could add that whenever
    public String reverseWords(String s) {
        int l = s.length();
        String res = "";
        String temp = "";
        boolean isFirst = true;
        
        int i = 0;
        for (char c : s.toCharArray()){
            if (c == ' '){
                if (isFirst){
                    res = temp + res;
                    isFirst = false;
                }
                else
                    res = temp + " " + res;
                temp = "";
            }
            if (i==l-1){
                res = temp + s.charAt(l-1) + " " + res;
            }
            
            if (c != ' ')
                temp += String.valueOf(c);
            i ++;
        }
        
        System.out.println(res);
        return res;
    }
}
