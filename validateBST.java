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
    public boolean isValidBST(TreeNode root) {
        return dfs(root, Long.MIN_VALUE, Long.MAX_VALUE);    
    }
    
    
    public boolean dfs(TreeNode root, long min, long max){
        if (root==null) return true;
        
        if ((root.val <= min) || (root.val >= max)) return false;
            
        return (dfs(root.left, min, root.val) && dfs(root.right, root.val, max));
    }
    
    
}


//     int orv = -1;
//     public boolean isValidBST(TreeNode root) {
//         orv = root.val;
//         TreeNode l = root.left;
//         TreeNode r = root.right;   
        
//         if (root==null) return true;
        
//         if ((l!=null && l.val==orv) || (r!=null && r.val == orv))
//             return false;
        
//         if (!dfs(root.left, 0) || !dfs(root.right, 1))
//             return false;
        
//         return true;
//     }
    
//     public boolean dfs(TreeNode root, int side){
//         if (root == null) 
//             return true;

//         TreeNode l = root.left;
//         TreeNode r = root.right;   
        
//         //System.out.println("root: " + root.val + " side: " + side);

//         if (l != null) {
//             //System.out.println("l: " + l.val + " \nr: " + r.val + "\n");
//             if (l.val >= root.val || l.val == orv)
//                 return false;
            
//             //check if nested left value is less than original on right side
//             if (orv!=root.val && l.val <= orv && side == 1)
//                 return false;


//             if (!dfs(root.left, side))
//                 return false;
//         }
        
//         if (r != null){
//             if (r.val <= root.val || r.val == orv)
//                 return false;
            
//             //check if nested right value is less than original on left side
//             if (orv!=root.val && r.val >= orv && side==0)
//                 return false;
            
//             if (!dfs(root.right, side))
//                 return false;
//         }
//         return true;
//     }
// }
