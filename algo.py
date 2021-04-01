

def workout_plan(minutes, time_for_exercise, calories, num_exercises): 
    K = [[0 for x in range(minutes+ 1)] for x in range(num_exercises + 1)]


    # Build table K[][] in bottom up manner
    for i in range(num_exercises + 1):
        for w in range(minutes+ 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif time_for_exercise[i-1] <= w:
                K[i][w] = max(calories[i-1] + K[i-1][w-time_for_exercise[i-1]],  K[i-1][w])
                S[w] = i 
            else:
                K[i][w] = K[i-1][w]

# Print the optimal solution    
    res = K[num_exercises][minutes]     
    print(res)
    w = minutes  
    for i in range(num_exercises, 0 ,-1):
        if res <= 0:
            break
        if res == K[i-1][w]:
            continue
        else:
            print(time_for_exercise[i-1])
            res = res - calories[i-1]
        w = w - time_for_exercise[i-1]


def main():
    val = input("Enter the number of minutes you have to workout: ")
    minutes = int(val)
    time_for_exercise = [10, 20, 30]
    calories = [60, 100, 120]
    num_exercises = 3
    workout_plan(minutes, time_for_exercise, calories, num_exercises)

main()

