def simplifyPath(path):
    stack = []
    i = 0
    res = ''
    while i < len(path):
        print path[i]
        end = i+1
        while end < len(path) and path[end] != "/":
            end += 1
        sub=path[i+1:end]
        # print sub
        if len(sub) > 0:
            if sub == "..":
                if stack != []: 
                    stack.pop()
            elif sub != ".":
                stack.append(sub)
            print "stack: ", stack
        i = end
    if stack == []: return "/"
    for i in stack:
        res += "/"+i
    return res

simplifyPath("/../a/b/c/./..")