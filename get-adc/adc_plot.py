import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_xlabel("Время, с", fontsize=14)
    ax.set_ylabel("Напряжение, В", fontsize=14)
    ax.grid(which="major", linewidth=1)
    ax.grid(which="minor", linestyle="-", color="gray", linewidth=0.4)
    plt.plot(time, voltage)
    plt.ylim(0,max_voltage)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_period=[]
    for i in range(len(time)-1):
        sampling_period.append(abs(time[i]-time[i+1]))
    fig, ax = plt.subplots(figsize=(10,6))
    ax.set_xlabel("Период измерения, с", fontsize=14)
    ax.set_ylabel("Количество измерений, В", fontsize=14)
    ax.grid(which="major", linewidth=1)
    ax.grid(which="minor", linestyle="-", color="gray", linewidth=0.4)
    plt.hist(sampling_period)
    #plt.xlim(0,0.06)
    plt.show()