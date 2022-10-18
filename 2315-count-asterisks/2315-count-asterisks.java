class Solution {
    public int countAsterisks(String s) {
        int ans = 0;
        boolean f = true;
        for(int i = 0;i<s.length();i++){
            if(s.charAt(i)=='|'){
                f ^= true;
            }else if(f&&s.charAt(i)=='*') {
                ans++;
            }
        }
        return ans;
    }
}