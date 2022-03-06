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
    // BFS iterative (queue)
    public TreeNode invertTreeBFS(TreeNode root) {
        if (root == null)  return null;
        
        Queue<TreeNode> q = new LinkedList<TreeNode>();
        q.offer(root);
        
        while (!q.isEmpty()){
            TreeNode curr = q.poll();
            
            TreeNode temp = curr.left;
            curr.left = curr.right;
            curr.right = temp;
            
            if (curr.left !=null) q.offer(curr.left);
            if (curr.right!=null) q.offer(curr.right);
            
        }
        
        return root;
        
    }
    
    
    
    // DFS Iterative (stack)
    public TreeNode invertTreeDFS(TreeNode root) {
        if (root == null)  return null;

        Stack<TreeNode> st = new Stack<>();
        st.push(root);
        
        while (!st.isEmpty()){
            TreeNode curr = st.pop();
            
            // switch left and right nodes before pushing
            TreeNode temp = curr.left;
            curr.left = curr.right;
            curr.right = temp;
            
            if (curr.left != null) st.push(curr.left);
            if (curr.right != null) st.push(curr.right);
            
            
        }
        
        return root;
    }
    
    
    
    // DFS recursive
    public TreeNode invertTree(TreeNode root) {
        if (root==null) return null;
        
        TreeNode temp = root.left;
        root.left = root.right;
        root.right = temp;
        
        invertTree(root.left);
        invertTree(root.right);
        
        return root;
    }
}
