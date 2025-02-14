class Solution 
{
    private:
        unordered_map<int, vector<int>> indices;

    public:    
        Solution(vector<int>& nums) 
        {
            int l = nums.size();
            for (int i = 0; i < l; ++i) 
            {
                this -> indices[nums[i]].push_back(i);
            }
        }
        
        int pick(int target) 
        {
            int l = indices[target].size();
            // pick an index at random
            int randomIndex = indices[target][rand() % l];
            return randomIndex;
        }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * int param_1 = obj->pick(target);
 */

// Link to the problem: https://leetcode.com/problems/random-pick-index/
