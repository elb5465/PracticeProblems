// https://leetcode.com/problems/number-of-closed-islands/discuss/425135/Java-Very-Simple-DFS-Solution

class Solution {
    public int closedIsland(int[][] grid) {
        // printing islands
        for (int[] g : grid){ for (int i : g){ System.out.print(" " + i);}System.out.println("");} System.out.println("");
        
        int count = 0;
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[i].length; j++) {
                
                if (grid[i][j]==0 && dfs(i, j, grid)==0) 
                    count++;
            }
        }
        
        // printing islands
        for (int[] g : grid){ for (int i : g){ System.out.print(" " + i);}System.out.println("");}
        
        return count;
    }
    
    
    
    private int dfs(int i, int j, int[][] grid) {
        if (i<0 || i>=grid.length || j<0 || j>=grid[0].length) {
            return 1;
        }
        
        if (grid[i][j]==1 || grid[i][j]==2) 
            return 0;
        
        // mark visited
        grid[i][j] = 2;
        
        // check each direction
        return dfs(i+1, j, grid) | dfs(i-1, j, grid) | dfs(i, j-1, grid) | dfs(i, j+1, grid);
    }

}
