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
    ListNode* mergeNodes(ListNode* head) {
        ListNode* prev = new ListNode();
        ListNode* ans = prev;
        while(head){
            head = head->next;
            if(!head) break;
            while(head && head->val){
                prev->val+=head->val;
                head = head->next;
            }
            if(head->next == NULL) break;
            prev->next = new ListNode();
            prev = prev->next;
        }
        return ans;
    }
};