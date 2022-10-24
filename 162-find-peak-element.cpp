//162-find-peak-element.cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) 
    {
        vector<int> temp;
        temp=nums;
        int ans;
        sort(nums.begin(),nums.end());
        for(int i=0;i<temp.size();i++)
        {
            if(nums[nums.size()-1]==temp[i])
            {
                ans=i;
                goto done;
            }
        }
        done:
            return ans;
    }
};
