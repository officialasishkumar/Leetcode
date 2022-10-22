class Solution {
public:
string minWindow(string s, string t) {
int i=0,j=0,MinL=INT_MAX,start=0;
unordered_map<char,int> mp;
for(int i = 0; i < t.size(); i++){
mp[t[i]]++;
}
int count=mp.size();

    while(j<s.length()){
       if(mp.find(s[j])!=mp.end()){
         mp[s[j]]--;
         if(mp[s[j]]==0)
            count--;
     }
         if(count==0){
            // MinL=min(MinL,j-i+1);
            if(MinL>j-i+1){
                MinL=j-i+1;
                start=i;
            }
            while(count==0){
                if(mp.find(s[i])!=mp.end()){
                    mp[s[i]]++;
                    if(mp[s[i]]==1){
                        count++;
                        // MinL=min(MinL,j-i+1);
                         if(MinL>j-i+1){
                            MinL=j-i+1;
                            start=i;
                        } 
                    }
                    i++;
                }
                else
                    i++;
            }
        }
        j++;
    }
    string str="";
    if(MinL!=INT_MAX)
        return str.append(s.substr(start,MinL));
    else
        return str;
}
};
