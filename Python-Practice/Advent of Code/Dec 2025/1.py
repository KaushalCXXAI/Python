inputs = [line.strip() for line in open("input1.txt") if line.strip()]

# inputs = ["L68","L30","R48","L5","R60","L55","L1","L99","R14","L82"]
# inputs = ["L300"]
current = 50
code = int(0)
for i in inputs:
    direction = "L" if i[:1] == "L" else "R"
    i = int(i[1:])
    print(f"{direction}{i}",end=" ")
    if direction == "L":
        if current > i  or current == i:
            current -= i
        elif i < 100:
            current = 100 - (( current - i )* -1)

        if  i > 100:
            current = ( current - i ) * -1
            while current > 100 :
                    current = ( 100 - current )* -1
                    if current == 100:
                        current = 0
                        break

        if current == 100:
            current = 0
        # print("current in L : ", current)
    elif direction == "R":
        # print("current in R befor any edit", current)
        Right_Rotation = current + i


        if Right_Rotation > 100:
            while Right_Rotation > 100 :
                    Right_Rotation -= 100
                    if Right_Rotation == 100:
                        current = 0
                        break
            # print("current in R right after loop ends will be 0 is point at 100 : ", current)
            ans = current + Right_Rotation
            current = ans if ans < 100 else (100 - ans)
            # print("current in else if rr > 100 (loop part) : ", current)
        else:
            current = Right_Rotation
            # print("current in else if rr < 100 : ", current)
        current = 0 if Right_Rotation == 100 else Right_Rotation
        # print("current in R : ", current)
    print(current)
    if current == 0:
        code += 1


print(code)