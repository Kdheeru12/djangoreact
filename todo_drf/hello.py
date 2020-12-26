class UserMainCode(object):
    @classmethod
    def moveApples(cls,input1,input2):
        a = list(input2)
        x = int(sum(a)/input1)
        c = []
        # print(a)
        # print(x)
        for i in a:
            if i >x:
                c.append(i-x)
        print(sum(c))
a = int(input())
b= 

UserMainCode.moveApples(5,{2849,1620,705,1,30})