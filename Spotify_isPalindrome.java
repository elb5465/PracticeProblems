class Solution {
    // doesn't work for "a." for some reason
    public boolean isPalindrome(String s) {
        int l = s.length()-1;
        String rev = ""; // reversed trimmed string
        String ts = "";  // trimmed string
        
        for (int i=0; i<l; i++){
            char c  = s.charAt(l-i);
            if (Character.isLetterOrDigit(c))
                rev += String.valueOf(c).toLowerCase();
            
            char ct = s.charAt(i);
            if (Character.isLetterOrDigit(ct))
                ts += String.valueOf(ct).toLowerCase();
        }
        
        System.out.println(rev);
        System.out.println(ts);
        return (rev.equals(ts));
    }
}
