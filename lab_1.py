def print_finland_flag():
    blue_bg = '\033[44m  \033[0m'  
    white_bg = '\033[47m  \033[0m' 
    print("Флаг Финляндии:")
    for i in range(8):
        if i in [3, 4]:  
            print(blue_bg * 8)
        else: 
            print(white_bg * 2 + blue_bg * 3 + white_bg * 3)

def print_pattern_i(count=2):
    white = '\033[47m \033[0m'
    black = '\033[40m \033[0m'
    height = 11
    for _ in range(count):
        for row in range(height):
            dist_from_center = abs(row - height // 2)
            left_black_pos = dist_from_center
            right_black_pos = 17 - dist_from_center
            line = ""
            for col in range(18):
                if col == left_black_pos or col == right_black_pos:
                    line += black
                else:
                    line += white
            print(line)
        if _ < count - 1:
            print()

def print_function_graph():
    print("График функции y = x/2")
    for y in range(9, -1, -1):
        x = y * 2
        line = f"y={y:2d} |"
        for i in range(21):
            if i == x:
                line += "*"
            else:
                line += " "
        print(line)
    print("    +" + "-" * 20)
    print("     0 2 4 6 8 10 12 14 16 18")

def print_percentage_diagram():
    file = open('sequence.txt', 'r')
    numbers = []
    for line in file:
        clean_line = line.strip()
        if clean_line:
            number = float(clean_line)
            numbers.append(number)

    filtered_numbers = []
    for num in numbers:
        if (5 <= num <= 10) or (-10 <= num <= -5):
            filtered_numbers.append(num)
   
    positive_count = 0
    negative_count = 0
    
    for num in filtered_numbers:
        if num > 0:
            positive_count += 1
        else:
            negative_count += 1
    total_count = len(filtered_numbers)
    if total_count > 0:
        positive_percent = (positive_count / total_count) * 100
        negative_percent = (negative_count / total_count) * 100
    else:
        positive_percent = 0
        negative_percent = 0
    print(f"\nДиаграмма процентного соотношения:")
    print(f"Положительные числа [5;10]: {positive_count} ({positive_percent:.1f}%)")
    print(f"Отрицательные числа [-10;-5]: {negative_count} ({negative_percent:.1f}%)")
    print("\nДиаграмма:")
    positive_bars = int(positive_percent / 5)
    negative_bars = int(negative_percent / 5)
    print("Положительные [5;10]: " + "#" * positive_bars + f" {positive_percent:.1f}%")
    print("Отрицательные [-10;-5]: " + "#" * negative_bars + f" {negative_percent:.1f}%")


if __name__ == "__main__":
    print("=" * 50)
    print("Задание 1: Флаг Финляндии")
    print("=" * 50)
    print_finland_flag()
    
    print("\n" + "=" * 50)
    print("Задание 2: Узор")
    print("=" * 50)
    print_pattern_i(2)
    
    print("\n" + "=" * 50)
    print("Задание 3: График функции y = x/2")
    print("=" * 50)
    print_function_graph()
    
    print("\n" + "=" * 50)
    print("Задание 4: Диаграмма процентного соотношения")
    print("=" * 50)
    print_percentage_diagram()