class Solution {
    // O(n) time, O(1) space?
    public void reverseString(char[] s) {
        int i = 0;
        int j = String.valueOf(s).length()-1;
        char temp = '';
      
        while (i<j){
            temp = s[i];
            s[i] = s[j];
            s[j] = temp;
            i ++;
            j --;
        }
    }
}
