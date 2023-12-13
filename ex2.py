import pandas as pd
import matplotlib.pyplot as plt

X = 10
Y = 13

def main():

    data = pd.read_csv("data.csv")

    plt.subplot(3, 1, 1)
    for c in data.columns:
        plt.plot(data[c])
    
    plt.subplot(3, 1, 2)
    for c in data.columns:
        plt.plot( data[c][:X] )
    
    plt.subplot(3,1,3)
    for c in ["Durata", "Puls"]:
        plt.plot( data[c][(len(data[c]) - Y): ])

    plt.show()

    return

if __name__ == '__main__':
    main()