"""
    书店店员有一张链表形式的书单，每个节点代表一本书，节点中的值表示书的编号。
    为更方便整理书架，店员需要将书单倒过来排列，
    就可以从最后一本书开始整理，逐一将书放回到书架上。
    请倒序返回这个书单链表。
    示例 1：
            输入：head = [3,6,4,1]
            输出：[1,4,6,3]
"""
from utils.list_node import ListNode


def reverse_book_list(head: ListNode):
    pre, cur = None, head
    while cur is not None:
        next_node = cur.next_node
        cur.next_node = pre
        pre = cur
        cur = next_node
    res = []
    while pre is not None:
        res.append(pre.value)
        pre = pre.next_node
    return res


head = ListNode.array_to_list_node([3, 6, 4, 1])
ListNode.print_list_node(head)
