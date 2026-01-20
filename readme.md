# 📌 Tìm Cân Bằng Nash bằng Python (NashPy)

---

## 🧠 Giới thiệu

Repository này minh họa cách sử dụng thư viện **NashPy** trong Python
để tìm **cân bằng Nash** cho một bài toán cạnh tranh giá cả
giữa hai doanh nghiệp trong lý thuyết trò chơi.

---

## 🎯 Mục tiêu

- Mô hình hóa trò chơi hai người dạng ma trận.
- Dùng `NashPy` để tìm các cân bằng Nash (hỗn hợp/tùy chọn).
- So sánh kết quả lập trình với phân tích lý thuyết.

## 🎮 Mô tả trò chơi

### Người chơi
- Doanh nghiệp A
- Doanh nghiệp B

### Chiến lược
- `H`: Giữ giá cao
- `L`: Giảm giá

### Ma trận payoff

| A \\ B| H       | L       |
|-------|---------|---------|
| H     | (6, 6)  | (1, 8)  |
| L     | (8, 1)  | (3, 3)  |

---

## ⚙️ Hướng dẫn chạy (từng bước)

1. Clone repository và chuyển vào thư mục:

```bash
git clone https://github.com/ptthao456/nash-equilibrium.git
cd nash-equilibrium
```

2. Tạo virtual environment:

```bash
python -m venv venv
```

3. Kích hoạt virtual environment:

Windows (PowerShell):

```powershell
venv\Scripts\Activate.ps1
# hoặc nếu dùng cmd:
venv\Scripts\activate
```

macOS / Linux:

```bash
source venv/bin/activate
```

Khi thành công, terminal sẽ hiển thị `(venv)`.

4. Cài đặt phụ thuộc:

```bash
pip install -r requirements.txt
```

File `requirements.txt` (gợi ý):

- numpy
- nashpy
- scipy

5. Chạy chương trình demo:

```bash
python main.py
```

---

## Ghi chú

- `main.py` chứa ví dụ mô tả ma trận payoff ở trên và in ra các cân bằng Nash tìm được.
- Nếu gặp lỗi khi cài `nashpy`, hãy kiểm tra phiên bản Python (>=3.8) và cài lại `scipy`.

---
