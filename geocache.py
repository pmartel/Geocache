#Puzzle Input
puzIn = (
(4,7,23,25,34,50,57,60,63,65,70,88,91,95),
(3,16,18,26,37,42,46,52,66,69,85,103),
(22,30,33,56,62,73,90,96,107),
(12,19,27,38,41,49,53,59,67),
(5,21,32,55,61,99),
(8,40,77,78,81,101),
(29,43,45,74,98,102),
(6,75,84,86,106),
(11,24,35,58,64),
(14,44,48,83,97),
(10,17,36,51),
(1,28,68,80),
(2,9,15,82),
(20,31,39,54),
(13,87,94),
(71,89,92),
(72,76,100),
(93,108),
(104,),
(79,),
(47,),
(105,)
)

#Letter frequency order from
#https://gist.github.com/pozhidaevak/0dca594d6f0de367f232909fe21cdb2f
initLetterFrequency = [
'E', 'T', 'A', 'O', 'I', 'N', 'S', 'R',
'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y',
'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q',
'J', 'Z' ]

# Functions operating on puzzle
def FillLine(puz,line,letter) :
     for i in line :
        puz[i-1] = letter

def PrintPuzzle(cols) :
    low=0
    while low + cols <= len(puzzle) :
        s = ""
        for i in range(low,low+cols):
            s += puzzle[i]
        print( s)
        low += cols


# script
print( "puzzle Input" )
print( puzIn )
print( "lines ", len(puzIn))

#verify number of cells
cells =0
for line in puzIn :
    cells += len(line)
print( cells, " cells")
# initialize puzzle
puzzle = []
for i in range(0,cells) :
    puzzle.append( "*")
print( "puzzle is of length ", len(puzzle))
#print( '"',puzzle,'"')

#letters = initLetterFrequency
#letters = ["T", "E"]

letters = list(22*"*")
letters[0]='T'
letters[1]='E'
letters[10]='H'
letters[3]="A"
letters[13]="D"
#Set up substitution
for p in range(len(puzIn)) :
    if p >= len(letters):
        el = "*"
    else:
        el = letters[p]
    FillLine(puzzle, puzIn[p], el)
PrintPuzzle(12)

#while 1 :
#    pass
