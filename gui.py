import tkinter as tk
from dynamicProgramming import runScheduler

fields = ['Weight(lbs)', 'Day 1(mins)', 'Day 2(mins)', 'Day 3(mins)', 'Day 4(mins)', \
         'Day 5(mins)','Day 6(mins)', 'Day 7(mins)']

def output(frame,workoutplan):
    newWindow = tk.Toplevel(frame)
    listbox = tk.Listbox(newWindow,height=45,width=70)
    for key in workoutplan:
        listbox.insert(tk.END,key)
        for j in workoutplan[key]:
            listbox.insert(tk.END, ' '.join(j))
    listbox.pack()


def fetch(entries,frame = None):
    inputs = []
    for entry in entries:
        text = entry[1].get()
        inputs.append(int(text))
    workoutplan = runScheduler(inputs)
    output(frame,workoutplan)



def makeform(root, fields):
    entries = []
    for field in fields:
        row = tk.Frame(root)
        lab = tk.Label(row, width=15, text=field, anchor='w')
        ent = tk.Entry(row)
        row.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)
        lab.pack(side=tk.LEFT)
        ent.pack(side=tk.RIGHT, expand=tk.YES, fill=tk.X)
        entries.append((field, ent))
    return entries

def gui():
    root = tk.Tk()
    tk.Label(root,text = 'Workout Scheduler').pack()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = tk.Button(root, text='Plan',
                  command=(lambda e=ents: fetch(e,root)))
    b1.pack(side=tk.LEFT, padx=5, pady=5)
    b2 = tk.Button(root, text='Quit', command=root.quit)
    b2.pack(side=tk.LEFT, padx=5, pady=5)
    root.mainloop()