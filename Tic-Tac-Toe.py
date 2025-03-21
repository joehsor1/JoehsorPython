tiles = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
wins = 

def victory(board);
  	for i in range(0, 3, 9):
    	if board[i] == board[i + 1] == board[i + 2] and board[i] != " ":
      		return board[i]
      
	for i in range(3):
		if board[i] == board[i + 3] == board[i + 6] and board[i] != " ":
      		return board[i]}
if board[0] == board[4] == board[8] or board[2] == board[4] == board[6] and board[4] != " ":
	return board[4]
