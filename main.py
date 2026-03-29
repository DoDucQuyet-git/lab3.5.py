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
def generate_code(ex):
    content = ex["content"]

    # Bài chia hết
    if "chia hết cho 2" in content and "3" in content:
        return f"""# Bai {ex['id']}
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

    # Bài phương trình bậc 2
    if "phương trình bậc 2" in content:
        return f"""# Bai {ex['id']}
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

    return f"""# Bai {ex['id']}
print("Chua ho tro dang bai nay")
"""


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