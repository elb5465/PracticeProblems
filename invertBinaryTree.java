// https://leetcode.com/problems/invert-binary-tree/discuss/62707/Straightforward-DFS-recursive-iterative-BFS-solutions

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode myInvertTree(TreeNode root) {
        if (root == null) return null;

        TreeNode temp;

        if (root.left != null && root.right != null)
            temp = new TreeNode();
            temp = root.left;
            root.left  = root.right;
            root.right = temp;

        root.left  = invertTree(root.left);
        root.right = invertTree(root.right);

        return root;
    }

    // simpler recursive
    public TreeNode invertTree(TreeNode root) {
        if (root == null)  return null;

        final TreeNode left = root.left, right = root.right;
        root.left = invertTree(root.right);
        root.right = invertTree(root.left);

        return root;
    }

    // Using a Stack / Deque
    public TreeNode invertTree(TreeNode root) {
        if (root == null)  return null;

        final Deque<TreeNode> stack = new LinkedList<>();
        // final Stack<TreeNode> stack = new Stack<>();  // works same as above   
        
        stack.push(root);

        while(!stack.isEmpty()) {
            final TreeNode node = stack.pop();
            System.out.println(node.val);

            final TreeNode left = node.left;
            node.left = node.right;
            node.right = left;

            if (node.left  != null)  stack.push(node.left);
            if (node.right != null)  stack.push(node.right);
        }
        return root;
    }
}
