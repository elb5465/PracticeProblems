class Solution {
    public int fib(int n) {
        if (n==0)
            return 0;
        if (n==1 || n==2)
            return 1;
        
        int[] fib = new int[n];
        fib[0] = 1;
        fib[1] = 1;
        for (int i=2; i<n; i++){
            fib[i] = fib[i-1] + fib[i-2];
        }
        
        return fib[n-1];
    }
}
