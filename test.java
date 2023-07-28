class Solution {
    public static int[][] maxValue(int[][] grid) {
        //dp[i][j] represent most value
        //dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + dp[i][j]
        int m = grid.length, n = grid[0].length;
        //initiate column
        for(int i = 1; i < m; i++) {
            grid[i][0] += grid[i-1][0];
        }
        for (int j = 1; j < n; j++) {
            grid[0][j] += grid[0][j-1];
        }

        for (int i = 1; i < m; i++) {
            for (int j = 1; j < m; j++) {
                grid[i][j] += Math.max(grid[i-1][j], grid[i][j-1]);
            }
        }

        return grid;
    }

    public static void main(String[] args) {
        int[][] a = {{1,2,5},{3,2,1}};
        int[][] grid = maxValue(a);
        System.out.println(grid);
    }
}