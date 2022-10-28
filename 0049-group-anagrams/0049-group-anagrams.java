class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        for(String s:strs){
            char[] ch = s.toCharArray();
            Arrays.sort(ch);
            String a = new String(ch);
            if(map.containsKey(a)){
                ans.get(map.get(a)).add(s);
            }else{
                ans.add(new ArrayList<>());
                int n = ans.size()-1;
                ans.get(n).add(s);
                map.put(a,n);
            }
            
        }
        return ans;
    }
}