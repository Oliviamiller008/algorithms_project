


def workout_plan(minutes, time_for_exercise, calories, num_exercises): 
    K = [[0 for x in range(minutes+ 1)] for x in range(num_exercises + 1)]

    # Build table K[][] in bottom up manner
    for i in range(num_exercises + 1):
        for w in range(minutes+ 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif time_for_exercise[i-1] <= w:
                K[i][w] = max(calories[i-1] + K[i-1][w-time_for_exercise[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]


    # Find and print the optimal solution    
    calories_burned = K[num_exercises][minutes]   
    exercises_done_day_1 = [] 
    print('Maximum calories: ' + str(calories_burned))
    print('Do these exercises: ')
    w = minutes  
    for i in range(num_exercises, 0 ,-1): 
        if calories_burned <= 0:
            break
        if calories_burned == K[i-1][w]:
            continue
        else:
            print(time_for_exercise[i-1])
            calories_burned = calories_burned - calories[i-1]

            #add the exercise to the excercises done array
            exercises_done_day_1.append(time_for_exercise[i-1])
        w = w - time_for_exercise[i-1]

    return exercises_done_day_1




def create_new_data(exercises_done_day_1, time_for_exercise, calories):

    new_exercises = time_for_exercise.copy()
    new_calories = calories.copy()

    #remove all exercises done the day before and record indicies removed
    indicies = []
    for j in range(len(exercises_done_day_1)):
        indicies.append(new_exercises.index(exercises_done_day_1[j]))
        new_exercises.remove(exercises_done_day_1[j])


    
    #remove the calories corresponding to the exercises deleted  
    for x in range(len(indicies)):
        new_calories.pop(indicies[x])

 
    return new_exercises, new_calories 



def main():
    time_for_exercise = [30, 20, 10]
    calories = [120, 100, 60]
    num_exercises = 3

    #create workout for first day 
    val = input("Enter the number of minutes you have to workout: ")
    minutes = int(val)
    exercises_done_day_1 = workout_plan(minutes, time_for_exercise, calories, num_exercises)

    # create constrained data 
    new_exercises, new_calories = create_new_data(exercises_done_day_1, time_for_exercise, calories)
  
    
    #create workout for second day 
    val2 = input("Enter number of minutes you have for second day: ")
    minutes = int(val2)
    workout_plan(minutes, new_exercises, new_calories, len(new_exercises))




main()

