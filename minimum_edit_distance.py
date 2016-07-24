# the column represents the original word
word_file = open('words2.txt')
word_list = word_file.read().split('\n')
def get_minimum_edit_distance(word_original, word_input):
    distance_matrix = [[x for x in range(len(word_original)+1)]]
#     def print_distance_matrix() :
#         for x in distance_matrix:
#             print x
    for x in range(len(word_input)):
        distance_matrix.append([x+1])
#     for x in distance_matrix:
#         print x
    for x in range(1, len(word_input)+1):
        current_row = distance_matrix[x];
        for y in range(1, len(word_original)+1):
            if(word_input[x-1] == word_original[y-1]):
                current_row.append(distance_matrix[x-1][y-1])
            else:
                current_row.append(min([distance_matrix[x-1][y-1], distance_matrix[x-1][y], current_row[y-1]] )+1)
#         print_distance_matrix()
#     print [' ']+list(word_original)
#     print_distance_matrix();
#     print [' '] + list(word_input)
    return distance_matrix[-1][-1]

threshold = 40
def get_ranked_list(word_input):
    ranked_list = []
    for word in word_list:
        distance = get_minimum_edit_distance(word, word_input)
        if distance/float(len(word_input)) <= threshold/100.0:
            ranked_list.append((word, distance))
    def getKey(x):
        return x[1]
    ranked_list.sort(key=getKey)
    if ranked_list[0][1]==0:
        print word_input,"is present in the dictionary"
    return ranked_list
word_input= raw_input()
print get_ranked_list(word_input)
