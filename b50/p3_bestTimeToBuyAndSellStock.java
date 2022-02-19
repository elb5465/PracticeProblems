class Solution {
    public int maxProfit(int[] p) {
        int lsf = Integer.MAX_VALUE;
        int maxProfit = 0;
        
        for (int i=0; i<p.length; i++){
            // update the curr min
            if (p[i] < lsf)
                lsf = p[i];
            
            // update the max profit
            if (maxProfit < p[i]-lsf)
                maxProfit = p[i]-lsf;
        }
        
        return maxProfit;
        
    }
}
