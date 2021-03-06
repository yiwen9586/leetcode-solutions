// 
// Generated by fetch-leetcode-submission project on GitHub.
// https://github.com/gitzhou/fetch-leetcode-submission
// Contact Me: aaron67[AT]aaron67.cc
// 
// Add Two Numbers
// https://leetcode.com/problems/add-two-numbers/
// 

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode newHead = new ListNode(0);
        ListNode cur1 = l1;
        ListNode cur2 = l2;
        ListNode cur = newHead;
        int carry = 0;
        while(cur1!=null || cur2!=null){
            int sum = 0;
            if(cur1 == null){
                sum = cur2.val + carry;
                cur2 = cur2.next;
            }
            else if(cur2 == null){
                sum = cur1.val + carry;
                cur1 = cur1.next;
            }
            else{ 
                sum = cur1.val + cur2.val + carry;
                cur1 = cur1.next;
                cur2 = cur2.next;
            }
            carry = sum / 10 ;
            cur.next = new ListNode(sum % 10);
            cur = cur.next;           
        }
       
        if(carry == 1)
            cur.next = new ListNode(1);
        
        return newHead.next; 
        
            
    }
}

