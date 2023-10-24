```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        _sum = 0

        for start_node in [l1, l2]:
            _list = []
            node = start_node
            while node:
                _list.append(str(node.val))
                node = node.next

            _list.reverse()
            _sum += int(''.join(_list))

        result = list(map(int, list(str(_sum))))
        result.reverse()

        node = ListNode()
        next_node = node

        for idx, n in enumerate(result):
            next_node.val = n
            if idx != len(result) - 1:
                next_node.next = ListNode()
                next_node = next_node.next

        return node
```
