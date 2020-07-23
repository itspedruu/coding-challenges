class Solution {
public:
    int numberOfSteps (int num) {
        if (num == 0) {
            return 0;
        }
        
        int steps;
        
        while (num != 0) {
            if (num % 2 == 0) {
                num /= 2;
                steps++;
            } else {
                num = (num - 1) / 2;
                steps += num == 0 ? 1 : 2;
            }
        }
        
        return steps;
    }
};