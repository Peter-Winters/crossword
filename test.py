# assignment = {
#     1: ["word1", "wordx"],
#     2: ["word2"],
#     3: ["word3"],
#     4: ["word4"],
#     5: ["word5"],
#     6: ["word6"],
# }
assignment = {}

assign = True
if assignment == {}:
    assign = False
for key in assignment.keys():
    print(assignment[key])
    print(len(assignment[key]))
    if len(assignment[key]) > 1:
        assign = False
        break
print(assign)
