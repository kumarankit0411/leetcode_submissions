class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)
        f_arr = [fruits[0], fruits[1]]
        last_known_tree_index = 1 if fruits[0] != fruits[1] else 0
        i=0
        max_size = 0

        for j in range(len(fruits)):
            current_tree = fruits[j]
            if current_tree not in f_arr:
                i = last_known_tree_index
                f_arr = [fruits[j-1], current_tree]

            if j > 0 and fruits[j] != fruits[j - 1]:
                last_known_tree_index = j

            if max_size < j - i + 1:
                max_size = j - i + 1

        return max_size