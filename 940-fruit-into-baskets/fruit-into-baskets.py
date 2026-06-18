class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        max_fruits = 0
        baskets = {}

        for right in range(len(fruits)):
            curr_fruit = fruits[right]
            baskets[curr_fruit] = baskets.get(curr_fruit, 0)+1
            
            while len(baskets)>2:
                left_fruit = fruits[left]
                baskets[left_fruit] -= 1

                if baskets[left_fruit] == 0:
                    del baskets[left_fruit]

                left +=1

            win_size = right - left + 1
            max_fruits = max(max_fruits, win_size)

        return max_fruits