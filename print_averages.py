import numpy as np

def print_averages(group_of_trajectories_to_average, title):
    # Go through all trajectories and find shortest
    min_len = 10000000
    for col in group_of_trajectories_to_average:
        col_len = col.size
        if col_len < min_len:
            min_len = col_len
    # Go through trajectories and get averages up to the shortest time for all
    total_mean_group = [group_of_trajectories_to_average[0][0:min_len].mean()]
    for i in range(1, len(group_of_trajectories_to_average)):
        total_mean_group.extend([group_of_trajectories_to_average[i][0:min_len].mean()])
    # Print average up to the shortest time step
    total_ns = min_len / 5
    print(title + " (" + str(total_ns) + " ns):       " + str("{:.3f}".format(np.mean(total_mean_group))))


def print_individual_averages(group_of_trajectories_to_average, titles):
    # Go through trajectories and get averages for each
    for i in range(0, len(group_of_trajectories_to_average)):
        trajectory_length = group_of_trajectories_to_average[i].size
        print(titles[i] + " " + str("{:.3f}".format(group_of_trajectories_to_average[i].mean())) +
              " " + str(trajectory_length / 10) + " ns")


def print_individual_averages_totime(group_of_trajectories_to_average, titles, time):
    # Go through trajectories and get averages for each
    for i in range(0, len(group_of_trajectories_to_average)):
        trajectory_length = time
        print(titles[i] + " " + str("{:.3f}".format(group_of_trajectories_to_average[i][0:trajectory_length].mean())) +
              " " + str(trajectory_length / 10) + " ns")
