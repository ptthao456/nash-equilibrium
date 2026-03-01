# 🎯 STAG HUNT -- Nash Equilibrium using NashPy

## 1️⃣ Mô hình trò chơi (Normal Form)

Trò chơi **Stag Hunt** là trò chơi đối xứng hai người chơi với thông tin
đầy đủ.

### Tập chiến lược

Mỗi người chơi có hai chiến lược:

-   **Stag** (Săn hươu)\
-   **Hare** (Săn thỏ)

S₁ = S₂ = {Stag, Hare}

------------------------------------------------------------------------

## 2️⃣ Biểu diễn ma trận lợi ích (Bimatrix)

Ma trận payoff chung:

                       Player 2: Stag   Player 2: Hare
  -------------------- ---------------- ----------------
  **Player 1: Stag**   (3,3)            (0,2)
  **Player 1: Hare**   (2,0)            (1,1)

Trong mỗi ô: 
- Số thứ nhất: payoff của Player 1\
- Số thứ hai: payoff của Player 2

------------------------------------------------------------------------

## 3️⃣ Cách triển khai trong Python

Thư viện **NashPy** yêu cầu truyền vào hai ma trận payoff riêng biệt:

Game(A, B)

Trong đó: 
- A: ma trận lợi ích của Player 1\
- B: ma trận lợi ích của Player 2

Chương trình thực hiện:

1.  Khai báo ma trận payoff chung (a,b)
2.  Tách thành hai ma trận số
3.  Khởi tạo đối tượng trò chơi
4.  Tìm cân bằng Nash bằng support_enumeration()

------------------------------------------------------------------------

## 4️⃣ Code

``` python
import numpy as np
import nashpy as nash


def analyze_stag_hunt_single_matrix():
    strategies = ["Stag", "Hare"]

    payoff_matrix = [
        [(3, 3), (0, 2)],
        [(2, 0), (1, 1)]
    ]

    payoff_player1 = np.array([[cell[0] for cell in row] for row in payoff_matrix])
    payoff_player2 = np.array([[cell[1] for cell in row] for row in payoff_matrix])

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
```

------------------------------------------------------------------------

## 5️⃣ Kết quả cân bằng Nash

Chương trình tìm được:

✔ Hai cân bằng Nash thuần túy: 
- (Stag, Stag)
- (Hare, Hare)

✔ Một cân bằng Nash hỗn hợp

------------------------------------------------------------------------

## 6️⃣ Cài đặt thư viện

``` bash
pip install numpy nashpy
```

------------------------------------------------------------------------

## 📌 Tóm tắt

-   Biểu diễn đúng mô hình trò chơi tĩnh
-   Tách payoff theo định nghĩa hàm lợi ích uᵢ(sᵢ, s₋ᵢ)
-   Áp dụng thuật toán support enumeration
-   Đối chiếu kết quả với lý thuyết trò chơi

