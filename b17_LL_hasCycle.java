/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public boolean hasCycle(ListNode head) {
        // fast and slow pointer may be O(n/2)
        ListNode slow = head, fast = head;
        
        while (fast!=null && fast.next!=null){
            slow = slow.next;
            fast = fast.next.next;
            
            if (slow == fast)
                return true;
        }
        return false;
    }
    
    public boolean hasCycleBrute(ListNode head) {
        // O(n) brute force: Go through each node and add save them, returning true there is a cycle if come across again
        HashSet<ListNode> nodeSet = new HashSet<ListNode>();
        
        while (head != null){
            if (nodeSet.contains(head))
                return true;
            nodeSet.add(head);
            head = head.next;
        }
        return false;
    }
}
