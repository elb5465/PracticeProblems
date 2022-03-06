class Solution {
    public int numIslands(char[][] grid) {
        int r = grid.length;
        int c = grid[0].length;
        int numIslands = 0;
        
        // edge case for empty grid
        if (rows == 0) return 0;
        
        // go through each cell and do dfs when you find a new island,
        // it will recursively mark all connected entries as '2', meaning 'visited'
        for (int i=0; i<r; i++){
            for (int j=0; j<c; j++){                
                if (grid[i][j] == '1'){
                    markIslandVisited(grid, i, j, r, c);
                    numIslands ++;
                }
            }
        }
        
        
        return numIslands;
    }
    
    public void markIslandVisited(char[][] grid, int i, int j, int r, int c){
        
        // if out of bounds, top, right, down, left
        // if cell is not '1' (unvisited land), ignore it
        if (i<0 || j>=c || i>=r || j<0 || grid[i][j]!='1')
            return;
        
        grid[i][j] = '2';
        
        markIslandVisited(grid, i-1, j, r, c); // top
        markIslandVisited(grid, i, j+1, r, c); // right 
        markIslandVisited(grid, i+1, j, r, c); // down
        markIslandVisited(grid, i, j-1, r, c); // left
    }
}
