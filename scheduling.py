import matplotlib.pyplot as plt


def job_scheduling(jobs, deadlines, profits):
    job_list = list(zip(jobs, deadlines, profits))

    job_list.sort(key=lambda x: x[2], reverse=True)

    n = len(jobs)
    result = [None] * n
    slot = [False] * n

    for job in job_list:
        for i in range(min(n, job[1]) - 1, -1, -1):
            if slot[i] is False:
                slot[i] = True
                result[i] = job[0]
                break

    job_sequence = [job for job in result if job is not None]

    job_profit_map = {job[0]: job[2] for job in job_list}
    profit_sequence = [job_profit_map[job] for job in job_sequence]

    total_profit = sum(profit_sequence)

    return job_sequence, profit_sequence, total_profit


def plot_jobs_vs_profits(job_sequence, profit_sequence):
    plt.figure(figsize=(10, 6))
    plt.bar(job_sequence, profit_sequence, color='skyblue')
    plt.xlabel('Jobs')
    plt.ylabel('Profits')
    plt.title('Job Profits')
    plt.show()


def main():
    # These values could change for each different problem
    jobs_ = ['J1', 'J2', 'J3', 'J4', 'J5', 'J6', 'J7']
    deadlines_ = [1, 3, 4, 3, 2, 1, 2]
    profits_ = [3, 5, 20, 18, 1, 6, 30]

    # Other example, please uncomment and comment the previous example to test
    # jobs_ = ['J1', 'J2', 'J3', 'J4']
    # deadlines_ = [2, 1, 2, 1]
    # profits_ = [100, 10, 15, 27]

    sequence, profit_sequence, profit = job_scheduling(jobs_, deadlines_, profits_)

    print(f"Job sequence: {sequence}")
    print(f"Profit sequence: {profit_sequence}")
    print(f"Total profit: {profit}")

    plot_jobs_vs_profits(sequence, profit_sequence)


if __name__ == "__main__":
    main()
