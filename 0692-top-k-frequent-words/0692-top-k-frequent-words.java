class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        Map<String,Integer> map = new HashMap<>();
        for(String s:words){
            int a = map.getOrDefault(s,0)+1;
            map.put(s,a);
        }
        List<pair> l = new ArrayList<>();
        for(String st:map.keySet()){
            l.add(new pair(st,map.get(st)));
        }
        Collections.sort(l,(a,b)->a.v==b.v?a.s.compareTo(b.s):b.v-a.v);
        List<String> list = new  ArrayList<>();
        for(int i=0;i< k;i++) list.add(l.get(i).s);
        return list;
    }
    class pair{
        String s;
        int v;
        pair(String s, int v){
            this.s = s;this.v = v;
        }
    }
}