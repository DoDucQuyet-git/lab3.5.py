import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import re
from datetime import datetime

# =========================
# AI LOGIC
# =========================
def detect_type(content):
    if "chia hết" in content:
        return "chia_het"
    if "phương trình bậc 2" in content:
        return "pt_bac2"
    return "unknown"


def generate_code(ex_id, content):
    t = detect_type(content)

    if t == "chia_het":
        return f"""# Bai {ex_id}
n = int(input("Nhap so: "))

if n % 2 == 0 and n % 3 == 0:
    print("Chia het cho ca 2 va 3")
elif n % 2 == 0:
    print("Chia het cho 2")
elif n % 3 == 0:
    print("Chia het cho 3")
else:
    print("Khong chia het")
"""

    if t == "pt_bac2":
        return f"""# Bai {ex_id}
import math

a = float(input("Nhap a: "))
b = float(input("Nhap b: "))
c = float(input("Nhap c: "))

if a == 0:
    if b != 0:
        print("x =", -c/b)
    else:
        print("Vo nghiem")
else:
    delta = b*b - 4*a*c

    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        print("x =", -b/(2*a))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
"""

    return f"# Bai {ex_id}\nprint('Chua ho tro')"


# =========================
# PARSE BÀI
# =========================
def parse_exercises(text):
    pattern = r"Bài\s*(\d+):(.+?)(?=Bài\s*\d+:|$)"
    return re.findall(pattern, text, re.S)


# =========================
# TẠO FILE + PUSH
# =========================
def run_ai():
    text = input_box.get("1.0", tk.END)

    exercises = parse_exercises(text)

    if not exercises:
        messagebox.showerror("Lỗi", "Không tìm thấy bài")
        return

    if not os.path.exists("output"):
        os.makedirs("output")

    result = ""

    for ex_id, content in exercises:
        filename = f"output/Bai{ex_id}.py"

        code = generate_code(ex_id, content.lower())

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)

        result += f"✔ Tạo {filename}\n"

    # push github
    os.system("git add .")
    os.system(f'git commit -m "auto {datetime.now()}"')
    os.system("git push")

    output_box.delete("1.0", tk.END)
    output_box.insert(tk.END, result)


# =========================
# GUI
# =========================
root = tk.Tk()
root.title("AI Sinh Code + GitHub")
root.geometry("750x500")

tk.Label(root, text="Nhập đề bài:", font=("Arial", 12)).pack()

input_box = scrolledtext.ScrolledText(root, height=8)
input_box.pack(fill="both", padx=10, pady=5)

tk.Button(root, text="🚀 Tạo code & Push GitHub", 
          command=run_ai, bg="purple", fg="white").pack(pady=10)

tk.Label(root, text="Kết quả:", font=("Arial", 12)).pack()

output_box = scrolledtext.ScrolledText(root, height=10)
output_box.pack(fill="both", padx=10, pady=5)

root.mainloop()
