class node:

    def __init__(self, value, parent=None):
        self.value=value
        self.parent=parent
        self.children=[]
    
    def add_child(self, child):
        children=self.children
        children.append(child)
        