// https://leetcode.com/problems/reverse-linked-list-ii/submissions/

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
    public ListNode reverseBetween(ListNode head, int left, int right) {
        if (head == null)
            return null;
        
        if (left == right)
            return head;
    
        ListNode prev = null;
        ListNode curr = head;
        
        while (left > 1){
            prev = curr;
            curr = curr.next;
            left--; right--;
        }
        
        ListNode leftConnect   = prev;
        ListNode tailToReverse = curr;
        
        while (right > 0){
            ListNode n = curr.next;
            curr.next = prev;
            prev = curr;
            curr = n;
            right--;
        }
        
        if (leftConnect != null)
            leftConnect.next = prev;
        else
            head = prev;
        
        tailToReverse.next = curr;
        return head;
    }
}
