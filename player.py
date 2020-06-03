from board import Direction, Rotation
from random import Random


class Player:
    def choose_action(self, board):
        raise NotImplementedError


class RandomPlayer(Player):
    def __init__(self, seed=None):
        self.random = Random(seed)


    def choose_action(self, board):

        return self.random.choice([
            [Direction.Left, Direction.Drop],
            [Direction.Right, Direction.Drop],
            [Direction.Down, Direction.Drop],
            [Rotation.Anticlockwise, Direction.Drop],
            [Rotation.Clockwise, Direction.Drop]
        ])



class playerA:

    def __init__(self, seed = None):
        self.random = Random(seed)

    #func that moves block to the target_position.
    def move_block(self, board, target_position):


        if target_position == 0:
            for i in range(0,5):
                if board.falling is not None:
                    board.move(Direction.Left)
            if board.falling is not None:
                board.move(Direction.Drop)
        elif target_position == 1:
            for i in range(0,4):
                if board.falling is not None:
                    board.move(Direction.Left)
            if board.falling is not None:
                board.move(Direction.Drop)
        elif target_position == 2:
            for i in range(0,3):
                if board.falling is not None:
                    board.move(Direction.Left)
            if board.falling is not None:
                board.move(Direction.Drop)
        elif target_position == 3:
            for i in range(0,2):
                if board.falling is not None:
                    board.move(Direction.Left)
            if board.falling is not None:
                board.move(Direction.Drop)
        elif target_position == 4:
            for i in range(0,1):
                if board.falling is not None:
                    board.move(Direction.Left)
            if board.falling is not None:
                board.move(Direction.Drop)
        elif target_position == 5:
            if board.falling is not None:
                board.move(Direction.Drop)
        elif target_position == 6:
            for i in range(0,1):
                if board.falling is not None:
                    board.move(Direction.Right)
            if board.falling is not None:
                board.move(Direction.Drop)
        elif target_position == 7:
            for i in range(0,2):
                if board.falling is not None:
                    board.move(Direction.Right)
            if board.falling is not None:
                board.move(Direction.Drop)
        elif target_position == 8:
            for i in range(0,3):
                if board.falling is not None:
                    board.move(Direction.Right)
            if board.falling is not None:
                board.move(Direction.Drop)
        elif target_position == 9:
            for i in range(0,4):
                if board.falling is not None:
                    board.move(Direction.Right)
            if board.falling is not None:
                board.move(Direction.Drop)

#
    def rotate_block(self, board, target_rotation):

        if target_rotation == 0: #it works
            board.skip()
        elif target_rotation == 1: #it works
            if board.falling is not None:
                board.rotate(Rotation.Clockwise)
        elif target_rotation == 2:
            if board.falling is not None:
                board.rotate(Rotation.Clockwise)
                board.rotate(Rotation.Clockwise)
        elif target_rotation == 3:
            if board.falling is not None:
                board.rotate(Rotation.Anticlockwise)




    def find_which_rotation(self, list1):
        max_num = max(list1)

        for i in range(0, 4):
            if list1[i] == max_num:
                return i # index tells the which rotation has that lowest num


    def find_which_position(self,board, which_rotation, list1):
        min_num = max(list1)
        clony = board.clone()
        self.rotate_block(clony, which_rotation)
        list = self.try_every_position(clony)

        list2 = []
        for i in range(0,10):
            if list[i] == min_num:
                list2.append(i)

        return list2



    def get_sum_heights(self, board):
        list =[]
        for x in range(0, 10):
            for y in range(0, board.height):
                # when reach to the bottom of the page and nothing, then print 0
                if (y == board.height - 1) and ((x,y) not in board.cells):
                    list.append(0)
                elif (x, y) in board.cells:
                    list.append((board.height) - y)
                    break
        return self.add_heights(list)

    def add_heights(self, list):
        #we take in one list
        #caluculate the sum of that list.
        sum = list[0] + list[1] + list[2] + list[3] + list[4] + \
              list[5] + list[6] + list[7] + list[8] + list[9]
        int(sum)
        return sum

        # func that identifies the num of holes.
    def hole_count(self, board):
        # go from top to bottom and left to right.
        hole_count = 0
        for y in range(0, board.height):
            for x in range(0, board.width):
                if (x, y) not in board.cells and (x, y - 1) in board.cells:
                    hole_count += 1
        return hole_count

    #bumpiness
    #get the height of position x and minus the height of the postion x-1
    #get the sum of the of the difference
    def bumpiness(self,board):
        list = []
        for x in range(0, 10):
            for y in range(0, board.height):
                # when reach to the bottom of the page and nothing, then print 0
                if (y == board.height - 1) and ((x,y) not in board.cells):
                    list.append(0)
                elif (x, y) in board.cells:
                    list.append((board.height) - y)
                    break
        bumpiness = self.difference_in_height(list)
        return bumpiness  #if this value is high, the score should be low

    def difference_in_height(self,list):

        bumpiness = 0
        for i in range(0,9):
            bumpiness += abs(list[i] - list[i + 1])
        return bumpiness

    #completed lines
    #if you run through the whole row and all of them in cell
    #then return true to show that line has completed.
    def completed_lines(self,board):

        completed_lines = 0

        for y in range(0,board.height):
            count = 0
            for x in range(0,board.width):
                if (x,y) in board.cells:
                    count += 1
            if count == 10:
                completed_lines += 1

        print(completed_lines)
        return completed_lines







    def score(self, height_sum, hole_count, bumpiness, completed_lines):
        weight1 = -0.7
        weight2 = -0.12
        weight3 = -0.22
        weight4 = 1.5 #the higher the completed lines the higher the score
        score = weight1*height_sum + weight2*hole_count +weight3*bumpiness + weight4*completed_lines
        return score


    def try_every_position(self, board):

        list = []
        for i in range(0, 10):
            clony = board.clone()
            self.move_block(clony, i)  # makes movements in clony
            hole_count = self.hole_count(clony)
            height_sum = self.get_sum_heights(clony)
            bumpiness = self.bumpiness(clony)
            completed_lines = self.completed_lines(clony)


            list.append(self.score(height_sum, hole_count, bumpiness, completed_lines))

        return list #a list of score of each position

    # at the end of the day, choose the positon and rotation of the highest score.
    def try_every_move(self, board):
        rotation = 0
        list1 = []

        # there are four rotations, 0, 1, 2, 3
        for i in range(0, 4):
            # do the rotation
            clony = board.clone()
            self.rotate_block(clony, rotation)
            # place the block in every position
            list = self.try_every_position(clony)  # return score  of all positions
            list1.append(max(list))
            rotation += 1

        return list1  # a list of the max score in each rotation.

    # figure out which rotation and which movement




    def choose_action(self, board):  # (document) once the actions run out, it will call choose_action again.

        list1= self.try_every_move(board)
        which_rotation = self.find_which_rotation(list1) #rotation of the max position

        list2 = self.find_which_position(board, which_rotation, list1)
        which_position = self.random.choice(list2) #position of the maximum position.

        return self.rot(which_rotation) + self.pos(which_position)



    def pos(self, target_position):

        list = []
        if  target_position == 0:
            for i in range(0,5):
                list.append(Direction.Left)
            list.append(Direction.Drop)
        elif target_position == 1:
            for i in range(0,4):
                list.append(Direction.Left)
            list.append(Direction.Drop)
        elif target_position == 2:
            for i in range(0,3):
                list.append(Direction.Left)
            list.append(Direction.Drop)
        elif target_position == 3:
            for i in range(0,2):
                list.append(Direction.Left)
            list.append(Direction.Drop)
        elif target_position == 4:
            for i in range(0,1):
                list.append(Direction.Left)
            list.append(Direction.Drop)
        elif target_position == 5:
            list.append(Direction.Drop)
        elif target_position == 6:
            for i in range(0,1):
                list.append(Direction.Right)
            list.append(Direction.Drop)
        elif target_position == 7:
            for i in range(0,2):
                list.append(Direction.Right)
            list.append(Direction.Drop)
        elif target_position == 8:
            for i in range(0,3):
                list.append(Direction.Right)
            list.append(Direction.Drop)
        elif target_position == 9:
            for i in range(0,4):
                list.append(Direction.Right)
            list.append(Direction.Drop)

        return list

    def rot(self,target_rotation):

        list = []
        if target_rotation == 0:  # it works
            pass
        elif target_rotation == 1:  # it works
            list.append(Rotation.Clockwise)
        elif target_rotation == 2:
            list.append(Rotation.Clockwise)
            list.append(Rotation.Clockwise)
        elif target_rotation == 3:
            list.append(Rotation.Anticlockwise)
        return list



SelectedPlayer = RandomPlayer

