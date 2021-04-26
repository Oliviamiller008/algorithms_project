from dataset.data import load_data
from exercises import exercises
import random
import datetime as dt
import time
import matplotlib.pyplot as plt

#Recursive Version
def dp(workoutlist, workoutTime):
    if workoutlist == [] or workoutTime == 0:
        result = (0, ())
    elif workoutlist[0].gettime() > workoutTime:
        # Right Branch
        result = dp(workoutlist[1:], workoutTime)
    else:
        nextExercise = workoutlist[0]
        #Left branch
        caloriesBurnt, chosenExecrices = dp(workoutlist[1:],
                                     workoutTime - nextExercise.gettime())
        caloriesBurnt += nextExercise.getcal()
        #Right branch
        caloriesLeft, otherExercises = dp(workoutlist[1:], workoutTime)
        # Choose better branch
        if caloriesBurnt > caloriesLeft:
            result = (caloriesBurnt, chosenExecrices + (nextExercise,))
        else:
            result = (caloriesLeft, otherExercises)
    return result

def dpBottomUp(workoutList , workoutTime):
    K = [[0 for x in range(workoutTime + 1)] for x in range(len(workoutList) + 1)]

    # Build table K[][] in bottom up manner
    for i in range(1,len(workoutList) + 1):
        for w in range(1,workoutTime+1):
            if workoutList[i-1].gettime() <= w:
                K[i][w] = max(workoutList[i-1].getcal() + K[i-1][w-workoutList[i-1].gettime()],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]


    #Save the optimal solutions
    maxCalorieBurnt = K[len(workoutList)][workoutTime]
    calories_burned = maxCalorieBurnt
    w = workoutTime
    i = len(workoutList)
    optimalExecrciselist = []
    while calories_burned >= 0 and w>0:
       if abs(calories_burned - K[i - 1][w]) >= 1:
            calories_burned -= workoutList[i-1].getcal()
            optimalExecrciselist.append(workoutList[i-1])
            w = w - workoutList[i-1].gettime()
       i -= 1

    # for i in range(len(workoutList), 0 ,-1):
    #     if calories_burned <=0:
    #         break
    #     if abs(calories_burned - K[i-1][w]) <= 1:
    #         continue
    #     else:
    #         #print(time_for_exercise[i-1])
    #         calories_burned = calories_burned - workoutList[i-1].getcal()
    #
    #         #add the exercise to the excercises done array
    #         exlist.append(workoutList[i - 1])
    #         w = w - workoutList[i-1].gettime()

    return maxCalorieBurnt, optimalExecrciselist

def buildexercises(exerciselist, inlist, weight):
    # returns the list of exercises that were not in previous day list
    return [exercises(key, values[1] * values[0] * weight, values[0])
            for key, values in exerciselist.items() if key not in inlist]


def runScheduler(inputs):
    workoutlist = load_data() #loads all the exercises
    workoutplan = {}
    inlist = []
    weight = inputs[0]
    for i in range(1, 8):
        workoutTime = inputs[i]
        exconsidered = buildexercises(workoutlist, inlist, weight)
        #totalCalBurnt, chosenExercises = dp(exconsidered, workoutTime)
        # exC = buildexercises(workoutlist, elist, weight)
        totalCalBurnt, chosenExercises = dpBottomUp(exconsidered,workoutTime)

        day = 'Day ' + str(i)
        workoutplan[day] = [['Total Calories Burnt: ' + "{:.2f}".format(totalCalBurnt),
                             'Total Workout Time: ' + str(workoutTime)]]

        #print("Day" + str(i))
        # print(f"Workout time: {workoutTime}")
        # print(f"Total Calorie Burnt: {totalCalBurnt:.2f}")
        inlist = []

        for ex in chosenExercises:
            inlist.append(ex.getname())
            # print(f"Name: {ex.getname()}, Calories: {ex.getcal():.2f}, Time: {ex.gettime()}")
            workoutplan[day].append([ex.getname(),' Calories: '+"{:.2f}".format(ex.getcal()),' Time: '+str(ex.gettime())])
        workoutplan[day].append([])

    return workoutplan

# workoutTime = 60
# wList = [(exercises(str(i),random.randint(100,250),random.randint(1,5)*5)) for i in range(250)]
# timeDp = []
# timeBf = []
# for i in range(5,60):
#     start = time.process_time()#dt.datetime.now()
#     dpBottomUp(wList[:i],workoutTime)
#     end = time.process_time()#dt.datetime.now()
#     timeDp.append(end-start)
#     print(timeDp)
#
# for i in range(5,60):
#     print(i)
#     start = time.process_time()#dt.datetime.now()
#     dp(wList[:i],workoutTime)
#     end = time.process_time()#dt.datetime.now()
#     timeBf.append(end-start)
#
# plt.plot(range(5,60),timeDp)
# plt.plot(range(5,60),timeBf)
# plt.xlabel('Num of Exercises')
# plt.xlabel('Execution time(Seconds)')
# plt.show()
# plt.savefig('runtime.png')