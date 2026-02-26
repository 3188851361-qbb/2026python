class Node():
    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem  # 节点值
        self.lchild = lchild  # 左孩子
        self.rchild = rchild  # 右孩子


class BinaryTree():
    def __init__(self, root=None):
        self.root = root
        self.help_queue = []  # 辅助数组

    def level_build_tree(self, node: Node):
        if self.root is None:
            self.root = node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild = node  # 放入左孩子
            else:
                self.help_queue[0].rchild = node  # 放出右孩子
                del self.help_queue[0]  # 移出满孩子的父节点

    def pre_order(self, current_node: Node):  # 前序遍历  也就是深度优先遍历
        if current_node:
            print(current_node.elem, end=' ')
            self.pre_order(current_node.lchild)
            self.pre_order(current_node.rchild)

    def lever_order(self):
        help_queue = []
        help_queue.append(tree.root)
        while help_queue:
            out_node:Node = help_queue.pop(0)
            print(out_node.elem, end=' ')
            if out_node.lchild:
                help_queue.append(out_node.lchild)
            if out_node.rchild:
                help_queue.append(out_node.rchild)


    def middle_order(self, current_node: Node):  # 中序遍历
        if current_node:
            self.middle_order(current_node.lchild)
            print(current_node.elem, end=' ')
            self.middle_order(current_node.rchild)

    def last_order(self, current_node: Node):  # 中序遍历
        if current_node:
            self.last_order(current_node.lchild)
            self.last_order(current_node.rchild)
            print(current_node.elem, end=' ')


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        node = Node(i)
        tree.level_build_tree(node)
    tree.pre_order(tree.root)
    print()
    tree.middle_order(tree.root)
    print()
    tree.last_order(tree.root)
    print()
    tree.lever_order()
