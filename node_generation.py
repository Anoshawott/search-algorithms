from node_assignment import node
from tree_generation import tree
from collections import defaultdict
import numpy as np

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

            temp_expanded=[]
            for a in expanded:
                temp_expanded.append([a[0],a[1]])

            if self.forbidden==None:
                a=0
                # print(temp_expanded)
                while a != len(children):
                    k = children[a]
                    if [k[0],k[1]] in temp_expanded:
                        # print([k[0],k[1]])
                        del children[a]
                    else:
                        # print('else')
                        child_node=node(value=k[0], parent=parent_node)
                        k[2]=child_node
                        parent_node.add_child(child_node)
                        fringe.append(k)
                        a+=1
            else:
                j=0
                while len(children)!=j:
                    if children[j][0] in self.forbidden or [children[j][0],children[j][1]] in temp_expanded:
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

            temp_expanded=[]
            for a in expanded:
                temp_expanded.append([a[0],a[1]])

            if self.forbidden==None:
                a=0
                # print(temp_expanded)
                while a != len(children):
                    k = children[a]
                    if [k[0],k[1]] in temp_expanded:
                        # print([k[0],k[1]])
                        del children[a]
                    else:
                        # print('else')
                        child_node=node(value=k[0], parent=parent_node)
                        k[2]=child_node
                        parent_node.add_child(child_node)
                        fringe.insert(0,k)
                        a+=1
            else:
                j=0
                while len(children)!=j:
                    if children[j][0] in self.forbidden or [children[j][0],children[j][1]] in temp_expanded:
                        del children[j]
                        continue
                    else:
                        child_node=node(value=children[j][0], parent=parent_node)
                        children[j][2]=child_node
                        parent_node.add_child(child_node)
                        fringe.insert(0,children[j])
                        j+=1

            # if self.forbidden==None:
            #     for k in children:
            #         child_node=node(value=k[0], parent=parent_node)
            #         k[2]=child_node
            #         parent_node.add_child(child_node)
            #         fringe.insert(0,k)
            # else:
            #     j=0
            #     while len(children)!=j:
            #         if children[j][0] in self.forbidden:
            #             del children[j]
            #             continue
            #         else:
            #             child_node=node(value=children[j][0], parent=parent_node)
            #             children[j][2]=child_node
            #             parent_node.add_child(child_node)
            #             fringe.insert(0,children[j])
            #             j+=1
            
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
            
            if depth_limit != Tree.depth(node=i[2]):
                # print('------------------')
                # print('fringe', fringe)
                children, parent_node=self.expand_children(number=i[0], changed=i[1], root_path=i[2])
                children.reverse()
                expanded.append(fringe[0])
                del fringe[0]

                temp_expanded=[]
                for a in expanded:
                    temp_expanded.append([a[0],a[1]])

                if self.forbidden==None:
                    a=0
                    # print(temp_expanded)
                    while a != len(children):
                        k = children[a]
                        if [k[0],k[1]] in temp_expanded:
                            # print([k[0],k[1]])
                            del children[a]
                        else:
                            # print('else')
                            child_node=node(value=k[0], parent=parent_node)
                            k[2]=child_node
                            parent_node.add_child(child_node)
                            fringe.insert(0,k)
                            a+=1
                else:
                    j=0
                    while len(children)!=j:
                        if children[j][0] in self.forbidden or [children[j][0],children[j][1]] in temp_expanded:
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
                expanded.append(i)
                del fringe[0]

        else:
            result='No solution found.'
            final_str=''

            try:
                # presenting expanded nodes
                beginning=0
                for i in expanded:
                    if beginning==0:
                        final_str=i[0]
                        beginning+=1
                    else:
                        final_str=final_str+','+i[0]

                result='No solution found.'
                return result, final_str

            except:        
                return result, final_str

            return result, final_str

        return path_str, final_str
    
    def IDS(self):
        print("IDS Method")
        final_expand=''
        solution_not_found=True
        depth_count=0
        ##### EDGE CASE PROBLEM WHERE "No solution found." string may loop infinitely 
        ##### over trees when all nodes have been expanded as much as possible
        while solution_not_found:
            # print(depth_count)
            result, expanded = self.DFS_IDS(depth_limit=depth_count)
            # print(expanded)
            if result == 'No solution found.':
                if depth_count==0:
                    final_expand=expanded
                else:
                    final_expand=final_expand+','+expanded
                depth_count+=1
            else:
                solution_not_found=False
        final_expand=final_expand+','+expanded
        return print(result+'\n'+final_expand)
    



    

    def calc_greedy_distance(self, value):
        split_value=[int(char) for char in value]
        split_goal=[int(char) for char in self.goal]

        i=0
        distance=0
        while i != len(split_value):
            distance=distance+abs(split_value[i]-split_goal[i])
            i+=1

        return distance

    def dist_ordered_fringe(self, children, fringe):  
        # print("children",children)
        # print("fringe",fringe)

        added_fringe=fringe+children
        # print(children, fringe, added_fringe)      
        new_temp_fringe = defaultdict(list)
        new_final_fringe=[]
        for i in added_fringe:
            val=i[0]
            dist=self.calc_greedy_distance(value=val)
            new_temp_fringe[dist].append(i)

        # print(new_temp_fringe)

        # print(new_temp_fringe)
        for i in new_temp_fringe:
            rev=[]
            for j in new_temp_fringe[i]:
                rev.insert(0,j)
            new_temp_fringe[i]=rev

        # print('after',sorted(new_temp_fringe))
                
        for i in sorted(new_temp_fringe):
            # print((i, new_temp_fringe[i]), end =" ")
            for j in new_temp_fringe[i]:
                new_final_fringe.append(j)

        # print('++++++++++++++++')
        # print(new_final_fringe)

        return new_final_fringe

    def Greedy(self):
        # print("Greedy Method")
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
            expanded.append(fringe[0])
            del fringe[0]

            temp_expanded=[]
            for a in expanded:
                temp_expanded.append([a[0],a[1]])

            if self.forbidden==None:
                a=0
                # print(temp_expanded)
                while a != len(children):
                    k = children[a]
                    if [k[0],k[1]] in temp_expanded:
                        # print([k[0],k[1]])
                        del children[a]
                    else:
                        # print('else')
                        child_node=node(value=k[0], parent=parent_node)
                        k[2]=child_node
                        parent_node.add_child(child_node)
                        # fringe.insert(0,k)
                        a+=1
            else:
                j=0
                while len(children)!=j:
                    if children[j][0] in self.forbidden or [children[j][0],children[j][1]] in temp_expanded:
                        del children[j]
                        continue
                    else:
                        child_node=node(value=children[j][0], parent=parent_node)
                        children[j][2]=child_node
                        parent_node.add_child(child_node)
                        # fringe.insert(0,children[j])
                        j+=1
            
            fringe=self.dist_ordered_fringe(children=children, fringe=fringe)
            

        return print(path_str+'\n'+final_str)
    



    def calc_astar_distance(self, node, read_tree):
        split_value=[int(char) for char in node[0]]
        split_goal=[int(char) for char in self.goal]
        
        pathway_nodes=read_tree.root_pathway(child=node[2])

        # del pathway_nodes[0]

        processed_pathway=[]

        for i in pathway_nodes:
            split_vals=[int(char) for char in i]
            processed_pathway.append(split_vals)

        # print('++++++++++++++++')

        i=0
        goal_distance=0
        while i != len(split_value):
            goal_distance=goal_distance+abs(split_value[i]-split_goal[i])
            i+=1
        
        temp_distance=0
        # print(processed_pathway)

        i=0
        j=1
        while i != len(processed_pathway):
            while j != len(processed_pathway):
                first_array=np.array(processed_pathway[i])
                second_array=np.array(processed_pathway[j])
                diffs=first_array-second_array
                diffs_abs=np.absolute(diffs)
                total=np.sum(diffs_abs)
                temp_distance+=total
                j+=1
                break
            i+=1

        # for i in processed_pathway:
        #     j=0
        #     while j!=len(split_value):
        #         temp_distance=temp_distance+abs(split_value[j]-i[j])
        #         j+=1
        
        total_distance=goal_distance+temp_distance

        return total_distance


    def astar_dist_ordered_fringe(self, children, fringe, current_tree):
        added_fringe=fringe+children
        new_temp_fringe=defaultdict(list)
        new_final_fringe=[]
        for i in added_fringe:
            dist=self.calc_astar_distance(node=i, read_tree=current_tree)
            new_temp_fringe[dist].append(i)

        for i in new_temp_fringe:
            rev=[]
            for j in new_temp_fringe[i]:
                rev.insert(0,j)
            new_temp_fringe[i]=rev
                
        for i in sorted(new_temp_fringe):
            for j in new_temp_fringe[i]:
                new_final_fringe.append(j)

        # print(new_final_fringe)

        return new_final_fringe

    def A_Star(self):
        print("A_Star Method")
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
            expanded.append(fringe[0])
            del fringe[0]

            temp_expanded=[]
            for a in expanded:
                temp_expanded.append([a[0],a[1]])

            if self.forbidden==None:
                a=0
                # print(temp_expanded)
                while a != len(children):
                    k = children[a]
                    if [k[0],k[1]] in temp_expanded:
                        # print([k[0],k[1]])
                        del children[a]
                    else:
                        # print('else')
                        child_node=node(value=k[0], parent=parent_node)
                        k[2]=child_node
                        parent_node.add_child(child_node)
                        # fringe.insert(0,k)
                        a+=1
            else:
                j=0
                while len(children)!=j:
                    if children[j][0] in self.forbidden or [children[j][0],children[j][1]] in temp_expanded:
                        del children[j]
                        continue
                    else:
                        child_node=node(value=children[j][0], parent=parent_node)
                        children[j][2]=child_node
                        parent_node.add_child(child_node)
                        # fringe.insert(0,children[j])
                        j+=1
            
            fringe=self.astar_dist_ordered_fringe(children=children, fringe=fringe, current_tree=Tree)

            # for i in fringe:
            #     print(i[0])

        return print(path_str+'\n'+final_str)
    
    def calc_greedy_distance(self, value):
        split_value=[int(char) for char in value]
        split_goal=[int(char) for char in self.goal]

        i=0
        distance=0
        while i != len(split_value):
            distance=distance+abs(split_value[i]-split_goal[i])
            i+=1

        return distance




    def dist_ordered_fringe(self, children, fringe):  
        # print("children",children)
        # print("fringe",fringe)

        added_fringe=fringe+children
        # print(children, fringe, added_fringe)      
        new_temp_fringe = defaultdict(list)
        new_final_fringe=[]
        for i in added_fringe:
            val=i[0]
            dist=self.calc_greedy_distance(value=val)
            new_temp_fringe[dist].append(i)

        # print(new_temp_fringe)

        # print(new_temp_fringe)
        for i in new_temp_fringe:
            rev=[]
            for j in new_temp_fringe[i]:
                rev.insert(0,j)
            new_temp_fringe[i]=rev

        # print('after',sorted(new_temp_fringe))
                
        for i in sorted(new_temp_fringe):
            # print((i, new_temp_fringe[i]), end =" ")
            for j in new_temp_fringe[i]:
                new_final_fringe.append(j)

        # print('++++++++++++++++')
        # print(new_final_fringe)

        return new_final_fringe
    
    def HillClimb(self):
        print("HillClimb Method")

        return