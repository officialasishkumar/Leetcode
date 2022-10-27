class Solution {
  public String shortestCommonSupersequence(String S1, String S2) {
      
    int n = S1.length();
      int m = S2.length();
      char[] ch1 = S1.toCharArray();
      char[] ch2 = S2.toCharArray();
      
      int[][] t = new int[n+1][m+1];
      for(int i = 0; i<n+1; i++){
          for(int j = 0; j<m+1; j++){
              if(i==0||j==0)
                  t[i][j] = 0;
          }
      }
      
      for(int i = 1; i<n+1; i++){
          for(int j = 1; j<m+1; j++){
              if(ch1[i-1] == ch2[j-1]){
                  t[i][j] = 1 + t[i-1][j-1];
              }
              else{
                  t[i][j] = Math.max(t[i-1][j], t[i][j-1]);
              }
          }
      }
      
      int i = n;
      int j = m;
      String ans = "";
      
      while(i>0 && j>0){
          if(ch1[i-1]==ch2[j-1]){
              ans=ch1[i-1]+ans;
              i--;
              j--;
          }
          
          else if(t[i-1][j]>t[i][j-1]){
              ans=ch1[i-1] + ans;
              i--;
          }

          else{
              ans=ch2[j-1]+ans;
              j--;
          }   
      }
      
      while(i>0){
          ans=ch1[i-1] + ans;
          i--;
      }
      
      while(j>0){
          ans=ch2[j-1]+ans;
          j--;
      }
     return ans;
  }
}