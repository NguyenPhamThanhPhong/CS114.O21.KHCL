import math

# Get input
a_x, a_y = map(float, input().split())
b_x, b_y = map(float, input().split())

# Compute vector v and normal vector n
v_x = a_x - b_x
v_y = a_y - b_y
n_x = v_y
n_y = -v_x

# Compute alpha
ab_len_sq = (a_x - b_x) ** 2 + (a_y - b_y) ** 2
alpha = math.sqrt(ab_len_sq / (n_x**2 + n_y**2))

# Compute coordinates of points
first_x = a_x + alpha * n_x
first_y = a_y + alpha * n_y
second_x = b_x + alpha * n_x
second_y = b_y + alpha * n_y
third_x = b_x - alpha * n_x
third_y = b_y - alpha * n_y
fourth_x = a_x - alpha * n_x
fourth_y = a_y - alpha * n_y

a_str = f"({a_x}, {a_y})"
b_str = f"({b_x}, {b_y})"
f_str = f"({first_x}, {first_y})"
s_str = f"({second_x}, {second_y})"
t_str = f"({third_x}, {third_y})"
fo_str = f"({fourth_x}, {fourth_y})"

if(a_x>b_x):
    # print("ax>bx")
    print(f"{a_str} {fo_str} {t_str} {b_str} ")
    print(f"{a_str} {f_str} {s_str} {b_str}")
elif(a_x<b_x):
    # print("ax<bx")
    print(f"{a_str} {f_str} {s_str} {b_str}")
    print(f"{a_str} {b_str} {t_str} {fo_str} ")
else:
    if(a_y>b_y):
        print(f"{a_str} {b_str} {t_str} {fo_str}")
        print(f"{a_str} {f_str} {s_str} {b_str}")
    else:
        print(f"{a_str} {b_str} {t_str} {fo_str}")
        print(f"{a_str} {f_str} {s_str} {b_str}")


def solve():
    inp = input().split()
    A = [int(inp[0]), int(inp[1])]
    inp = input().split()
    B = [int(inp[0]), int(inp[1])]
    C = [A[0] + A[1] - B[1], A[1] + B[0] - A[0]]
    D = [B[0] + A[1] - B[1], B[1] + B[0] - A[0]]
    print(
        "({}, {}) ({}, {}) ({}, {}) ({}, {})".format(
            A[0], A[1], C[0], C[1], D[0], D[1], B[0], B[1]
        )
    )

    C = [A[0] - A[1] + B[1], A[1] - B[0] + A[0]]
    D = [B[0] - A[1] + B[1], B[1] - B[0] + A[0]]
    print(
        "({}, {}) ({}, {}) ({}, {}) ({}, {})".format(
            A[0], A[1], B[0], B[1], D[0], D[1], C[0], C[1]
        )
    )


if __name__ == "__main__":
    solve()
