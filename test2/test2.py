import numpy as np



print("---------Hello-----------")
a = np.linspace(start = -5, stop = 150,
                num = 128, endpoint = True)

print("Graphical Representation : \n", np.cbrt(a))
print(type(np.cbrt(a)))
print("---------Thank you------------")

# plt.title("blue : with cbrt\nred : without cbrt")
# plt.plot(a, np.cbrt(a))
#
# plt.scatter(a, a, color = 'red')
# plt.show()
