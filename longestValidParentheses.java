public class Solution {
  
    // one iteration using a stack O(n)
    public int longestValidParentheses(String s) {
        Stack<Integer> st = new Stack<Integer>();
        st.push(-1); // adding -1 so we can consistently get accurate diff since 0 indexed.
        int max = 0;
        
        for (int i=0; i<s.length(); i++){
          
            // if curr is right paren, and -1 isn't the only thing on the stack, and the prev elem on stack is a left, then you have a valid pair
            if ( s.charAt(i)==')'  &&  st.size()>1  &&  s.charAt(st.peek())=='('){
                st.pop();                          // found a pair, so pop off left and update max
                max = Math.max(max, i-st.peek());  // take max of currentMax or the diff between i and the last element index on the stack
            }
          
            // you want to also pushl LEFT so you can pop eventually, or INVALID RIGHT paren index to use to tell where to count valid from
            else
                st.push(i);
        }
      
        return max;
    }
    
    // dynamic programming O(n)
    public int longestValidParentheses(String s) {
        char[] chs = s.toCharArray();
        int[] dp = new int[chs.length];
        int max = 0;
        
        for (int i=1; i<chs.length; i++) {
            if (chs[i] == ')') {
                if (chs[i-1] == '(') {
                    dp[i] = ((i == 1) ? 0 : dp [i-2]) + 2;
                } else {
                    int pos = i - dp[i-1] - 1;
                    if (pos >= 0 && chs[pos] == '(') {
                        dp[i] = dp[i-1] + 2 + ((pos > 0) ? dp[pos-1] : 0);
                    }
                }
            }

            max = Math.max(max, dp[i]);
        }
        
        return max;        
    }
}
