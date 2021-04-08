class tree:
    
    def __init__(self, root):
        self.root=root

    def root_pathway(self, child):
        root=self.root

        pathway=[]
        while child != root:
            pathway.append(child.value)
            child = child.parent
        
        pathway.append(child.value)

        return pathway

    def depth(self, node):
        root=self.root

        node_count=0
        while node != root:
            node_count+=1
            node=node.parent

        return node_count