class Solution:
    def numberOfLines(self, widths, S):
        letterCount = 0
        lines = 1

        for index in range(len(S)):
            width = widths[ord(S[index]) - 97]
            letterCount += width

            if letterCount > 100:
                lines += 1
                letterCount = width

        return [lines, letterCount]

solution = Solution().numberOfLines([7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9], "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie")
print('You need {} lines and the width of the last line is {}'.format(solution[0], solution[1]))