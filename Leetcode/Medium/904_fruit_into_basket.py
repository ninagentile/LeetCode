from collections import defaultdict


class Solution(object):
    def totalFruit(self, fruits):
        """
        Solve this problem by finding the largest subarray with at most
        2 distinct elements. Use a sliding window approach

        :type fruits: List[int]
        :rtype: int
        """

        first = 0
        last = 0
        counter = defaultdict(int)
        indexes = {}
        max_fruits = 0
        while last < len(fruits):
            current = fruits[last]

            # Slide the window
            counter[current] += 1
            indexes[current] = last

            # If a third type of fruit is found, update the window
            if len(counter) > 2:
                last_fruit = fruits[last - 1]

                # Find the fruit to remove
                fruit_to_remove = None
                for fruit in counter:
                    if (fruit != current) and (fruit != last_fruit):
                        fruit_to_remove = fruit
                        break

                # Get the index of fruit_to_remove
                idx_fruit_to_remove = indexes[fruit_to_remove]
                del indexes[fruit_to_remove]

                # Count the number of last_fruit to remove
                n_fruits_to_remove = idx_fruit_to_remove - first + 1
                n_fruits_to_remove -= counter[fruit_to_remove]

                # Remove all the fruit_to_remove from the counter
                del counter[fruit_to_remove]

                # Remove n_fruits_to_remove from last_fruit counter
                counter[last_fruit] -= n_fruits_to_remove

                # Shrink the window
                first = idx_fruit_to_remove + 1

            # Update the max count of fruits
            curr_n_fruits = sum(counter.values())
            max_fruits = max(max_fruits, curr_n_fruits)
            last += 1
        return max_fruits
