class Solution {
    public boolean checkSubarraySum(int[] nums, int k) {
        Set<Integer> set = new HashSet<>();
        int cur = 0,pre = 0;
        for(int a:nums){
            cur = (cur + a) % k;
            if(set.contains(cur)) return true;
            set.add(pre);
            pre = cur;
        }
        return false;
    }
}