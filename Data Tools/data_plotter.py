import matplotlib.pyplot as plt
import os


def plotandsave(filedir):
    datafile = open(filedir)
    lines = datafile.readlines()

    str = ''
    for line in lines:
        str += line
    groups = str.split("\n\n")
    x=[]
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    print(groups[:-1])
    for group in groups[:-1]:
        x.append((float)(group.split('/')[0].split(' ')[-1]))
        y1.append((float)(group.split('train Loss: ')[1].split(' ')[0]))
        y2.append((float)(group.split('val Loss: ')[1].split(' ')[0]))
        y3.append((float)(group.split('Acc: ')[1].split('\n')[0]))
        y4.append((float)(group.split('Acc: ')[-1]))

    fig = plt.figure(figsize=(12,6))
    ax1 = fig.add_subplot(111)
    ax1.plot(x, y1, 'b--', linewidth=1, label="Train loss")
    ax1.plot(x, y2, 'r--', linewidth=1, label="Val loss")
    ax1.legend(loc=2)
    plt.xlabel("Epochs")
    ax1.set_ylabel("Loss")
    ax2 = ax1.twinx()
    ax2.plot(x, y3, 'b', linewidth=1, label="Train acc")
    ax2.plot(x, y4, 'r', linewidth=1, label="Val acc")
    ax2.legend(loc=1)
    ax2.set_ylabel("Accuracy")
    filename = filedir.split('\\')[-1]
    ax1.set_title("Convergence graph of {}".format(filename))

    plt.savefig("{}Convergence graph of {}.jpg".format(filedir.split('resnet50')[0], filename))


if __name__ == '__main__':
    filedir = '..\\..\\logs'
    for file in os.listdir(filedir):
        plotandsave(os.path.join(filedir, file))

