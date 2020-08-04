import matplotlib.pyplot as plt
import csv

x = []
y = []
y1 = []

# with open('plotting_outputs/updated_varying_PID.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))
#     print(row[1])

fig, ax = plt.subplots(2)

with open('data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 0
    print(plots)
    for row in plots:
        count += 1
        x.append(count)
        y.append(int(row[0]))
        y1.append(int(row[1]))


ax[0].plot(x, y, label='Loaded from file!')
ax[1].plot(x, y1, label='second subplot')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
