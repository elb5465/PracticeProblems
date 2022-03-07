/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode curr = head;
        
        while (curr != null){
            // save a node on the 2nd in
            ListNode n = curr.next; 
            
            // make ptr from head point to null
            curr.next = prev;
            
            // make the head the previous value
            prev = curr;
            
            // adjust the head ptr to now move forward through the list
            curr = n;
        }
        
        return prev;
    }
}
