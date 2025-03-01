#!/usr/bin/env python3
"""
素数判定アルゴリズム集

このスクリプトは以下の素数判定アルゴリズムを実装し、実行結果を比較します：
1. 試し割り法 - 基本的な素数判定法
2. エラトステネスの篩 - 範囲内の素数を効率的に列挙
3. ミラー・ラビン素数判定法 - 確率的素数判定
4. 最適化された素数列挙 - メモリ効率を考慮した実装

実行例: python prime_numbers.py
"""

import math
import random
import time


# ==== 1. 試し割り法（基本的な方法） ====
def is_prime_trial_division(n):
    """
    試し割り法による素数判定
    
    Args:
        n: 判定する整数
    
    Returns:
        bool: nが素数ならTrue、そうでなければFalse
    """
    # 2未満の数は素数ではない
    if n < 2:
        return False
    
    # 2は素数
    if n == 2:
        return True
    
    # 偶数は2以外素数ではない
    if n % 2 == 0:
        return False
    
    # 3以上の奇数で割り切れるかチェック
    # √nまでチェックすれば十分（それ以上の約数があれば、それ以下にも対応する約数がある）
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):  # 奇数のみチェック
        if n % i == 0:
            return False
    
    return True


# ==== 2. エラトステネスの篩（ふるい） ====
def sieve_of_eratosthenes(n):
    """
    エラトステネスの篩による n 以下の素数リストの生成
    
    Args:
        n: この値以下の素数を求める
    
    Returns:
        list: n以下の素数のリスト
    """
    # 初期化: すべての数を素数候補とする
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0と1は素数ではない
    
    # 2から√nまでの数について処理
    for i in range(2, int(math.sqrt(n)) + 1):
        if is_prime[i]:  # iが素数なら
            # iの倍数をすべて除外（i*iから開始して、i刻みで進む）
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    
    # 素数のリストを作成
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes


# ==== 3. ミラー・ラビン素数判定法 ====
def miller_rabin(n, k=5):
    """
    ミラー・ラビン素数判定法
    
    Args:
        n: 判定する数
        k: テスト回数（大きいほど精度が上がる）
    
    Returns:
        bool: 素数である確率が高いならTrue
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    # n-1 = 2^r * d の形に分解する
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # k回のテストを実行
    for _ in range(k):
        a = random.randint(2, n - 2) if n > 3 else 2
        x = pow(a, d, n)  # (a^d) % n を効率的に計算
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # 合成数と判定
    
    return True  # おそらく素数


# ==== 4. 特定の範囲内の素数をすべて列挙する（最適化版） ====
def list_primes_optimized(n):
    """
    n以下のすべての素数を最適化された方法で列挙する
    
    Args:
        n: この値以下の素数を求める
    
    Returns:
        list: n以下の素数のリスト
    """
    # 小さな数の場合は直接リストを返す
    if n < 2:
        return []
    if n == 2:
        return [2]
    
    # 必要なメモリを減らすため、奇数のみを考慮
    # 偶数は2のみが素数
    size = (n - 1) // 2  # 3, 5, ..., n までの奇数の数
    sieve = [True] * size
    
    # 篩にかける
    limit = int(math.sqrt(n))
    for i in range(size):
        if sieve[i]:  # iが素数なら
            # 実際の値は 2*i + 3
            p = 2 * i + 3
            if p > limit:
                break
                
            # pの倍数を除外（まずp*pから始める）
            # p*pの位置を計算: (p*p-3)//2
            start = (p * p - 3) // 2
            # 奇数の倍数のみを除外
            step = p
            for j in range(start, size, step):
                sieve[j] = False
    
    # 素数リストの作成（2と奇数の素数）
    primes = [2] + [2 * i + 3 for i in range(size) if sieve[i]]
    return primes


# ==== 比較関数 ====
def benchmark_prime_algorithms():
    """
    各素数判定アルゴリズムのパフォーマンスを比較
    """
    print("===== 素数判定アルゴリズムのベンチマーク =====")
    
    # 小さな数のテスト
    small_number = 10007  # 素数
    
    print(f"\n1. 試し割り法で {small_number} が素数かチェック:")
    start = time.time()
    result = is_prime_trial_division(small_number)
    elapsed = time.time() - start
    print(f"   結果: {result}, 実行時間: {elapsed:.6f}秒")
    
    print(f"\n3. ミラー・ラビン法で {small_number} が素数かチェック:")
    start = time.time()
    result = miller_rabin(small_number)
    elapsed = time.time() - start
    print(f"   結果: {result}, 実行時間: {elapsed:.6f}秒")
    
    # 中程度の範囲のテスト
    range_limit = 10000
    
    print(f"\n2. エラトステネスの篩で {range_limit} 以下の素数を列挙:")
    start = time.time()
    primes = sieve_of_eratosthenes(range_limit)
    elapsed = time.time() - start
    print(f"   素数の数: {len(primes)}, 実行時間: {elapsed:.6f}秒")
    print(f"   最初の10個: {primes[:10]}")
    print(f"   最後の10個: {primes[-10:]}")
    
    print(f"\n4. 最適化された方法で {range_limit} 以下の素数を列挙:")
    start = time.time()
    primes_opt = list_primes_optimized(range_limit)
    elapsed = time.time() - start
    print(f"   素数の数: {len(primes_opt)}, 実行時間: {elapsed:.6f}秒")
    print(f"   最初の10個: {primes_opt[:10]}")
    print(f"   最後の10個: {primes_opt[-10:]}")
    
    # 結果の検証
    assert primes == primes_opt, "2つの方法で得られた素数リストが一致しません"
    
    # 大きな数のテスト
    large_number = 104729 * 104723  # 合成数
    large_prime = 104729  # 素数
    
    print(f"\n大きな数のテスト:")
    print(f"ミラー・ラビン法で {large_prime} が素数かチェック:")
    start = time.time()
    result = miller_rabin(large_prime)
    elapsed = time.time() - start
    print(f"   結果: {result}, 実行時間: {elapsed:.6f}秒")
    
    print(f"ミラー・ラビン法で {large_number} が素数かチェック:")
    start = time.time()
    result = miller_rabin(large_number)
    elapsed = time.time() - start
    print(f"   結果: {result}, 実行時間: {elapsed:.6f}秒")


# ==== インタラクティブテスト ====
def interactive_test():
    """
    ユーザー入力で素数判定を試す
    """
    while True:
        try:
            print("\n===== 素数判定テスト =====")
            print("1: 試し割り法で素数判定")
            print("2: エラトステネスの篩で範囲内の素数を列挙")
            print("3: ミラー・ラビン法で素数判定")
            print("4: 最適化された方法で範囲内の素数を列挙")
            print("5: ベンチマーク実行")
            print("0: 終了")
            
            choice = int(input("\n選択してください (0-5): "))
            
            if choice == 0:
                break
                
            elif choice == 1:
                n = int(input("判定する数を入力: "))
                start = time.time()
                result = is_prime_trial_division(n)
                elapsed = time.time() - start
                print(f"{n} は{'素数です' if result else '素数ではありません'}")
                print(f"実行時間: {elapsed:.6f}秒")
                
            elif choice == 2:
                n = int(input("上限を入力: "))
                start = time.time()
                primes = sieve_of_eratosthenes(n)
                elapsed = time.time() - start
                print(f"{n}以下の素数の数: {len(primes)}")
                if len(primes) <= 100:
                    print(f"素数リスト: {primes}")
                else:
                    print(f"最初の10個: {primes[:10]}")
                    print(f"最後の10個: {primes[-10:]}")
                print(f"実行時間: {elapsed:.6f}秒")
                
            elif choice == 3:
                n = int(input("判定する数を入力: "))
                k = int(input("テスト回数を入力 (推奨: 5-20): "))
                start = time.time()
                result = miller_rabin(n, k)
                elapsed = time.time() - start
                print(f"{n} は{'おそらく素数です' if result else '合成数です'}")
                print(f"実行時間: {elapsed:.6f}秒")
                
            elif choice == 4:
                n = int(input("上限を入力: "))
                start = time.time()
                primes = list_primes_optimized(n)
                elapsed = time.time() - start
                print(f"{n}以下の素数の数: {len(primes)}")
                if len(primes) <= 100:
                    print(f"素数リスト: {primes}")
                else:
                    print(f"最初の10個: {primes[:10]}")
                    print(f"最後の10個: {primes[-10:]}")
                print(f"実行時間: {elapsed:.6f}秒")
                
            elif choice == 5:
                benchmark_prime_algorithms()
                
            else:
                print("無効な選択です。0から5の数字を入力してください。")
                
        except ValueError:
            print("数値を入力してください。")
        except KeyboardInterrupt:
            print("\n終了します...")
            break


if __name__ == "__main__":
    print("素数判定アルゴリズム集")
    print("=" * 30)
    print("このプログラムでは4つの素数判定アルゴリズムの実装と比較を行います。")
    
    try:
        interactive_test()
    except KeyboardInterrupt:
        print("\nプログラムを終了します。")