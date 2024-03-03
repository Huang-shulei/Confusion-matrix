import numpy as np
import matplotlib.pyplot as plt


plt.figure(figsize=(10.4,9.0))
con_mat = np.array([[47,0,3,0,0],
                    [0,47,0,1,2],
                    [10,0,39,0,1],
                    [0,1,0,37,12],
                    [0,1,1,12,36]])
a = 0.0
for i in range(5):
    a += con_mat[i,i]
print(a/250)
classes = ["normal", "a", "b", "c", "d"]
plt.imshow(con_mat, cmap=plt.cm.Blues)
indices = range(len(con_mat))
plt.xticks(indices, classes, fontsize = "33")
plt.yticks(indices, classes, fontsize = "33", rotation=90, va='center')
plt.colorbar().ax.tick_params(labelsize='38')
plt.xlabel('Guess',size=40)
plt.ylabel('True',size=40)
for first_index in range(len(con_mat)):
    for second_index in range(len(con_mat[first_index])):
        if con_mat[second_index][first_index] <= 25:
            plt.text(first_index, second_index, con_mat[second_index][first_index], va='center', ha='center',
                     color="black", size=48)
        if con_mat[second_index][first_index] > 25:
            plt.text(first_index, second_index, con_mat[second_index][first_index], va='center', ha='center',
                     color="white", size=48)

plt.show()