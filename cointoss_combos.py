"""This program creates a list of all possible outcomes/
when tossing a coin for n times."""

# there are two possible outcomes when tossing a coin: heads and tails
coin = ['H', 'T']

"""The following two lines are for user interface"""
# print('Enter the number of times the coin is tossed: ')
# times = int(input())

"""For me it is faster to change one value here:"""
times = 3


def augment(outcomes):
    """This function takes a list of possible outcomes of n tosses/
    and creates a list of possible outcomes for n+1 tosses, /
    thus augmenting the toss count by 1"""
    new_list = []
    for outcome in outcomes:
        for side in coin:
            new_list.append(outcome + side)
    return new_list


def tosses(times, list):
    """This function repeats augmenting for the user-entered number of times"""
    for i in range(times-1):
        list = augment(list)
    return list


print(*tosses(times, coin), sep='\n')


