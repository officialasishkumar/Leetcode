class Solution {
    int ans;
    public int maxLength(List<String> arr) {
        ans = 0;
        helper(arr,0,new boolean[26]);
        return ans;
    }
    public void helper(List<String> arr,int i,boolean[] ch){
        if(i==arr.size()) {
            int a =0;
            for(boolean c:ch) a+=c?1:0;
            ans = Math.max(ans,a);
            return;
        }
        boolean[] nch = Arrays.copyOf(ch,26);
        boolean f = true;
        for(int j=0;j<arr.get(i).length();j++){
            int k = arr.get(i).charAt(j)-'a'; 
            if(nch[k]){
                f = false;
                break;
            }
            nch[k] = true;
            
        }
        helper(arr,i+1,ch);
        if(f) helper(arr,i+1,nch);
    }
}