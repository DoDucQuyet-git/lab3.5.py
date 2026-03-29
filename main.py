import os
import re
from datetime import datetime

# =========================
# 1. ĐỌC ĐỀ TỪ FILE
# =========================
def read_input():
    with open("input.txt", "r", encoding="utf-8") as f:
        return f.read()


# =========================
# 2. TÁCH BÀI
# =========================
def parse_exercises(text):
    pattern = r"Bài\s*(\d+):(.+?)(?=Bài\s*\d+:|$)"
    matches = re.findall(pattern, text, re.S)

    return [{"id": num, "content": content.strip().lower()} for num, content in matches]


# =========================
# 3. SINH CODE
# =========================
def detect_type(content):
    keywords = {
        "chia_het": ["chia hết", "chia het"],
        "pt_bac2": ["phương trình bậc 2", "bậc 2", "ax^2"],
        "so_nguyen_to": ["nguyên tố", "prime"],
    }

    for key, words in keywords.items():
        for w in words:
            if w in content:
                return key

    return "unknown"


def generate_code(ex):
    content = ex["content"]
    ex_type = detect_type(content)

    # ===== TEMPLATE =====

    templates = {

        "chia_het": f"""# Bai {ex['id']}
n = int(input("Nhap so: "))

ket_qua = []

if n % 2 == 0:
    ket_qua.append("2")

if n % 3 == 0:
    ket_qua.append("3")

if ket_qua:
    print("Chia het cho:", ", ".join(ket_qua))
else:
    print("Khong chia het cho 2 hoac 3")
""",

        "pt_bac2": f"""# Bai {ex['id']}
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
        print("Nghiem kep:", -b/(2*a))
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("x1 =", x1)
        print("x2 =", x2)
""",

        "so_nguyen_to": f"""# Bai {ex['id']}
n = int(input("Nhap n: "))

if n < 2:
    print("Khong phai so nguyen to")
else:
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print("Khong phai so nguyen to")
            break
    else:
        print("La so nguyen to")
"""
    }

    return templates.get(ex_type, f"""# Bai {ex['id']}
print("AI chua hieu bai nay")
""")


# =========================
# 4. TẠO FILE
# =========================
def create_files(exercises):
    if not os.path.exists("output"):
        os.makedirs("output")

    files = []

    for ex in exercises:
        filename = f"output/Bai{ex['id']}.py"

        code = generate_code(ex)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(code)

        files.append(filename)

    return files


# =========================
# 5. PUSH GITHUB
# =========================
def git_push():
    os.system("git add .")
    os.system(f'git commit -m "auto {datetime.now()}"')
    os.system("git push")


# =========================
# MAIN
# =========================
if __name__ == "__main__":

    text = read_input()

    exercises = parse_exercises(text)

    files = create_files(exercises)

    print("✅ Đã tạo:", files)

    git_push()