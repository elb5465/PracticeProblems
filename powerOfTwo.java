class Solution {
    public boolean isPowerOfTwo(int n) {
        if (n == 1) return true;
        if (n % 2 == 1) return false;
        
        long t = 1;
        while (t < n){
            t *= 2;
            System.out.println(t);
        }
        if (t == n) return true;
        
        return false;
    }
}
