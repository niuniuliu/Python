# print "Hi"
# a = range(5)
# print a


# from datetime import datetime
# from datetime import date


# print datetime.now()

# print date.today()


# def shout(phrase):
#     if phrase == phrase.upper():
#         return "YOU'RE SHOUTING!"
#     else:
#         return "Can you speak up?"

# x = shout("I'M INTERESTED IN SHOUTING")
# print x

# def hotel_cost(nights):
#     return 140 * nights


# print hotel_cost(7)

'''
{
    'pocket': ['seashell', 'strange berry', 'lint'],
    'backpack': ['bedroll', 'bread loaf', 'xylophone'],
    'pouch': ['flint', 'gemstone', 'twine'],
    'burlap bag': ['apple', 'small ruby', 'three-toed sloth'],
    'gold': 550
}




lloyd = {
    "name" : "Lloyd",
    "homework" : [],
    "quizzes" : [],
    "tests" : []
    }

alice = {
    "name" : "Alice",
    "homework" : [],
    "quizzes" : [],
    "tests" : []
    }

tyler = {
    "name" : "Tyler",
    "homework" : [],
    "quizzes" : [],
    "tests" : []
    }





from random import randint

board = []
for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)


print "Let's play Battleship!"
for turn in range(4):
    # Print (turn + 1) here!
    print "Turn: " + str(turn + 1)
    # print_board(board)

    ship_row = random_row(board)
    ship_col = random_col(board)
    print '## ' + str(ship_row) + ", " + str(ship_col)

    # Everything from here on should go in your for loop!
    # Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    elif guess_row not in range(5) or guess_col not in range(5) :
        print "Oops, that's not even in the ocean."
    elif (board[guess_row][guess_col] == "X"):
        print "You guessed that one already."
    else:
        print "Your Input: " + str(guess_row) + " , " + str(guess_col)
        print "You missed my battleship!"
        board[guess_row][guess_col] = "X"
        print_board(board)

    if turn == 3:
        print "Game Over"


def reverse(text):
    txt = ''
    for i in range(len(text)):
        txt += text[len(text) - 1 - i]
    return txt

print reverse('abcd')



# import string


# a = "abcddee"
# b = 'd'

# c = a.replace('d', '')

# print c

a = "this hack is wack hack"
b = "hack"

aa = a.split()

res = []
for i in range(len(aa)):
    if aa[i] == b:
        aa[i] = "*" * len(b)


print " ".join(aa)

# z = ['a', 'b']
# d = " ".join(z)
# print z
# print d




lst = ['a', 'b', 'c', 'd', 'e', 'd']
for i in range(len(lst)):
    print i

print range(len(lst))[1:]






def remove_duplicates(lst):
    res = lst
    new = []
    for i in range(len(lst)):
        if lst[i] not in res:
            print
            new.append(lst[i])

    return new



remove_duplicates([1,1,2,2, 3])


# print '1232'
class Triangle(object):
    
    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3
        
    number_of_sides = 3
        
    def check_angles(self):
        if self.angle1 + self.angle2 + self.angle3 == 180:
            return True
        else:
            return False

my_triangle = Triangle(90, 30, 60)
print my_triangle.number_of_sides
print my_triangle.check_angles()



def Equilateral(Triangle):
    angle = 60
    def __init__(self):
        self.angle = self.angle1  = self.angle2 = self.angle3
        
        



print "This is a [%s], [%s]MPG." % ("abc", 'fdsfds')

'''

single = ()
singleton = (2 , )

# print len(single)
# print len(singleton)
# x = ({'Swaroop'   : 'swaroop@swaroopch.com'},
#         {'Larry'     : 'larry@wall.org'},
#         {'Matsumoto' : 'matz@ruby-lang.org'},
#         {'Spammer'   : 'spammer@hotmail.com'})

ab = {  'Swaroop'   : 'swaroop@swaroopch.com',
        'Larry'     : 'larry@wall.org',
        'Matsumoto' : 'matz@ruby-lang.org',
        'Spammer'   : 'spammer@hotmail.com'
    }
print ab[-1]

# print type(x)
# for items in x:
#     print items
#     print type(items)

# print 'There are {} items in ab'.format(len(ab))

# for name, address in ab.items():
#     print 'Contact {} at {}'.format(name, address)

# for key, value in ab.items():
#     print key, value