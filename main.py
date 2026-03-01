import numpy as np
import nashpy as nash


def analyze_stag_hunt_single_matrix():
    """
    STAG HUNT
    Biểu diễn bằng 1 ma trận payoff chung (a,b)
    Sau đó tách thành 2 ma trận cho NashPy
    """

    # ==============================
    # BƯỚC 1: Tập chiến lược
    # ==============================
    strategies = ["Stag", "Hare"]

    # ==============================
    # BƯỚC 2: Ma trận payoff chung
    # ==============================
    payoff_matrix = [
        [(3, 3), (0, 2)],
        [(2, 0), (1, 1)]
    ]

    # ==============================
    # BƯỚC 3: Tách thành 2 ma trận số
    # ==============================
    payoff_player1 = np.array([[cell[0] for cell in row] for row in payoff_matrix])
    payoff_player2 = np.array([[cell[1] for cell in row] for row in payoff_matrix])

    # ==============================
    # BƯỚC 4: Khởi tạo game
    # ==============================
    stag_hunt_game = nash.Game(payoff_player1, payoff_player2)

    print("=== PAYOFF MATRIX (a,b) ===")
    for row in payoff_matrix:
        print(row)

    print("\n=== NASH EQUILIBRIA ===")

    equilibria = list(stag_hunt_game.support_enumeration())

    for sigma_p1, sigma_p2 in equilibria:
        print("Player 1:", sigma_p1)
        print("Player 2:", sigma_p2)
        print("-" * 30)


if __name__ == "__main__":
    analyze_stag_hunt_single_matrix()
