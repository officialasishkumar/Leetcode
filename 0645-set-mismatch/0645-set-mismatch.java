class Solution {
    public int[] findErrorNums(int[] nums) {
        int[] ans = new int[2];
        int xor = 0;
        Set<Integer> set = new HashSet<>();
        for(int i=0;i<nums.length;i++){
            if(set.contains(nums[i]))
                ans[0]= nums[i];
            else{
                set.add(nums[i]);
                xor ^= nums[i];
            }
            xor ^= i+1;
        }
        ans[1] = xor;
        return ans;
    }
}
