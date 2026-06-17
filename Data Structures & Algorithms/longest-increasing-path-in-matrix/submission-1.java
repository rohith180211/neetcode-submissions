class Solution {
    private int[][] dirs = {{1,0}, {-1,0}, {0,1}, {0,-1}};
    private int[][] dp;
    
    public int longestIncreasingPath(int[][] matrix) {
        int n = matrix.length, m = matrix[0].length;
        dp = new int[n][m];
        int maxPath = 0;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                maxPath = Math.max(maxPath, dfs(matrix, i, j, n, m));
            }
        }
        return maxPath;
    }
    
    private int dfs(int[][] matrix, int i, int j, int n, int m) {
        if (dp[i][j] != 0) return dp[i][j];
        
        int maxLen = 1; // at least the current cell
        for (int[] d : dirs) {
            int ni = i + d[0];
            int nj = j + d[1];
            if (ni >= 0 && nj >= 0 && ni < n && nj < m && matrix[ni][nj] > matrix[i][j]) {
                maxLen = Math.max(maxLen, 1 + dfs(matrix, ni, nj, n, m));
            }
        }
        dp[i][j] = maxLen;
        return maxLen;
    }
}
