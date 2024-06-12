class Sorter:
    def quicksort(self, bug_array, sort_key):
        if len(bug_array) <= 1:
            return bug_array
        else:
            pivot = bug_array[0]
            left = [x for x in bug_array[1:] if x[sort_key] < pivot[sort_key]]
            right = [x for x in bug_array[1:] if x[sort_key] >= pivot[sort_key]]
            return (
                self.quicksort(left, sort_key)
                + [pivot]
                + self.quicksort(right, sort_key)
            )
