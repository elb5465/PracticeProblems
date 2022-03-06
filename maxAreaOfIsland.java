class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int maxArea = 0;
        
        // edge case for empty grid
        if (r == 0) return 0;
        
        // go through each cell and do dfs when you find a new island,
        // it will recursively mark all connected entries as '2', meaning 'visited'
        for (int i=0; i<r; i++){
            for (int j=0; j<c; j++){     
                
                if (grid[i][j] == 1)
                    maxArea = Math.max(maxArea, getIslandSize(grid, i, j, r, c));
            }
        }
        
        return maxArea;
    }
    
    public int getIslandSize(int[][] grid, int i, int j, int r, int c){
        
        // if out of bounds, top, right, down, left
        // if cell is not '1' (unvisited land), ignore it
        if (i<0 || j>=c || i>=r || j<0 || grid[i][j]!=1)
            return 0;
        
        // mark current cell as visited so there isn't an endless loop of recursion
        grid[i][j] = 2;
        
        // Do DFS on neighboring cells to add up area
        int cnt = 1;
        cnt += getIslandSize(grid, i-1, j, r, c); // top
        cnt += getIslandSize(grid, i, j+1, r, c); // right 
        cnt += getIslandSize(grid, i+1, j, r, c); // down
        cnt += getIslandSize(grid, i, j-1, r, c); // left
        return cnt;
    }
}
