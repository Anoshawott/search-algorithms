from node_assignment import node
from tree_generation import tree

class action_space:
    def __init__(self, start, goal, forbidden=None):
        self.start=start
        self.goal=goal
        self.forbidden=forbidden


    def expand_children(self, number, changed=None, root_path=None):
        children=[]
        new_digits=[]
        k = 0
        while k != len(number):
            check=0
            temp_digits=[]
            i = number[k]
            integer=int(i)
            if integer != 9:
                above_i=integer+1
                temp_digits.append(str(above_i))
                check+=1
            if integer != 0:
                below_i=integer-1
                temp_digits.append(str(below_i))
                check+=1
            if check==1:
                temp_digits.append(0)
            temp_digits.append(check)
            new_digits.append(temp_digits)
            k+=1

        if changed==None:    
            i=0
            while i != len(number):
                # print(new_digits)
                if i==0:
                    if new_digits[i][2]==2:
                        new_number1=new_digits[i][1]+number[1]+number[2]
                        new_number2=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0,root_path])
                        children.append([new_number2,0,root_path])
                    elif new_digits[i][2]==1:
                        new_number1=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0,root_path])
                elif i==1:
                    if new_digits[i][2]==2:
                        new_number1=number[0]+new_digits[i][1]+number[2]
                        new_number2=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1,root_path])
                        children.append([new_number2,1,root_path])
                    elif new_digits[i][2]==1:
                        new_number1=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1,root_path])
                elif i==2:
                    if new_digits[i][2]==2:
                        new_number1=number[0]+number[1]+new_digits[i][1]
                        new_number2=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2,root_path])
                        children.append([new_number2,2,root_path])
                    elif new_digits[i][2]==1:
                        new_number1=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2,root_path])
                i+=1
        
        elif changed==0:
            i=0
            while i != len(number):
                if i==1:
                    if new_digits[i][2]==2:
                        new_number1=number[0]+new_digits[i][1]+number[2]
                        new_number2=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1,root_path])
                        children.append([new_number2,1,root_path])
                    elif new_digits[i][2]==1:
                        new_number1=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1,root_path])
                elif i==2:
                    if new_digits[i][2]==2:
                        new_number1=number[0]+number[1]+new_digits[i][1]
                        new_number2=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2,root_path])
                        children.append([new_number2,2,root_path])
                    elif new_digits[i][2]==1:
                        new_number1=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2,root_path])
                i+=1

        elif changed==1:
            i=0
            while i != len(number):
                if i==0:
                    if new_digits[i][2]==2:
                        new_number1=new_digits[i][1]+number[1]+number[2]
                        new_number2=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0,root_path])
                        children.append([new_number2,0,root_path])
                    elif new_digits[i][2]==1:
                        new_number1=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0,root_path])
                elif i==2:
                    if new_digits[i][2]==2:
                        new_number1=number[0]+number[1]+new_digits[i][1]
                        new_number2=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2,root_path])
                        children.append([new_number2,2,root_path])
                    elif new_digits[i][2]==1:
                        new_number1=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2,root_path])
                i+=1

        elif changed==2:
            i=0
            while i != len(number):
                if i==0:
                    if new_digits[i][2]==2:
                        new_number1=new_digits[i][1]+number[1]+number[2]
                        new_number2=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0,root_path])
                        children.append([new_number2,0,root_path])
                    elif new_digits[i][2]==1:
                        new_number1=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0,root_path])
                elif i==1:
                    if new_digits[i][2]==2:
                        new_number1=number[0]+new_digits[i][1]+number[2]
                        new_number2=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1,root_path])
                        children.append([new_number2,1,root_path])
                    elif new_digits[i][2]==1:
                        new_number1=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1,root_path])
                i+=1

        # print('Number', number)
        # print('New digits', new_digits)
        # print('Children', children)
        return children, root_path


    def BFS(self):
        # print("BFS Method")
        starting_node=node(value=self.start)
        Tree = tree(root=starting_node)
        fringe=[[self.start, None, starting_node]]
        expanded=[]

        while len(fringe)!=0:
            i=fringe[0]
            if i[0]==self.goal:
                expanded.append(i)

                try:
                    # presenting expanded nodes
                    beginning=0
                    for i in expanded:
                        if beginning==0:
                            final_str=i[0]
                            beginning+=1
                        else:
                            final_str=final_str+','+i[0]

                    # presenting path of nodes
                    pathway=Tree.root_pathway(child=expanded[-1][2])

                    beginning=0
                    for i in reversed(pathway):
                        if beginning==0:
                            path_str=i
                            beginning+=1
                        else:
                            path_str=path_str+','+i

                except:        
                    print('Nothing to process...')

                break
            if len(expanded)==1000:
                return print('Limit has been reached.')
            # print('------------------')
            # print('fringe', fringe)
            children, parent_node=self.expand_children(number=i[0], changed=i[1], root_path=i[2])
            if self.forbidden==None:
                for k in children:
                    child_node=node(value=k[0], parent=parent_node)
                    k[2]=child_node
                    parent_node.add_child(child_node)
                    fringe.append(k)
            else:
                j=0
                while len(children)!=j:
                    if children[j][0] in self.forbidden:
                        del children[j]
                        continue
                    else:
                        child_node=node(value=children[j][0], parent=parent_node)
                        children[j][2]=child_node
                        parent_node.add_child(child_node)
                        fringe.append(children[j])
                        j+=1
            expanded.append(fringe[0])
            del fringe[0]            
        
        else:
            return print('No solution found.')

        return print(path_str+'\n'+final_str)






    def DFS(self):
        # print("DFS Method")
        starting_node=node(value=self.start)
        Tree = tree(root=starting_node)
        fringe=[[self.start, None, starting_node]]
        expanded=[]

        while len(fringe)!=0:
            i=fringe[0]
            if i[0]==self.goal:
                expanded.append(i)
                try:
                    # presenting expanded nodes
                    beginning=0
                    for i in expanded:
                        if beginning==0:
                            final_str=i[0]
                            beginning+=1
                        else:
                            final_str=final_str+','+i[0]

                    # presenting path of nodes
                    pathway=Tree.root_pathway(child=expanded[-1][2])

                    beginning=0
                    for i in reversed(pathway):
                        if beginning==0:
                            path_str=i
                            beginning+=1
                        else:
                            path_str=path_str+','+i

                except:        
                    print('Nothing to process...')

                break
            if len(expanded)==1000:
                return print('Limit has been reached.')
            # print('------------------')
            # print('fringe', fringe)
            children, parent_node=self.expand_children(number=i[0], changed=i[1], root_path=i[2])
            children.reverse()
            expanded.append(fringe[0])
            del fringe[0]
            if self.forbidden==None:
                for k in children:
                    child_node=node(value=k[0], parent=parent_node)
                    k[2]=child_node
                    parent_node.add_child(child_node)
                    fringe.insert(0,k)
            else:
                j=0
                while len(children)!=j:
                    if children[j][0] in self.forbidden:
                        del children[j]
                        continue
                    else:
                        child_node=node(value=children[j][0], parent=parent_node)
                        children[j][2]=child_node
                        parent_node.add_child(child_node)
                        fringe.insert(0,children[j])
                        j+=1
            
            # print('expanded')
            # for i in expanded:
            #     print(i[0])
            # print('children')
            # for i in children:
            #     print(i[0])
            # print('fringe')
            # for i in fringe:
            #     print(i[0])
        
        else:
            return print('No solution found.')

        return print(path_str+'\n'+final_str)

    def DFS_IDS(self, depth_limit):
        # print("DFS Method")
        starting_node=node(value=self.start)
        Tree = tree(root=starting_node)
        fringe=[[self.start, None, starting_node]]
        expanded=[]

        while len(fringe)!=0:
            i=fringe[0]
            if i[0]==self.goal:
                expanded.append(i)
                try:
                    # presenting expanded nodes
                    beginning=0
                    for i in expanded:
                        if beginning==0:
                            final_str=i[0]
                            beginning+=1
                        else:
                            final_str=final_str+','+i[0]

                    # presenting path of nodes
                    pathway=Tree.root_pathway(child=expanded[-1][2])

                    beginning=0
                    for i in reversed(pathway):
                        if beginning==0:
                            path_str=i
                            beginning+=1
                        else:
                            path_str=path_str+','+i

                except:        
                    print('Nothing to process...')

                break
            if len(expanded)==1000:
                return print('Limit has been reached.')
            
            if depth_limit == 
            # print('------------------')
            # print('fringe', fringe)
            children, parent_node=self.expand_children(number=i[0], changed=i[1], root_path=i[2])
            children.reverse()
            expanded.append(fringe[0])
            del fringe[0]
            if self.forbidden==None:
                for k in children:
                    child_node=node(value=k[0], parent=parent_node)
                    k[2]=child_node
                    parent_node.add_child(child_node)
                    fringe.insert(0,k)
            else:
                j=0
                while len(children)!=j:
                    if children[j][0] in self.forbidden:
                        del children[j]
                        continue
                    else:
                        child_node=node(value=children[j][0], parent=parent_node)
                        children[j][2]=child_node
                        parent_node.add_child(child_node)
                        fringe.insert(0,children[j])
                        j+=1
            
            # print('expanded')
            # for i in expanded:
            #     print(i[0])
            # print('children')
            # for i in children:
            #     print(i[0])
            # print('fringe')
            # for i in fringe:
            #     print(i[0])
        
        else:
            result='No solution found.'

            return 

        return print(path_str+'\n'+final_str)
    
    def IDS(self):
        print("IDS Method")
        
        solution_not_found=True
        depth_count=0
        while solution_not_found:
            result = self.DFS_IDS(depth_limit=depth_count)
            if result != 

        return
    
    def Greedy(self):
        print("Greedy Method")

        return
    
    def A_Star(self):
        print("A_Star Method")

        return
    
    def HillClimb(self):
        print("HillClimb Method")

        return