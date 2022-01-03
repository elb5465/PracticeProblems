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
    public boolean isSameTree(TreeNode p, TreeNode q) {
        
        // if recursed to end and both still match, done
        if (p==null && q==null)
            return true;
        
        // if recursed to end and only one is null, end false
        if (p==null || q==null)
            return false;
        
        // if current nodes are not equal, return false
        if (p.val != q.val)
            return false;
        
        // o.w. continue to recurse down both sides comparing each node accordingly
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        
    }
}
