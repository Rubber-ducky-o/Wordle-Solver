import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d





def plotting(twoD_list : list[list]):
    # X - Word | Y - Layer | Z = IG SCORE
    x_values = []
    y_values = []
    z_values = []
    labels = []
    all_words = sorted({word for layer in twoD_list for word, _ in layer})
    word_index = {word : index for index, word in enumerate(all_words)}

    for y_num, layer in enumerate(twoD_list):
        for word, IG in layer:
            x_values.append(word_index[word])
            y_values.append(y_num+1)
            z_values.append(round(IG,2))
            labels.append(word)

    fig = plt.figure()
    ax = fig.add_subplot(111,projection = "3d")

    ax.scatter(x_values,y_values,z_values)
    for x,y,z, word in zip(x_values,y_values,z_values,labels):
        ax.text(x,y,z,word,fontsize = 7)
    ax.set_xlabel("WORD VALUE")
    ax.set_ylabel("LAYER / GUESS #")
    ax.set_zlabel("INFORMATION GAIN")

    plt.show()
