import numpy as np
Q = {}
# Learning parameters
alpha = 0.1  # Learning rate
gamma = 0.9  # Discount factor
epsilon = 0.2  # Exploration rate

def get_state(board):
    return tuple(board.flatten())

def choose_action(state, available_actions):
    if np.random.uniform(0, 1) < epsilon:
        # Explore: Random action
        return np.random.choice(available_actions)
    else:
        # Exploit: Choose the best action from Q-table
        q_values = [Q.get((state, action), 0) for action in available_actions]
        return available_actions[np.argmax(q_values)]

def update_q_value(state, action, reward, next_state, available_actions):
    current_q = Q.get((state, action), 0)
    next_q = max([Q.get((next_state, a), 0) for a in available_actions], default=0)
    Q[(state, action)] = current_q + alpha * (reward + gamma * next_q - current_q)

def is_winner(board, player):
    for line in [board[i, :] for i in range(3)] + [board[:, i] for i in range(3)] + \
                [np.diag(board), np.diag(np.fliplr(board))]:
        if all(x == player for x in line):
            return True
    return False

def train_tic_tac_toe(episodes=10000):
    for _ in range(episodes):
        board = np.zeros((3, 3), dtype=int)  # Reset the board
        state = get_state(board)
        player = 1  # Start with player 1
        
        while True:
            available_actions = [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]
            if not available_actions:
                # Draw
                break
            
            action = choose_action(state, available_actions)
            board[action] = player
            
            # Check for game-ending conditions
            if is_winner(board, player):
                update_q_value(state, action, 1, None, [])
                break
            elif not any(0 in row for row in board):
                update_q_value(state, action, 0.5, None, [])
                break

            next_state = get_state(board)
            update_q_value(state, action, 0, next_state, available_actions)
            
            state = next_state
            player *= -1  # Switch players

# Train the bot
train_tic_tac_toe()

# Q-table is now trained and can be used for decision-making
print("Training complete!")
