class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self, node):
        node.parent = self
        self.children.append(node)
    
    def print_tree_dfs(self):
        print(self.data)
        if self.children:
            for child in self.children:
                child.print_tree_dfs()
        
        
    def get_height(self):
        if not self.children:
            return 1
        height = 0
        for child in self.children:
            height = max(height, child.get_height())
        
        return height + 1
    
def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Surface"))
    laptop.add_child(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.add_child(TreeNode("iPhone"))
    cellphone.add_child(TreeNode("Google Pixel"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("LG"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)
    
    print(root.get_height())
    root.print_tree_dfs()
if __name__ ==  '__main__':
    build_product_tree()