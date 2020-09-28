import pickle


def write_datafile_pkl(data, file_name):
    output = open('{}.pickle'.format(file_name), 'wb')
    pickle.dump(data, output)
    output.close()


def read_datafile_pkl(filename):
    output = open('{}.pickle'.format(filename), 'rb')
    data = pickle.load(output)
    output.close()
    return data
