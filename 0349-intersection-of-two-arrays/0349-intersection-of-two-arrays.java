import java.util.*;
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        
        Set<Integer> set1 = new HashSet<Integer>();
        Set<Integer> answer = new HashSet<Integer>();
        
        for(int ele: nums1){
            set1.add(ele);  
        }
     
        for(int ele: nums2){
            if(set1.contains(ele)){
                answer.add(ele);
            }
        }

        int[] ans = new int[answer.size()];
        int i = 0;
      
        for(int ele: answer)
           ans[i++] = ele;
        return ans; 
    }
}
