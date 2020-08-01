import numpy as np 
import logging

'''
Within the game of tic-tac-toe (TTT), the board is defined as follows:

0   1   2

3   4   5

6   7   8

'''

class Game:
    '''
    Initializes game.
    '''
    def __init__(self):
        self.current_player = 1
        self.game_state = GameState((np.array([0,0,0,0,0,0,0,0,0]), 1)) #current game state
        self.action_space = np.array([0,0,0,0,0,0,0,0,0]) #current actionable states
        self.pieces = {'1': 'X', '0': '-', '-1': '0'} # 1 represents one player, -1 represents the other and 0 represents neutral
        self.grid_shape = (3,3)
        self.input_shape = (2,3,3)
        self.name = 'tictactoe'
        self.state_size = len(self.game_state.binary)
        self.action_size = len(self.action_space)
    
    def reset(self):
        self.game_state = GameState(np.array([0,0,0,0,0,0,0,0,0]), 1)
        self.current_player = 1
        return self.game_state
    
    def step(self, action):
        next_state, value, done = self.game_state.takeAction(action)
        self.game_state = next_state
        self.current_player = -self.current_player
        info = None
        return ((next_state, value, done, info))

class GameState:
    '''
    Provides update to the state of the game.
    e.g. If player chose '4', there should be
    an updated state in which square 4 is occupied.
    '''
    def __init__(self, board, player_turn):
        self.board = board
        self.pieces = {'1': 'X', '0': '-', '-1': '0'}
        self.winners = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,4,8],
            [2,4,6],
            [0,3,6],
            [1,4,7],
            [2,5,8]
        ]
        self.player_turn = player_turn
        self.binary = self._binary()
        self.id = self._convertStateToId()
        self.allowed_actions = self._allowedActions()
        self.is_end_game = self._checkForEndGame()
        self.value = self._getValue()
        self.score = self._getScore()
        
    def _allowedActions(self):


		return allowed
    
    def takeAction(self, action):
        new_board = np.array(self.board)
        new_board[action] = self.player_turn
        new_state = GameState(new_board, -self.player_turn)
        
        value = 0
        done = 0
        
        if new_state.is_end_game:
            value = new_state.value[0]
            done = 1
            
        return (new_state, value, done)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            


