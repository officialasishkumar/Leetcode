class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        Map<Integer,Integer> map =  new HashMap<>();
        int i=0,j=0;
        while(i<nums.length){
            if(map.getOrDefault(nums[i],0)>=1) return true;
            map.put(nums[i],map.getOrDefault(nums[i],0)+1);
            if(i-j==k) {
                map.put(nums[j],map.getOrDefault(nums[j],0)-1);
                j++;
            }
            i++;
        }
        return false;
    }
}