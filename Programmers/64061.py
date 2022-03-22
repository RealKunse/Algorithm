import pprint

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

pprint.pprint(board)


def solution(board, moves):
    picked = []
    answer = 0

    for j in range(len(moves)):
        for i in range(len(board)):
            if board[i][moves[j] - 1] != 0:
                picked.append(board[i][moves[j] - 1])
                board[i][moves[j] - 1] = 0
                break

        if len(picked) >= 2 and picked[-1] == picked[-2]:
            answer += 2
            picked = picked[:-2]

    print(answer)

solution(board, moves)
