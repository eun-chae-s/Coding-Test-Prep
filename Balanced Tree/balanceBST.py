"""
Leetcode 1382. Balance a Binary Search Tree

Given the root of a binary search tree, return a balanced binary search tree
with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every
node never differs by more than 1.

"""
from typing import Optional


class TreeNode:
    """
    Class for a Tree node
    """

    def __init__(self, val=0, left=None, right=None) -> None:
        """
        :param val: a value of the tree node
        :param left: a left subtree of this node
        :param right: a right subtree of this node
        """
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    A class for the list of functions
    """

    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
            A function that creates a new AVL Tree
        """
        sorted_array = self.getSortedArray(root)

        # Step 2. sorted array -> height-balanced BST (Leetcode #108)
        return self.sortedArrayToBST(sorted_array)

    def getSortedArray(self, root: TreeNode) -> list[int]:
        """
            A function that gets the sorted array from BST
        """
        if root is None:
            return []
        else:
            return self.getSortedArray(root.left) + [root.val] + self.getSortedArray(root.right)

    def sortedArrayToBST(self, nums: list[int]) -> Optional[TreeNode]:
        """
        Get the BST from the sorted array
        :param nums: sorted array of integers
        :return: a height-balanced BST
        """
        if nums == []:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0], None, None)
        else:
            mid = len(nums) // 2

            left = self.sortedArrayToBST(nums[:mid])
            right = self.sortedArrayToBST(nums[mid + 1:])
            return TreeNode(nums[mid], left, right)
