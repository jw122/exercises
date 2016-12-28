import collections
result_groups = collections.defaultdict(lambda:[])

MEMBERS_BY_GROUPS = {
'Group0': {
'NestedGroups': ['Group3'],
'Members': ['User0', 'User1']
},
'Group1': {
'NestedGroups': ['Group3'],
'Members': ['User2', 'User3', 'User4']
},
'Group2': {
'NestedGroups': ['Group3', 'Group5'],
'Members': ['User4', 'User5']
},
'Group3': {
'NestedGroups': ['Group4'],
'Members': ['User6', 'User7']
},
'Group4': {
'NestedGroups': [],
'Members': ['User8', 'User9']
},
'Group5': {
'NestedGroups': [],
'Members': ['User10', 'User11']
}
}

def get_ancestors(group, ancestors):
    for k in MEMBERS_BY_GROUPS.keys():
        if group in MEMBERS_BY_GROUPS[k]['NestedGroups']:
            ancestors.append(k)
            get_ancestors(k, ancestors)
    return ancestors

def ancestry_dict(inputDict):
    resultDict = collections.defaultdict(lambda:[])
    for item in inputDict:
        nested = inputDict[item]['NestedGroups']
        for nestedGroup in nested:
            resultDict[nestedGroup] = get_ancestors(nestedGroup, [])
    return resultDict

def group_by_users(members_by_groups):
    ancestryDict = ancestry_dict(members_by_groups)

    for item in members_by_groups:
        users = members_by_groups[item]['Members']
        for usr in users:
            result_groups[usr].append(item)
            result_groups[usr] += ancestryDict[item]
    
    return result_groups

print group_by_users(MEMBERS_BY_GROUPS)



##### SOLUTION
# GROUPS_BY_USERS = {'User6': ['Group1', 'Group0', 'Group3', 'Group2'],
#                   'User7': ['Group1', 'Group0', 'Group3', 'Group2'],
#                   'User4': ['Group1', 'Group2'],
#                   'User5': ['Group2'],
#                   'User2': ['Group1'],
#                   'User3': ['Group1'],
#                   'User0': ['Group0'],
#                   'User1': ['Group0'],
#                   'User8': ['Group4', 'Group1', 'Group0', 'Group3', 'Group2'],
#                   'User9': ['Group4', 'Group1', 'Group0', 'Group3', 'Group2'],
#                   'User10': ['Group5', 'Group2'],
#                   'User11': ['Group5', 'Group2']}