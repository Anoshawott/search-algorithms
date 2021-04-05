class action_space:
    def __init__(self, start, goal, forbidden=None):
        self.start=start
        self.goal=goal
        self.forbidden=forbidden
    
    def generate(self):
        print(self.start)
        print(self.goal)
        print(self.forbidden)

    def expand_children(self, number, changed=None):
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
            temp_digits.append(check)
            new_digits.append(temp_digits)
            k+=1

        if changed==None:    
            i=0
            while i != len(number):
                if i==0:
                    if new_digits[i][-1]==2:
                        new_number1=new_digits[i][1]+number[1]+number[2]
                        new_number2=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0])
                        children.append([new_number2,0])
                    elif new_digits[i][-1]==1:
                        new_number1=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0])
                elif i==1:
                    if new_digits[i][-1]==2:
                        new_number1=number[0]+new_digits[i][1]+number[2]
                        new_number2=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1])
                        children.append([new_number2,1])
                    elif new_digits[i][-1]==1:
                        new_number1=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1])
                elif i==2:
                    if new_digits[i][-1]==2:
                        new_number1=number[0]+number[1]+new_digits[i][1]
                        new_number2=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2])
                        children.append([new_number2,2])
                    elif new_digits[i][-1]==1:
                        new_number1=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2])
                i+=1
        
        elif changed==0:
            i=0
            while i != len(number):
                if i==1:
                    if new_digits[i][-1]==2:
                        new_number1=number[0]+new_digits[i][1]+number[2]
                        new_number2=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1])
                        children.append([new_number2,1])
                    elif new_digits[i][-1]==1:
                        new_number1=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1])
                elif i==2:
                    if new_digits[i][-1]==2:
                        new_number1=number[0]+number[1]+new_digits[i][1]
                        new_number2=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2])
                        children.append([new_number2,2])
                    elif new_digits[i][-1]==1:
                        new_number1=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2])
                i+=1

        elif changed==1:
            i=0
            while i != len(number):
                if i==0:
                    if new_digits[i][-1]==2:
                        new_number1=new_digits[i][1]+number[1]+number[2]
                        new_number2=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0])
                        children.append([new_number2,0])
                    elif new_digits[i][-1]==1:
                        new_number1=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0])
                elif i==2:
                    if new_digits[i][-1]==2:
                        new_number1=number[0]+number[1]+new_digits[i][1]
                        new_number2=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2])
                        children.append([new_number2,2])
                    elif new_digits[i][-1]==1:
                        new_number1=number[0]+number[1]+new_digits[i][0]
                        children.append([new_number1,2])
                i+=1

        elif changed==2:
            i=0
            while i != len(number):
                if i==0:
                    if new_digits[i][-1]==2:
                        new_number1=new_digits[i][1]+number[1]+number[2]
                        new_number2=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0])
                        children.append([new_number2,0])
                    elif new_digits[i][-1]==1:
                        new_number1=new_digits[i][0]+number[1]+number[2]
                        children.append([new_number1,0])
                elif i==1:
                    if new_digits[i][-1]==2:
                        new_number1=number[0]+new_digits[i][1]+number[2]
                        new_number2=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1])
                        children.append([new_number2,1])
                    elif new_digits[i][-1]==1:
                        new_number1=number[0]+new_digits[i][0]+number[2]
                        children.append([new_number1,1])
                i+=1

        print('Number', number)
        print('New digits', new_digits)
        print('Children', children)
        return children




    def BFS(self):
        print("BFS Method")
        fringe=[[self.start, None]]
        expanded=[]

        while len(fringe)!=0:
            i=fringe[0]
            if i[0]==self.goal:
                expanded.append([str(self.goal), 0])
                break
            if len(expanded)==1000:
                return print('Limit has been reached.')
            print('------------------')
            # print('fringe', fringe)
            children=self.expand_children(number=i[0], changed=i[1])
            if self.forbidden==None:
                for k in children:
                    fringe.append(k)
            else:
                j=0
                while len(children)!=j:
                    if children[j][0] in self.forbidden:
                        del children[j]
                        continue
                    else:
                        fringe.append(children[j])
                        j+=1
            expanded.append(fringe[0])
            del fringe[0]            
        
        try:
            beginning=0
            for i in expanded:
                print(i)
                if beginning==0:
                    final_str=i[0]
                    beginning+=1
                else:
                    final_str=final_str+','+i[0]
        except:
            print('Nothing to process...')

        return print(final_str)






    def DFS(self):
        print("DFS Method")

        return
    
    def IDS(self):
        print("IDS Method")

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