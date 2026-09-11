import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits import mplot3d





def plotting(twoD_list : list[list]):
    # X - Word | Y - Layer | Z = IG SCORE


    all_words = sorted({word for layer in twoD_list for word, _ in layer})
    word_index = {word : index for index, word in enumerate(all_words)}

    fig = plt.figure()
    ax = fig.add_subplot(111,projection = "3d")

    for y_num, layer in enumerate(twoD_list,start =1):

        x_values = []
        y_values = []
        z_values = []

        for word, IG in layer:


            x_values.append(word_index[word])
            y_values.append(y_num)
            z_values.append(round(IG,2))

        ax.scatter(x_values,y_values,z_values,label = f"IG Iteration {y_num}: {len(layer)} words")

    ax.legend()


    num_layers = len(twoD_list)

    ax.set_xlabel("LEXOGRAPHICAL WORD INDEX")
    ax.set_ylabel("IG ITERATION")
    ax.set_zlabel("INFORMATION GAIN")

    ax.set_ylim(0.5,num_layers + 0.5)
    ax.set_yticks(range(1,num_layers + 1))

    ax.view_init(elev =25,azim = -60)

    ax.set_box_aspect((2,1,1))
    info = (f"IG Layers: {len(twoD_list)}\n"
            f"Final Candidates: {len(twoD_list[-1])}"
            )
    ax.text2D(0.02,0.95,info,transform = ax.transAxes,verticalalignment = "top")


    ax.set_title("Information Gain through Wordle Solver Iterations")
    for i, layer in enumerate(twoD_list,start = 1):
        print(f"IG LAYER{i}: {len(layer)} WORDS")

    plt.show()

def decision_graph(guess_history):
    _,ax = plt.subplots()
    x = 0
    spacing = 2

    for index, (word,score) in enumerate(guess_history):
        y = -(index * spacing)

        ax.text(x,y,word.upper(),ha = "center",va = "center",bbox = dict(boxstyle="circle",fill=False))

        ax.text(x + 0.4,y-1,score,ha = "left",va = "center")

        if index < len(guess_history) - 1:
            next_y = -((index + 1) * spacing)
            ax.plot([x,x],[y-0.3,next_y + 0.3])


    ax.set_title("Solver Guess path")
    ax.axis("off")
    plt.show()

def reduction_graph(pairwise,initial_count : int):
    _,ax = plt.subplots()

    iterations = [0]
    candidate_count = [initial_count]

    for iteration,layer in enumerate(pairwise,start=1):

        iterations.append(iteration)
        candidate_count.append(len(layer))

    ax.plot(
        iterations,
        candidate_count,
        marker ="o"
    )
    for x,y in zip(iterations,candidate_count):
        ax.text(x,y,str(y),ha= "center",va= "bottom")
    ax.set_xlabel("IG ITERATION")
    ax.set_ylabel("POSSIBLE WORDS")
    ax.set_title("Candidate Search")

    ax.set_xticks(iterations)

    plt.show()