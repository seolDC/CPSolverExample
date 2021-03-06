from cp_solver import cp_solver
from linear_optimization import linear_optimization
from n_queens import n_queens, print_n_queens
from nurse_scheduler import nurse
from task_scheduler import task_scheduler


def play_n_queens():
    # n 은 가로 세로 길이
    n = input(" L X L 길이 설정 : ")
    solver = n_queens(int(n))
    print_n_queens(solver[0], solver[1], int(n))


def play_linear_optimization():
    # ax + by <= c
    constraint_list = [{"a": 1, "b": 2, "c": 14},
                       {"a": -3, "b": 1, "c": 0},
                       {"a": 1, "b": -1, "c": 2},
                       ]
    objective_data = {"a": 3, "b": 4}
    linear_optimization(constraint_list, objective_data)


if __name__ == "__main__":
    print("Example number : 1.nQueens, 2.linear optimization, 3.cp_solver, 4.nurse schedule, 5.task schedule")
    selected = input("select solver example : ")
    
    if selected is "1":
        play_n_queens()
    elif selected is "2":
        play_linear_optimization()
    elif selected is "3":
        cp_solver()
    elif selected is "4":
        nurse()
    elif selected is "5":
        task_scheduler()
