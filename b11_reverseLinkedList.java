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
        // need to save a prev var to point to while reversing
        ListNode prev = null;
        
        // save next node first, so you can adjust current pointer without losing the next node
        while (head != null){
            ListNode next = head.next;
            head.next = prev;
            prev = head;
            head = next;
        }
        
        // returning previous bc loop breaks when head = null, therefore last valid node is the previous 
        return prev;
    }
}
