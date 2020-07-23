#include <map>

class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        std::map<int, int> seen;
        int pairs = 0;
        
        for (auto i = nums.begin(); i != nums.end(); i++) {
            pairs += seen[*i];
            seen[*i] += 1;
        }
        
        return pairs;
    }
};