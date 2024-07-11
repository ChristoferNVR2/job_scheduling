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
    total_profit = sum([profits[jobs.index(job)] for job in job_sequence])

    return job_sequence, total_profit


def main():
    # These values could change for each different problem
    jobs_ = ['J1', 'J2', 'J3', 'J4']
    deadlines_ = [2, 1, 2, 1]
    profits_ = [100, 10, 15, 27]

    sequence, profit = job_scheduling(jobs_, deadlines_, profits_)
    print(f"Job sequence: {sequence}")
    print(f"Total profit: {profit}")


if __name__ == "__main__":
    main()
