class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<Character>();
        
        for (char c : s.toCharArray()){
            if (st.empty() && (c==')' || c=='}' || c==']')) 
                return false;

            if (c=='(' || c=='{' || c=='[')
                st.push(c);
            
            else if (c == ')'){
                if (!st.empty() && st.pop() != '(')
                    return false;
            }
            
            else if (c == ']'){
                if (!st.empty() && st.pop() != '[')
                    return false;
            }
            
            else if (c == '}'){
                if (!st.empty() && st.pop() != '{')
                    return false;
            }
            
        }
        return st.empty();
    }
}
