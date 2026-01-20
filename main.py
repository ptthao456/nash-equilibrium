import numpy as np
import nashpy as nash


def main():
    """
    Tìm cân bằng Nash cho bài toán cạnh tranh giá
    giữa hai doanh nghiệp A và B bằng thư viện NashPy
    """

    # Ma trận payoff của doanh nghiệp A
    A = np.array([
        [6, 1],
        [8, 3]
    ])

    # Ma trận payoff của doanh nghiệp B
    B = np.array([
        [6, 8],
        [1, 3]
    ])

    # Khởi tạo trò chơi
    game = nash.Game(A, B)

    # Tìm cân bằng Nash bằng support enumeration
    equilibria = list(game.support_enumeration())

    # In kết quả
    print("Các cân bằng Nash tìm được:\n")
    for eq in equilibria:
        print("Chiến lược doanh nghiệp A:", eq[0])
        print("Chiến lược doanh nghiệp B:", eq[1])
        print("-" * 40)


if __name__ == "__main__":
    main()
