#=========== Design a Tic Tac Toe Game ==============#

'''
# Define Requirements / Scope
- Size of Board (standard: 3x3, extend: NxN)
- Define State of the Board (game is being played or not)
- Will game be Timed (yes / no)
- Will there be any observers (yes / no)
- Number of Players (standard: 2, extend N)
- Types of Symbol (standard: O/X, extend: any)
- How is Winner Declared (standard: [horizontal, vertical, diagonal], custom)
- Can players perform Undo Operation?

#==================== Create Classes and Define Methods ===================#
class Game()
- gameID
- gameState(bool)
- play()
- Board()
- Players(n, [players]) 
- Observers()
- Rules()
- sendMsg()
- whosTurn(deque)
- moveHistory([])
- getResult()

class Board()
- size n
- grid [n][n]
- displayBoard()
- isCellEmpty()
- markCell()
- getCellInfo()
- resetBoard()

class Player()
- details(name, id)
- currentStatus(playing / idle)
- setSymbol(X / O / custom)
- getScore() / getStats()

class Symbol()
- getSymbol(enum)

class Rules()                   classStandard(Rules)
- isValidMove()                 - isValidMove()
- checkWinner()                 - checkWinner()
- checkForDraw()                - checkForDraw()    


class Oberserver()
- details(name, id)
- gameID

class Notifier()
- sendMsg()
'''

