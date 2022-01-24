class Solution {
    public int addDigits(int num) {
        
        String s = String.valueOf(num);
        
        if (s.length() == 1)
            return num;
            
        int sum = 0;
        for (char c : s.toCharArray()){
            sum += Integer.parseInt(String.valueOf(c));
        }
        
        return addDigits(sum);
        
    }
}
