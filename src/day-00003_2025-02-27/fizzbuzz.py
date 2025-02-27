import math 

def lcm(num1,num2):
    """
    2つの数の最小公倍数（LCM）を計算する関数

    Args:
        num1: 1つ目の数
        num2: 2つ目の数
    
    Returns:
         最小公倍数
    """
    # 最小公倍数 = (num1 * num2 ) / 最大公約数
    return (num1 * num2 )// math.gcd(num1,num2)


def lcm_of_multiple_numbers(numbers):
    """
    任意の数のリストの最小公倍数を計算する関数

    Args:
        numbers: 数値のリスト

    Returns:
        最小公倍数
    """
    if not numbers:
        return 0
    # 先頭の値を取得
    result = numbers[0]
    # 先頭の値との最小公倍数を取得していってそれと後続の最小公倍数を求めていく
    for num in numbers[1:]:
        result = lcm(result,num)
    return result 

if __name__ == "__main__":

    print(lcm(3,5))
    print(lcm_of_multiple_numbers([7,3,4]))

    print('=======FizzBuzz======')
    for i in range(1,101):
        if i % lcm(3,5) == 0:
            print("FizzBuzz")
        elif i%3 == 0:
            print("Fizz")
        elif i%5 == 0:
            print("Buzz")
        else:
            print(i)

# memo
# 最大公約数は素因数分解して、共通する素数の最小指数を取得する
# 最大公倍数は素因数分解して、共通する素数の最大指数を取得する