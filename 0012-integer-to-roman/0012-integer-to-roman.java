class Solution {
    public String intToRoman(int num) {
        int[] arr = {1,4,5,9,10,40,50,90,100,400,500,900,1000};
        String[] s = {"I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"};
        StringBuilder sb = new StringBuilder();
        for(int i=arr.length-1;i>=0;i--){
            while(num>=arr[i]) {
                sb.append(s[i]);
                num -= arr[i];
            }
        }
        return sb.toString();
    }
}