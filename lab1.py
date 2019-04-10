def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == []:
       return None
   if int_list is None:
       raise ValueError
   maxNum = int_list[0]
   for i in range(len(int_list)):
       if int_list[i] > maxNum:
           maxNum = int_list[i]
   return maxNum


def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
       raise ValueError
   if not int_list:
       return int_list
   last = [int_list[-1]]
   rest = int_list[:-1]
   return last + reverse_rec(rest)



def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError
   figure out the mid which is low + high // 2. That mid index returns a number.
   if it matches the target return that index. if its not equal figure out which direction
   if its greater than adjust the low index up. Low = mid + 1. Then repeat the low + high // 2.
   check the number again and repeat. if the mid == low index, then target number is to the other side.
   if at any point low is greater than high then terminate. """
   if int_list is None:
       return ValueError
   mid_index = (int_list.index(low) + int_list.index(high)) // 2
   if int_list[mid_index] == target:
       return mid_index
   elif int_list.index(low) >= int_list.index(high) or mid_index == int_list.index(low):
       return None
   if int_list[mid_index] < target:
       low = int_list[mid_index]
       return bin_search(target, low, high, int_list)
   elif int_list[mid_index] > target:
       high = int_list[mid_index]
       return bin_search(target, low, high, int_list)

