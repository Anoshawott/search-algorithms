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
