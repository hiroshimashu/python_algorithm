## Write a function that accepts fight string consists of only small letters 
# and * which means a bomb drop place. 
# Return who wins the fight after bombs are exploded. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

# Left side
# m - 4
# q - 3 
# d - 2
# z - 1




# Right side
# w - 4
# p - 3 
# b - 2
# s - 1


def alphabet_war(fight):
    LEFT_SIDE = {"m": 4,"q": 3, "d": 2, "z": 1}
    RIGHT_SIDE = {"w": 4,"p": 3, "b": 2, "s": 1}
    POINT_LEFT = 0
    POINT_RIGHT = 0
    # Search letters in fight
    # If letter in left_side, then increase POINT_LEFT and the same in case with right_side
    for letter in fight: 
        for key in LEFT_SIDE:
            if key == letter:
                POINT_LEFT += LEFT_SIDE[key]
        for key in RIGHT_SIDE:
            if key == letter:
                POINT_RIGHT += RIGHT_SIDE[key]
    if POINT_LEFT > POINT_RIGHT: 
        return "Left side wins!"
    elif POINT_LEFT < POINT_RIGHT:
        return "Right side wins!"
    else:
        return "Let's fight again!"

result1 = alphabet_war("s*zz")
print(result1)

