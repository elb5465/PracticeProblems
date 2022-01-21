class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<Character>();
        
        for (char c : s.toCharArray()){
            if (c == '(')
                st.push(c);
            
            if (c == ')'){
                if (!st.empty() && st.pop() != '(')
                    return false;
            }
        }
        return st.empty();
    }
}
