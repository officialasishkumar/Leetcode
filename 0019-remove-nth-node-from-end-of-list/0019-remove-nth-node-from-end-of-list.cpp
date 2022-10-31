/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode *slow=head, *fast=head;
        int k=n;
        while(k){
            //making fast and slow distant by 'n' units
            fast=fast->next;
            k--;
        }
        if(!fast){
            //if fast becomes NULL then we need to remove the first node
            return head->next;
        }
        while(fast && fast->next){
            slow=slow->next;
            fast=fast->next;
        }
        //we need to remove the node next to 'slow'
        slow->next=slow->next->next;
        return head;
    }
};

// Do star this repo
