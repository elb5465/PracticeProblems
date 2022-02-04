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
    public ListNode middleNode(ListNode head) {
        Stack<ListNode> st = new Stack<ListNode>();
        int cnt = 1; 
        ListNode p = null;
        
        while (head != null){
            st.add(head);
            head = head.next;
            cnt ++;
        }
        
        cnt = cnt / 2;
        while (cnt != 0){
            p = st.pop();
            cnt --;
            System.out.println("" + p.val);
            System.out.println("cnt: " + cnt);
        }
        
        return p;
        
    }
}
