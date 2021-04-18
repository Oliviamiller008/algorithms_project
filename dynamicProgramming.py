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