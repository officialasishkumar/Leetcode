class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int m = matrix.size();
        // finding Transpose of matrix
        for(int i = 0; i < m; i++){
            for(int j = i; j < m; j++){
                if( i != j){
                    swap(matrix[i][j], matrix[j][i]);
                }
            }
        }
        
        // reverse each row
        for(int i = 0; i < m; i++){
            reverse(matrix[i].begin(), matrix[i].end());
        }
    }
};