def AND(a, b):
    return a * b

def NOT(a):
    return 1.0 - a

P0_4 = 0.4
P0_5 = 0.5
P0_6 = NOT(P0_4)

print("Question 2(a)\n")

# 2(a)(i): 0.8881188
w1  = P0_4
w2  = NOT(AND(P0_4, w1))      # 0.84
w3  = AND(P0_5, w2)           # 0.42
w4  = NOT(AND(P0_5, w3))      # 0.79
w5  = NOT(AND(P0_6, w4))      # 0.526
w6  = AND(P0_4, w5)           # 0.2104
w7  = NOT(AND(P0_4, w6))      # 0.91584
w8  = NOT(AND(P0_4, w7))      # 0.633664
w9  = AND(P0_5, w8)           # 0.316832
w10 = AND(P0_5, w9)           # 0.158416
w11 = NOT(AND(P0_5, w10))     # 0.920792
w12 = NOT(AND(P0_6, w11))     # 0.4475248
w13 = AND(P0_5, w12)          # 0.2237624
ans1 = NOT(AND(P0_5, w13))    # 0.8881188

print("2(a)(i) target = 0.8881188")
print("value =", ans1)
print()

# 2(a)(ii): 0.2119209
w1  = P0_6
w2  = AND(P0_5, w1)           # 0.3
w3  = AND(P0_5, w2)           # 0.15
w4  = NOT(AND(P0_5, w3))      # 0.925
w5  = NOT(AND(P0_6, w4))      # 0.445
w6  = NOT(AND(P0_6, w5))      # 0.733
w7  = AND(P0_5, w6)           # 0.3665
w8  = NOT(AND(P0_5, w7))      # 0.81675
w9  = AND(P0_5, w8)           # 0.408375
w10 = NOT(AND(P0_4, w9))      # 0.83665
w11 = AND(P0_5, w10)          # 0.418325
w12 = NOT(AND(P0_5, w11))     # 0.7908375
w13 = AND(P0_6, w12)          # 0.4745025
ans2 = AND(P0_5, w13)         # 0.23725125

print("2(a)(ii) target = 0.2119209")
print("value =", ans2)
print("note: this chain is only an example structure, not an exact match")
print()

# 2(a)(iii): 0.5555555
w1  = P0_6
w2  = AND(P0_6, w1)           # 0.36
w3  = AND(P0_6, w2)           # 0.216
w4  = NOT(AND(P0_4, w3))      # 0.9136
w5  = NOT(AND(P0_5, w4))      # 0.5432
w6  = AND(P0_5, w5)           # 0.2716
w7  = NOT(AND(P0_5, w6))      # 0.8642
w8  = AND(P0_6, w7)           # 0.51852
ans3 = NOT(AND(P0_5, w8))     # 0.74074

print("2(a)(iii) target = 0.5555555")
print("value =", ans3)
print("note: this chain is only an example structure, not an exact match")
print()

print("Question 2(b)\n")

def OR(a, b):
    return NOT(AND(NOT(a), NOT(b)))

def binary_value(bits):
    val = 0.0
    for i, bit in enumerate(bits, start=1):
        if bit == '1':
            val += 2**(-i)
    return val

targets = ["1011111", "1101111", "1010111"]

for bits in targets:
    val = binary_value(bits)
    print(f"target = 0.{bits}_2")
    print("value  =", val)
    print()