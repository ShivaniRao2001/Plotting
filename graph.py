import matplotlib.pyplot as plt
import time
import numpy as np

start_time = time.time()
x = np.linspace(1,10)
y = np.sin(x)
plt.plot(x,y,"-r",label="y=sin(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of Sine Curve")
plt.legend()
plt.show()
end_time = time.time()



print("Time taken: " + str(end_time-start_time)+" seconds")