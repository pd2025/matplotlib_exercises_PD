import matplotlib.pyplot as plt
import csv

x = []
y = []

# with open('plotting_outputs/updated_varying_PID.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     for row in spamreader:
#         print(', '.join(row))
#     print(row[1])

with open('data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    count = 0
    print(plots)
    for row in plots:
        count += 1
        x.append(count)
        y.append(int(row[0]))

plt.plot(x, y, label='Loaded from file!')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()
