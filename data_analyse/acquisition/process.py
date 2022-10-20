from data_analyse.acquisition.setup import ACQ_LENGHT, ACQ_PATH


def acquisition(id):
    for i in range(ACQ_LENGHT):
        print(i, ACQ_PATH)
        # TODO Make multiple data save into csv

# TODO Make Prompt interface for future dataset