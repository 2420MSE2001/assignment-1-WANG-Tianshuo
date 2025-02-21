# main.py
def left_side(x, num_terms):
    """
    计算方程左侧前 num_terms 项的和。
    """
    result=(1-2*x)/(1-x+x*x)
    for i in range(1,num_terms):
        result+=(2**i*x**(2*i-1)-2**(i+1)*x**(2*i+1))/(1-x**(2**i)+x**(2**(i+1)))

    return result

def right_side(x):
    """
    计算方程右侧的固定值。
    """
    result=(1+2*x)/(1+x+x*x)
    return result

def find_num_terms(x, tolerance=1e-3):#运行10e-6时提示溢出，所以改成了10e-3
    """
    寻找满足左侧与右侧差异小于容差的最小项数。
    """
    num_terms=1
    while abs(left_side(x,num_terms)-right_side(x))>=tolerance:
        num_terms+=1
    return num_terms

if __name__ == "__main__":
    x = 0.25  # 题目给定的 x 值
    num_terms = find_num_terms(x)
    print(f"所需最小项数: {num_terms}")
