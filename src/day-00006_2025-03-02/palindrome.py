def is_palindrome_simple(text):
    """
    シンプルな方法でパリンドロームを判定する関数
    文字列を反転して元の文字列と比較する
    """
    # 文字列を小文字に変換し、スペースと記号を削除
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    # 反転して比較
    return cleaned_text == cleaned_text[::-1]

def is_palindrome_two_pointer(text):
    """
    ポインタを使用した方法でパリンドロームを判定する関数
    左右から同時に文字を比較する
    """
    # 文字列を小文字に変換し、スペースと記号を削除
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    left, right = 0, len(cleaned_text) - 1
    while left < right:
        if cleaned_text[left] != cleaned_text[right]:
            return False
        left += 1
        right -= 1
    
    return True

def is_palindrome_recursive(text):
    """
    再帰を使用してパリンドロームを判定する関数
    """
    # 文字列を小文字に変換し、スペースと記号を削除
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    def check_palindrome(s, left, right):
        # 基底ケース: 左ポインタが右ポインタを超えたら、パリンドロームである
        if left >= right:
            return True
        # 現在の左右の文字が異なる場合、パリンドロームではない
        if s[left] != s[right]:
            return False
        # 再帰的に内側の部分文字列をチェック
        return check_palindrome(s, left + 1, right - 1)
    
    return check_palindrome(cleaned_text, 0, len(cleaned_text) - 1)

# テスト
test_strings = [
    "A man, a plan, a canal, Panama",
    "race a car",
    "Was it a car or a cat I saw?",
    "No 'x' in Nixon",
    "Not a palindrome",
    "12321",
    "Madam, I'm Adam",
    "じいさんてんさいじ"
]

print("シンプルな方法:")
for s in test_strings:
    print(f'"{s}" -> {is_palindrome_simple(s)}')

print("\nポインタを使用した方法:")
for s in test_strings:
    print(f'"{s}" -> {is_palindrome_two_pointer(s)}')

print("\n再帰を使用した方法:")
for s in test_strings:
    print(f'"{s}" -> {is_palindrome_recursive(s)}')

# シンプルな方法：文字列を反転して元の文字列と比較する方法です。Pythonの文字列スライシング [::-1] を使って文字列を簡単に反転できます。
# 二重ポインタ法：文字列の両端から内側に向かって文字を比較していく方法です。左端と右端から同時に文字を比較し、不一致があればパリンドロームではないと判断します。
# 再帰的方法：再帰関数を使用して、文字列の外側から内側へと比較を進めていく方法です。