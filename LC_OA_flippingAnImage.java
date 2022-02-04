class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        int row = A.length;
        int col = A[0].length;
        int[][] B = new int[row][col];
        
        for (int i=0; i<row; i++){
            for (int j=0; j<col; j++){
            
                // load the elems into the new array backwards to from A[][] to reverse
                B[i][j] = A[i][col - j - 1];
                
                // invert each elem as we traverse
                B[i][j] = (B[i][j]==0) ? 1 : 0;
            }
        }
        
        return B;
    }
}
