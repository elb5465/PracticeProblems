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
    public int kthSmallest(TreeNode root, int k) {
        // not using Collections.reverseOrder() here bc we want a min heap since we wanna get a small number 
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        
        // iterate through BST using a queue instead of recursion, add values to pq as we go along
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        pq.offer(root.val);
        
        while (q.size() != 0){
            TreeNode tn = q.poll();
            if (tn.left  != null) {
                pq.offer(tn.left.val);
                q.offer(tn.left);
            }
            if (tn.right  != null) {
                pq.offer(tn.right.val);
                q.offer(tn.right);
            }
        }

        // now simply iterate through the minHeap and pop until you wanna return the kth smallest element
        while (k>1)  {
            pq.poll();
            k --;
        }
        return pq.poll();
    }
}
