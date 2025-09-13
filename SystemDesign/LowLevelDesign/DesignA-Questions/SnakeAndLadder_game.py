#=========== Design a Snakes and Ladder Game ==============#

'''
# Define Requirements / Scope
- Size of Board (standard: 10X10, extend: NxN)
- Define State of the Board (game is being played or not)
- Will game be Timed (yes / no)
- Will there be any observers (yes / no)
- Number of Players (standard: 1, extend N)
- How is Winner Declared (standard: reaching nth cell, starting from 1st, custom)
- How many dice (standard: 1 [1-6], custom: n)

#==================== Create Classes and Define Methods ===================#
class Game()
- gameID
- gameState(bool)
- play()
- Board()
- Players(n, [players]) 
- Dice()
- Observers()
- Rules()
- sendMsg()
- whosTurn(deque)
- moveHistory([])
- getResult()

class Board()
- size n
- grid [n][n]
- boardEntity() [[entities]]
- displayBoard()
- isCellEmpty()
- markCell()
- getCellInfo()
- resetBoard()

class Player()
- details(name, id)
- currentStatus(playing / idle)
- getPos()
- getScore() / getStats()

class boardEntity()        class Snake(boardEntity)             class Ladder(boardEntity)
- startPos()               - display()                          - display()
- endPos()
- display()


class Rules()                   class Standard(Rules)
- isValidMove()                 - isValidMove()
- calcNewPost()                 - calcNewPost()    
- checkWinner()                 - checkWinner()




class Oberserver()
- details(name, id)
- gameID

class Notifier()
- sendMsg()
'''

