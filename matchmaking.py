# dim(student_score) == dim(employer_scores^T)

score_matrix1 = [[1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1]]

score_matrix2 =[[1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]]

current_highest_score = 0
highest_scores_in_matches = []
matches1 = []
matches2 = []

accessable_from_matrix1 = []
accessable_from_martix2 = []
score_discrepacy = []
score_matrix = []

if len(score_matrix1)!= len(score_matrix2[0]) or len(score_matrix2) != len(score_matrix1[0]):
    print("The dimensions of the Studentscore matrix most be equal to the dimensions of the transpose matrix of the employerscore matrix")
    quit()

for i in range(1, len(score_matrix1)):
    if len(score_matrix1[0]) != len(score_matrix1[i]):
        print("There is an inquality of the length of the rows within the student_score-matrix")
        quit()

for i in range(1, len(score_matrix2)):
    if len(score_matrix2[0]) != len(score_matrix2[i]):
        print("There is an inquality of the length of the rows within the employer_score-matrix")
        quit()


for i in range(len(score_matrix1)):
    score_matrix.append([])
    for j in range(len(score_matrix2)):
        score_matrix[i].append(score_matrix1[i][j] + score_matrix2[j][i])

current_highest_score = 0
final_matches = []
lowest_match_scores = []

if len(score_matrix2) <= len(score_matrix1):
    coords_of_equals = []

    for i in range(len(score_matrix1)):
        accessable_from_matrix1.append(i)

    for i in range(len(score_matrix2)):
        matches1.append([0, 0])
        score_discrepacy.append(0)
        for j in accessable_from_matrix1:

            if score_matrix[j][i] > current_highest_score:
                current_highest_score = score_matrix[j][i]

                matches1[i][1] = i + 1
                matches1[i][0] = j + 1

            elif score_matrix[j][i] == current_highest_score:
                current_score_discrepancy = abs(score_matrix1[j][i] - score_matrix2[i][j])
                if score_discrepacy[i] < current_score_discrepancy:
                    current_highest_score = score_matrix[j][i]
                    score_discrepacy[i] = abs(score_matrix1[j][i] - score_matrix2[i][j])

                    matches1[i][1] = i + 1
                    matches1[i][0] = j + 1
                    coords_of_equals.append(matches1[i])

        accessable_from_matrix1.remove(matches1[i][0] - 1)
        current_highest_score = 0

    for i in range(len(score_matrix2)):
        final_matches.append(0)

    for j in range(len(score_matrix2)):
        for i in range(len(matches1)):
            if matches1[i][1] == j + 1:
                if score_matrix[matches1[i][1] - 1][matches1[i][1] - 1] > current_highest_score:
                    current_highest_score = score_matrix[matches1[i][0] - 1][matches1[i][1] - 1]
                    final_matches[j] = i
        current_highest_score = 0

    for final_match in final_matches:
        print(f'The best match for employer: {matches1[final_match][1]}, is student: {matches1[final_match][0]}')

else:
    coords_of_equals = []
    for i in range(len(score_matrix2)):
        accessable_from_martix2.append(i)

    for i in range(len(score_matrix1)):
        matches2.append([0, 0])
        score_discrepacy.append(0)
        for j in accessable_from_martix2:
            if score_matrix[i][j] > current_highest_score:
                current_highest_score = score_matrix[i][j]
                print(i)
                matches2[i][0] = i + 1
                matches2[i][1] = j + 1

            elif score_matrix[i][j] == current_highest_score:
                current_score_discrepancy = abs(score_matrix1[i][j] - score_matrix2[j][i])
                if score_discrepacy[i] < current_score_discrepancy:
                    current_highest_score = score_matrix[i][j]
                    score_discrepacy[i] = abs(score_matrix1[i][j] - score_matrix2[j][i])

                    matches2[i][0] = i + 1
                    matches2[i][1] = j + 1
                    coords_of_equals.append(matches2[i])

        accessable_from_martix2.remove(matches2[i][1] - 1)
        current_highest_score = 0

    for match in matches2:
        print(f'The best match for student: {match[0]}, is employer: {match[1]}')


