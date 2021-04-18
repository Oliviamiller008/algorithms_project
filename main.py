from dataset.data import load_data
import random
from exercises import exercises
from dynamicProgramming import dp


def buildexercises(exerciselist, inlist, weight):
    # returns the list of exercises that were not in previous day list
    return [exercises(key, values[1] * values[0] * weight, values[0])
            for key, values in exerciselist.items() if key not in inlist]


def runScheduler():
    workoutlist = load_data()
    workoutplan = {}
    inlist = []
    weight = random.randint(150, 200)
    for i in range(1, 8):
        workoutTime = random.randint(9,24)*5 #choose randomly between 45,120 minutes
        exconsidered = buildexercises(workoutlist, inlist, weight)
        totalCalBurnt, chosenExercises = dp(exconsidered, workoutTime)
        workoutplan['day' + str(i)] = chosenExercises
        print("Day" + str(i))
        print(f"Workout time: {workoutTime}")
        print(f"Total Calorie Burnt: {totalCalBurnt:.2f}")
        inlist = []
        for ex in chosenExercises:
            inlist.append(ex.getname())
            print(f"Name: {ex.getname()}, Calories: {ex.getcal():.2f}, Time: {ex.gettime()}")


def main():
    runScheduler()


if __name__ == '__main__':
    main()
