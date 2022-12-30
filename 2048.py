import random


class Field:

    playing_field = [
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0]
            ]

    numbers = []

    generation_rarity = 50

    @staticmethod
    def rand_gen(numbers, generation_rarity):
        coordinates = []
        location = 0
        value = 0
        for y in range(len(Field.playing_field)):
            for x in range(len(Field.playing_field[y])):
                if Field.playing_field[y][x] == 0:
                    coordinates.append([y,x])

        if len(coordinates) > 0:
            value = random.randrange(len(coordinates))
            if random.randrange(1,100) < generation_rarity:

                Field.playing_field[coordinates[value][0]][coordinates[value][1]] = numbers[random.randrange(len(numbers)-1)]

            return True
        else:
            return False

    @staticmethod
    def row_logic(current_pos, last_pos, direction):
    #the current value doesnt equal 0 and the current position doesnt equal the last position
        if Field.playing_field[current_pos[0]][current_pos[1]] != 0 and current_pos != last_pos:

            if Field.playing_field[current_pos[0]][current_pos[1]] == Field.playing_field[last_pos[0]][last_pos[1]]:
            #if the current value equals the value at the last savable position

                Field.playing_field[last_pos[0]][last_pos[1]] += Field.playing_field[current_pos[0]][current_pos[1]]
                Field.playing_field[current_pos[0]][current_pos[1]] = 0
                # add to the last savable position, set current position to 0
                last_pos[0] += direction[0]
                last_pos[1] += direction[1]

                        # mutate the last savable position by the proper vector
            elif Field.playing_field[last_pos[0]][last_pos[1]] == 0:
                    #if the last savable value equals 0, set the current value to it then set the current value to 0
                    Field.playing_field[last_pos[0]][last_pos[1]] += Field.playing_field[current_pos[0]][current_pos[1]]
                    Field.playing_field[current_pos[0]][current_pos[1]] = 0
            else:
                #if none of the above work, mutate the last position by the direction, and set it there (unless the new position isn't the current position)
                last_pos[0] += direction[0]
                last_pos[1] += direction[1]
                if last_pos != current_pos:
                    Field.playing_field[last_pos[0]][last_pos[1]] += Field.playing_field[current_pos[0]][current_pos[1]]
                    Field.playing_field[current_pos[0]][current_pos[1]] = 0

    @staticmethod
    def move(y_vector,x_vector, boolean):

        directions = [0,0]
        saved_state = [0,0]
        if boolean:
            directions[1] = x_vector[2]

            for y in range(y_vector[0], y_vector[1], y_vector[2]):

                saved_state[0] = y
                saved_state[1] = x_vector[0]

                for x in range(x_vector[0], x_vector[1], x_vector[2]):
                
                    Field.row_logic([y, x], saved_state, directions)

        else:
            directions[0] = x_vector[2]
            for y in range(y_vector[0], y_vector[1], y_vector[2]):

                saved_state[1] = y
                saved_state[0] = x_vector[0]

                for x in range(x_vector[0], x_vector[1], x_vector[2]):

                    Field.row_logic([x,y], saved_state, directions)

positive = [0,4,1]
negative = [3,-1,-1]



#0/1 controls whether or not moving horz/ve
# rt
#neg/pos x controls neg/pos direction




while True:
    print("\n"*10
          )
    text = raw_input("next")
    n = [0,0,0,0]
    if text =="a":
        Field.move(positive, positive, 1)
    elif text == "d":
        Field.move(positive, negative, 1)
        Field.rand_gen([2,4], 100)

    elif text == "w":
        Field.move(positive, positive, 0)
        Field.rand_gen([2,4], 100)

    elif text == "s":
        Field.move(positive, negative, 0)
        Field.rand_gen([2,4], 100)


    for y in Field.playing_field:
        for x in range(0, len(y)):
            foo = len(str(y[x]))
            if foo > n[x] :
               n[x] = foo 


    for y in Field.playing_field:
        for x in range(0, len( y)):
            
            if y[x] != 0:    
                print(y[x]),

            else:
                print (" "),
                
            
                
            print(" ") * (n[x] - len(str(y[x])) ),

        print("")
