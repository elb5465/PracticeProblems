class Solution {
    public void rotate(int[][] A) {
        int len = A.length;
        
        // transpose the matrix
        for (int i=0; i<len; i++){
            for (int j=i+1; j<len; j++){
                // aka: switch rows and columns for each entry
                int temp = A[i][j];
                A[i][j] = A[j][i];
                A[j][i] = temp;
            }
        }
            
        int middle = len/2;
        
        // flip horizontally
        for (int i=0; i<len; i++){
            for (int j=0; j<middle; j++){
                int temp = A[i][j];
                A[i][j] = A[i][len-j-1];
                A[i][len-j-1] = temp;
            }
        }
    }
}
