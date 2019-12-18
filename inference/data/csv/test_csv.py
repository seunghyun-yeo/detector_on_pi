import os

data_length_list = ['0.1', '0.5', '1.0']


for data_length in data_length_list:

    dataDir = os.getcwd().split('csv')[0] + 'trimmed/test/' + data_length
    csvDir = os.getcwd() + '/test_' + data_length + '.csv'
    
    f = open(csvDir,'w')
    f.write("filename\n")

    for i in os.listdir(dataDir):
        try:
            name = i.split(".wav")[0]
            f.write(name + '\n')
        except:
            continue



