#include <algorithm>
#include <vector>

class Solution {
public:
    vector<bool> kidsWithCandies(vector<int>& candies, int extraCandies) {
        auto max = *std::max_element(std::begin(candies), std::end(candies));
        vector<bool> result;
        
        for (auto i = candies.begin(); i != candies.end(); i++) {
            result.push_back(*i + extraCandies >= max);
        }
        
        return result;
    }
};