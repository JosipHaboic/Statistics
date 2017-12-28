''' Not finsihed '''
class BiNode:
    pass

class BiNode:

    EMPTY_ELEMENT = None

    def __init__(self, value=None, parent=None):
        self.value = value
        self.parent = parent
        self.left = BiNode.EMPTY_ELEMENT
        self.right = BiNode.EMPTY_ELEMENT
        self.compare_function = lambda x,y: True if x > y else False

    def insert(self, value) -> None:
        if self.compare_function(self.value, value):
            if self.left != BiNode.EMPTY_ELEMENT:
                self.left.insert(value)
            else:
                self.left = BiNode(value, self)
        else:
            if self.right != BiNode.EMPTY_ELEMENT:
                self.right.insert(value)
            else:
                self.right = BiNode(value, self)

    @staticmethod
    def search_recursively(node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            BiNode.search_recursively(node.left, value)
        return BiNode.search_recursively(node.right, value)

    @staticmethod
    def from_list(data: list) -> BiNode:
        tree = BiNode(value=data[0])
        for i in data[0:]:
            tree.insert(i)
        return tree


    def is_leaf(self) -> bool:
        if (self.left == BiNode.EMPTY_ELEMENT) and (self.right == BiNode.EMPTY_ELEMENT):
            return True
        else:
            return False

    def is_root(self) -> bool:
        if self.parent == None:
            return True
        else:
            return False

    def get_children(self) -> tuple:
        return self.left, self.right

    def get_children_values(self) -> tuple:
        return (
            BiNode.EMPTY_ELEMENT if self.left == BiNode.EMPTY_ELEMENT else self.left.value,
            BiNode.EMPTY_ELEMENT if self.right == BiNode.EMPTY_ELEMENT else self.right.value
        )

    def generate_side(self, side='left', include_empty=False):
        if side == 'left':
            if self.left == BiNode.EMPTY_ELEMENT:
                if include_empty:
                    yield BiNode.EMPTY_ELEMENT
            else:
                yield from self.left.generate_values()
        elif side == 'right':
            if self.right == BiNode.EMPTY_ELEMENT:
                if include_empty:
                    yield BiNode.EMPTY_ELEMENT
            else:
                yield from self.right.generate_values()
        else:
            print('Invalid side choice of {}'.format(side))


    def generate_values(self, traversal='preorder', include_empty=False):
        if traversal == 'preorder':
            yield self.value
            yield from self.generate_side('left', include_empty=include_empty)
            yield from self.generate_side('right', include_empty=include_empty)

        elif traversal == 'postorder':
            yield from self.generate_side('left', include_empty=include_empty)
            yield from self.generate_side('right', include_empty=include_empty)
            yield self.value

        elif traversal == 'inorder':
            yield from self.generate_side('left', include_empty=include_empty)
            yield self.value
            yield from self.generate_side('right', include_empty=include_empty)


    def generate_list(self, traversal='preorder'):
        children = self.get_children()
        if traversal == 'preorder':
            yield [self, *children]
        if traversal == 'postorder':
            yield [*children, self]
        if traversal == 'inorder':
            yield [children[0], self, children[1]]

    def __repr__(self):
        return '[{},{},{}]\n'.format(self.left, self.value, self.right)

    def __iter__(self):
        yield self
        yield self.left
        yield self.right

