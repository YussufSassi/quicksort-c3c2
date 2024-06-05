class Sorter:
    def quicksort(self, array):
        if len(array) <= 1:
            return array
        else:
            pivot = array[0]
            left = [x for x in array[1:] if x < pivot]
            right = [x for x in array[1:] if x >= pivot]
            return self.quicksort(left) + [pivot] + self.quicksort(right)
