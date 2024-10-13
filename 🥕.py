import os, sys, random, json

args = sys.argv[1:]

if len(args) == 0:
    print('\x1b[31m🥕 Write your file name as an Argument\x1b[39m')
    exit(1)
if not os.path.exists(args[0]) and args[0] != '-':
    print('\x1b[31m🥕 This file doesn\'t exist !\x1b[39m')
    exit(1)
if not os.path.isfile(args[0]) and args[0] != '-':
    print('\x1b[31m🥕 This is not a file !\x1b[39m')
    exit(1)


FN = args[0]

if not FN.endswith(".🥕"):
    print("\x1b[31m🥕 This is not a Carrot file !\x1b[39m")
    exit(1)

FC = ""
with open(FN, "r") as f:
    FC = f.read()

FC = FC.replace("ðŸ¥•", "🥕")

#FC = FC.replace("ðŸ—¿", "🗿")


AL = []
for a in FC.split("\n"):
    AL.append([])
    for i in a.split():
        AL[-1].append(len(i))

    if len(AL[-1]) == 0:
        AL.pop()


stack = []
exe = []
variables = {}
whil = 0
dex = 0
will = [0]


while dex != len(AL):


    a = AL[dex]

    if a[0] == 1:
        stack.append(0)
        for i in a[1:]:
            if i == 1:
                stack[-1] = stack[-1]*(-1)
            elif i == 2:
                stack[-1] = stack[-1]+1
            elif i == 3:
                stack[-1] = stack[-1]+2
            elif i == 4:
                stack[-1] = stack[-1]+3
            elif i == 5:
                stack[-1] = stack[-1]+5
            elif i == 6:
                stack[-1] = stack[-1]*2
            elif i == 7:
                stack[-1] = stack[-1]*3
            elif i == 8:
                stack[-1] = stack[-1]*5
            else:
                print("🥕WHY ?")
                break
    elif a[0] == 2:
        for i in a[1:]:
            NB = stack.pop()
            NA = stack.pop()
            if i == 1:
                stack.append(NA+NB)
            elif i == 2:
                stack.append(NA-NB)
            elif i == 3:
                stack.append(NA*NB)
            elif i == 4:
                stack.append(NA/NB)
            elif i == 5:
                stack.append(random.randint(NA, NB))
    elif a[0] == 3:
        for i in a[1:]:
            if i == 1:
                stack[-1] = chr(stack[-1])
            elif i == 2:
                print(stack)
            elif i == 3:
                stack.pop()
            elif i == 4:
                print(AL)
            elif i == 5:
                final = stack[-2]+stack[-1]
                stack.pop()
                stack.pop()
                stack.append(final)
            elif i == 6:
                final = ""
                for b in stack:
                    final += str(b)
                stack = final
            elif i == 7:
                print(stack[-1])
            elif i == 8:
                final = ""
                for b in stack[-1]:
                    final += str(b)
                stack[-1] = final
    elif a[0] == 4:
        if a[1] == 1:
            if a[2] == 1:
                stack.append(input())
            elif a[2] == 2:
                stack.append(int(input()))
        elif a[1] == 2:
            NA = stack[-2]
            NB = stack[-1]
            stack.pop()
            stack.pop()
            stack.append(str(NA)+str(NB))
            
    elif a[0] == 5:
        for i in a[1:]:
            if i == 1:
                stack.append(0)
                stack[-1] = stack[-1]+64
            elif i == 2:
                stack.append(0)
                stack[-1] = stack[-1]+96
            elif i == 3:
                stack.append(0)
                stack[-1] = stack[-1]+47
            elif i == 4:
                if str(stack[-1]) in variables:
                    variables |= {str(stack[-1]): str(stack[-2])}
                    stack.pop()
                    stack.pop()
                else:
                    variables.update({str(stack[-1]): str(stack[-2])})
                    stack.pop()
                    stack.pop()
            elif i == 5:
                if len(stack) < 1:
                    print("\x1b[31m🥕 You need more information !\x1b[39m")
                    exit(1)
                elif str(stack[-1]) in variables:
                    NA = stack[-1]
                    stack.pop()

                    stack.append(variables[str(NA)])
                else:
                    print("\x1b[31m🥕 Variable not existent !\x1b[39m")
                    exit(1)
            elif i == 6:
                stack.append(variables)
            elif i == 7:
                if len(stack) < 1:
                    print("\x1b[31m🥕 You need more information !\x1b[39m")
                    exit(1)
                elif not os.path.exists(str(stack[-1])) and str(stack[-1]) != '-':
                    print('\x1b[31m🥕 This file doesn\'t exist !\x1b[39m')
                    exit(1)
                elif not os.path.isfile(str(stack[-1])) and str(stack[-1]) != '-':
                    print('\x1b[31m🥕 This is not a file !\x1b[39m')
                    exit(1)
                else:
                    fn = str(stack[-1])
                    fc = {}
                    stack.pop()

                    with open(fn, "r") as f:
                        fc = json.load(f)
                    variables.update(fc)
            elif i == 8:
                stack.append(".var")
            elif i == 9:
                stack[-1] = int(stack[-1])


    elif a[0] == 6:
        if a[1] == 1:
            NB = stack.pop()
            NA = stack.pop()
            NC = stack.pop()
            if a[2] == 1:
                if a[3] == 1:
                    ND = stack.pop()
                    
                    if NA == NB:
                        stack.append(NC)
                    else:
                        stack.append(ND)
                elif a[3] == 2:
                    if NA == NB:
                        stack.append(NC)
                    else:
                        stack.append(False)
                else:
                    if NA == NB:
                        stack.append(NC)
        elif a[1] == 2:
            stack.append(f"WHILE")
            will[0] = 0
            whil = dex 

        elif a[1] == 3:
            index = 0
            p = 0
            for i in stack:
                if str(i) == ("WHILE"):
                    p = index
                index += 1

            index = p


            if will[0] != 1:
                dex = whil

        elif a[1] == 4:
            NB = stack.pop()
            NA = stack.pop()
            if NA == NB:
                will[0] = 1


    elif a[0] > 10:
        pass

    dex += 1

