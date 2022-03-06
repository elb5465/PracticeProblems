class Solution {
    public int[][] merge(int[][] iv) {
        ArrayList<int[]> resArr = new ArrayList<int[]>();
        Arrays.sort(iv, (a, b) -> a[0] - b[0]);
        
        if (iv.length == 0) return new int[][]{};
        if (iv.length == 1) return iv;

        resArr.add(iv[0]);
        
        for (int i=1; i<iv.length; i++){
            int lastEnd   = resArr.get(resArr.size()-1)[1];
            int lastStart = resArr.get(resArr.size()-1)[0];

            // if last elem of prev interval greater/equal to first elem of curr, merge them
            if (iv[i][0] <= lastEnd){
                
                // if last elem of curr greater/equal to last prev, make last elem of curr end
                int end   = Math.max(iv[i][1], lastEnd);
                
                resArr.set(resArr.size()-1, new int[]{lastStart, end});
            }
            
            else
                resArr.add(iv[i]);
            
        }
    
        return resArr.toArray(new int[][]{});
    }
}
