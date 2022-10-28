class Solution {
  public int[] createTargetArray(int[] nums, int[] index) {
      
      ArrayList<Integer> target = new ArrayList<>();
      
      for(int i = 0; i<nums.length; i++){
          target.add(index[i], nums[i]);
      }
      
      int[] arr = target.stream().mapToInt(i -> i).toArray();
      return arr;
  }
}