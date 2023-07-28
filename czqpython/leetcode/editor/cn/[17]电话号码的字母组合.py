# 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。 
# 
#  给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：digits = "23"
# 输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
#  
# 
#  示例 2： 
# 
#  
# 输入：digits = ""
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：digits = "2"
# 输出：["a","b","c"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= digits.length <= 4 
#  digits[i] 是范围 ['2', '9'] 的一个数字。 
#  
#  Related Topics 哈希表 字符串 回溯 👍 1710 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        path = []
        digitMap = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mon",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        def dfs(index):
            if index >= len(digits):
                res.append("".join(path))
                return
            digit = int(digits[index])
            letters = digitMap[digit]
            for letter in letters:
                path.append(letter)
                dfs(index + 1)
                path.pop()
        if len(digits) == 0: return res
        dfs(0)
        return res

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    s = Solution()