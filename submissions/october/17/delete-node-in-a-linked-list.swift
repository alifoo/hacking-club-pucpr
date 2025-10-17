/*
    Rafael Longhi
    Curso: BCC
    Problema: https://leetcode.com/problems/delete-node-in-a-linked-list
*/

class Solution {

    // Como nós não temos o primeiro node da lista,
    // nós vamos copiar os valores dos nodes next
    // para o atual, um por um, para sobrar um node 
    // duplicado no final, que será retirado.
    func deleteNode(_ node: ListNode?) {
        guard let node = node,
              let nextNode = node.next else { return }
        
        node.val = nextNode.val

        if nextNode.next == nil {
            node.next = nil
        } else {
            deleteNode(nextNode)
        }
    }
}