from typing import List, Optional

# 2. Add Two Numbers
"""
2. Add Two Numbers
Solved
Medium
Topics
Companies
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 
Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        result = ListNode(0)
        temp_result = result
        carry = 0

        while l1 != None or l2 != None or carry != 0:

            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry

            carry = columnSum // 10
            temp_result.val = columnSum % 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if l1 != None or l2 != None or carry != 0:
                newNode = ListNode(0)
                temp_result.next = newNode
                temp_result = newNode

        return result
# ----------------------------------------------------------------------------------------------------------------------
# 4. Median of Two Sorted Arrays
"""
4. Median of Two Sorted Arrays
Solved
Hard
Topics
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""
def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    result = 0.0
    final_list = []

    list1_counter = 0
    list1_finished = False if len(nums1) > 0 else True
    list2_counter = 0
    list2_finished = False if len(nums2) > 0 else True
    i = 0

    while list1_counter <= len(nums1) - 1 or list2_counter <= len(nums2) - 1:
        if list2_finished == True or list1_finished == False and nums1[list1_counter] < nums2[list2_counter]:
            final_list.append(nums1[list1_counter])
            list1_counter += 1
            if list1_counter == len(nums1):
                list1_finished = True
        elif list2_finished == False:
            final_list.append(nums2[list2_counter])
            list2_counter += 1
            if list2_counter == len(nums2):
                list2_finished = True
        i += 1

    if len(final_list) % 2 == 0:
        result = (final_list[len(final_list) // 2] + final_list[len(final_list) // 2 - 1]) / 2
    else:
        result = final_list[len(final_list) // 2]
    return result
# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    temp = 0
