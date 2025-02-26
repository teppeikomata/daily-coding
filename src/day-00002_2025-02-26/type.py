"""
Pythonの主要な型とその使用例を示すサンプルコード
"""
from icecream import ic 
# 基本的な型 -----------------------------------------
print("基本的な型")
# int型: 整数値を表現。計算、カウント、インデックス参照などに使用
print("int型: 整数値を表現。計算、カウント、インデックス参照などに使用")
integer_value = 42
ic(integer_value)
ic(integer_value + 10)# 算術演算
ic(integer_value // 10) # 整数除算

# float型: 小数点を含む数値。科学計算や割合の表現などに使用
print("float型: 小数点を含む数値。科学計算や割合の表現などに使用")
float_value = 3.14
print(float_value)
ic(float_value * (5 ** 2))  # 円の面積計算

# bool型: 真偽値。条件分岐やフラグとして使用
print("# bool型: 真偽値。条件分岐やフラグとして使用")
boolean_value = True
if boolean_value:
    print("条件は真です")
is_active = False  # ユーザーの状態を表すフラグ

# complex型: 複素数。科学計算や信号処理などに使用
print("complex型: 複素数。科学計算や信号処理などに使用")
complex_value = 1 + 2j
ic(complex_value)
magnitude = abs(complex_value)  # 複素数の大きさ
ic(magnitude)
conjugate = complex_value.conjugate()  # 共役複素数
ic(conjugate)

# str型: 文字列。テキストデータの表現やメッセージ表示などに使用
print("str型: 文字列。テキストデータの表現やメッセージ表示などに使用")
string_value = "Hello, World!"
ic(string_value)
greeting = "こんにちは、" + "世界！"  # 文字列連結
ic(greeting)
multiline = """複数行の
テキストも
表現できます"""  # 複数行の文字列
ic(multiline)

# シーケンス型 -----------------------------------------
print("シーケンス型")
# list型: 順序付き可変コレクション。データの集合や順序が重要な場合に使用
print("list型: 順序付き可変コレクション。データの集合や順序が重要な場合に使用")
list_value = [1, 2, 3, 4, 5]
ic(list_value)
list_value.append(6)  # 要素の追加
ic(list_value)
first_three = list_value[:3]  # スライス処理
ic(first_three)

# tuple型: 順序付き不変コレクション。変更されない値のグループや多値返却に使用
print("tuple型: 順序付き不変コレクション。変更されない値のグループや多値返却に使用")
tuple_value = (1, 2, 3, 4, 5)
ic(tuple_value)
x, y, z = (10, 20, 30)  # アンパック
ic(x,y,z)
point = (3.5, 4.2)  # 座標点など、関連する値のグループ化
ic(point)

# range型: 数値シーケンス。ループの反復回数指定やインデックス生成に使用
print("range型: 数値シーケンス。ループの反復回数指定やインデックス生成に使用")
range_value = range(10)  # 0から9までの数値シーケンス
ic(range_value)
for i in range(5):
    ic(i)  # 0から4まで順に表示（ループ制御）
even_numbers = range(0, 10, 2)  # 0, 2, 4, 6, 8（偶数のみ）
ic(even_numbers)

# マッピング型 -----------------------------------------
print("マッピング型")
# dict型: キーと値のペアを格納。関連データの検索や構造化に使用
print("dict型: キーと値のペアを格納。関連データの検索や構造化に使用")
dict_value = {"name": "Alice", "age": 30, "email": "alice@example.com"}
ic(dict_value)
user_age = dict_value["age"]  # キーによる値の取得
ic(user_age)
dict_value["location"] = "Tokyo"  # 新しいキー・値の追加
ic(dict_value)
employee_data = {
    "id": "E12345",
    "department": "Engineering",
    "manager": "Bob Smith"
}  # 構造化データの表現
ic(employee_data)

# セット型 -----------------------------------------
print("セット型")
# set型: 重複のない可変コレクション。一意の値の集合や集合演算に使用
print("set型: 重複のない可変コレクション。一意の値の集合や集合演算に使用")
set_value = {1, 2, 3, 4, 5}
ic(set_value)
set_value.add(6)  # 要素の追加
ic(set_value)
unique_chars = set("mississippi")  # 'm', 'i', 's', 'p'（重複除去）
ic(unique_chars)
is_member = 3 in set_value  # 所属判定（高速）
ic(is_member)
tags = {"python", "programming", "tutorial"}  # タグのような一意の識別子
ic(tags)
ic(type(tags))

# frozenset型: 重複のない不変コレクション。辞書のキーやセットの要素として使用可能
print("frozenset型: 重複のない不変コレクション。辞書のキーやセットの要素として使用可能")
frozenset_value = frozenset([1, 2, 3])
ic(frozenset_value)
# ハッシュ可能なため、辞書のキーに使用可能
cache = {frozenset([1, 2]): "data for [1, 2]"}
ic(cache)

# 商品IDの組み合わせごとの割引率
discount_rates = {
    frozenset([101, 102]): 10,  # 商品101と102を一緒に買うと10%オフ
    frozenset([101, 103, 105]): 15,  # 商品101、103、105を一緒に買うと15%オフ
}
ic(discount_rates)

# カートの中の商品
cart = [105, 101, 103]
ic(cart)
# 割引を計算
cart_set = frozenset(cart)
ic(cart_set)
if cart_set in discount_rates:
    discount = discount_rates[cart_set]
    print(f"適用される割引率: {discount}%")  # "適用される割引率: 15%" が表示される

# 不変なので、一度生成後は変更不可
# frozenset_value.add(4)  # これはエラーになる

# バイナリシーケンス型 -----------------------------------------
print("バイナリシーケンス型")
# bytes型: 不変バイト列。バイナリデータや文字エンコーディングに使用
print("bytes型: 不変バイト列。バイナリデータや文字エンコーディングに使用")
bytes_value = b"hello"
ic(bytes_value)
file_signature = bytes([0x89, 0x50, 0x4E, 0x47])  # PNGファイルの先頭バイト
ic(file_signature)
encoded = "こんにちは".encode('utf-8')  # 文字列をバイトにエンコード
ic(encoded)

# bytearray型: 可変バイト列。バイナリデータの編集に使用
print("bytearray型: 可変バイト列。バイナリデータの編集に使用")
bytearray_value = bytearray(b"hello")
ic(bytearray_value)
bytearray_value[0] = 72  # 'h'を'H'に変更
ic(bytearray_value)
buffer = bytearray(1024)  # 1KBのバッファ初期化
ic(buffer)

# memoryview型: メモリ内のバイトデータの効率的なアクセスに使用
print("memoryview型: メモリ内のバイトデータの効率的なアクセスに使用、大規模なバイナリデータに有用")
memoryview_value = memoryview(bytes_value)
ic(memoryview_value)
first_byte = memoryview_value[0]  # コピーなしでデータにアクセス
ic(first_byte)
slice_view = memoryview_value[1:3]  # コピーなしでスライス処理
ic(slice_view)

# その他の型 -----------------------------------------
print("その他の型")
# None型: 値の不在を表す。初期化や関数の戻り値などに使用
print("None型: 値の不在を表す。初期化や関数の戻り値などに使用")
none_value = None
ic(none_value)
def optional_operation(value=None):
    if value is None:
        return "デフォルト処理"
    return f"値 {value} での処理"
ic(optional_operation())

# type型: オブジェクトの型を表す。型チェックや動的オブジェクト生成に使用
print("type型: オブジェクトの型を表す。型チェックや動的オブジェクト生成に使用")
type_value = type(42)  # <class 'int'>
ic(type_value)
if type("hello") is str:
    print("これは文字列です")

# object型: 全てのクラスの基底。汎用オブジェクトやプレースホルダとして使用
print("object型: 全てのクラスの基底。汎用オブジェクトやプレースホルダとして使用")
object_value = object()
ic(object_value)
# カスタムクラスの基底クラスとして使用
class CustomObject(object):
    pass
# 上記と同義
class CustomObject2:
    pass

# Ellipsis型: 省略記号。多次元配列のスライスや未実装部分の表現に使用
print("Ellipsis型: 省略記号。多次元配列のスライスや未実装部分の表現に使用")
ellipsis_value = ...
ic(ellipsis_value)
# NumPyなどでの次元指定
# array[..., 0] は全ての次元の最初の要素
import numpy as np
array = np.zeros((5, 5, 5))  # 3次元配列
ic(array)
# 最初の次元はすべて、最後の次元は0番目の要素を取得
subset = array[..., 0]
ic(subset)
# これは以下と同等:
subset2 = array[:, :, 0]
ic(subset2)

# 具体例
array = np.zeros((2, 3, 4))  # 2x3x4の3次元配列

# 各要素を一意に特定できる値で埋める
# 100*i + 10*j + k の形式で値を設定（i,j,kはそれぞれの次元のインデックス）
for i in range(2):
    for j in range(3):
        for k in range(4):
            array[i, j, k] = 100*i + 10*j + k

# 配列全体を表示
print("===== 元の3次元配列 =====")
ic(array)
ic("\n形状:", array.shape)  # (2, 3, 4)

print("\n===== array[..., 0] の結果 =====")
subset = array[..., 0]
ic(subset)
ic("\n形状:", subset.shape)  # (2, 3)

# NotImplemented型: 特殊メソッドが特定の入力に対応していないことを示す
print("NotImplemented型: 特殊メソッドが特定の入力に対応していないことを示す")
notimplemented_value = NotImplemented
ic(notimplemented_value)
class CustomNumber:
    def __add__(self, other):
        if isinstance(other, CustomNumber):
            return CustomNumber()
        return NotImplemented  # 他の型との加算は未実装

#class CustomNumber: - カスタム数値クラスを定義しています。
#def __add__(self, other): - + 演算子の動作を定義する特殊メソッドです。例えば a + b という式があると、Python は a.__add__(b) を呼び出します。
#if isinstance(other, CustomNumber): - もし足し算の相手も CustomNumber クラスのインスタンスなら...
#return CustomNumber() - 同じクラス同士の加算は実装されており、新しい CustomNumber インスタンスを返します。
#return NotImplemented - 異なる型との加算は実装していないことを Python に伝えます。
#NotImplemented を返すと、Python はもう一方のオブジェクトの反対向きのメソッド（この場合は other.__radd__(self)）を試すようになります。それも実装されていなければ、TypeError が発生します。

a = CustomNumber()
b = CustomNumber()
c = a + b  # 動作する（CustomNumber インスタンスを返す）
# d = a + 5  # NotImplemented が返されるので、int.__radd__(a) が試されるがこれも実装されていないため、TypeError が発生

# コレクション関連（importが必要）-----------------------------------------
print("コレクション関連（importが必要）")
import collections

# namedtuple: フィールド名を持つタプル。小さなデータ構造やレコードに使用
Person = collections.namedtuple('Person', ['name', 'age'])
person = Person("Bob", 25)
print(person.name)  # 名前付きフィールドでアクセス
# データベースの行やCSVレコードの表現に最適

# deque: 両端キュー。両端からの高速な挿入・削除が必要な場合に使用
deque_value = collections.deque([1, 2, 3])
deque_value.appendleft(0)  # 左端に追加
deque_value.pop()  # 右端から削除
# キュー、スタック、または固定サイズバッファとして使用

# ChainMap: 複数の辞書を結合。設定の階層や検索順序が必要な場合
chainmap_value = collections.ChainMap({'a': 1}, {'b': 2}, {'a': 3})
# 最初のマップで見つかった値が使用される: chainmap_value['a'] は 1
# 設定の階層（デフォルト→ユーザー設定→一時的な設定）などに使用

# Counter: 要素のカウント。頻度分析や集計に使用
counter_value = collections.Counter(['a', 'b', 'a', 'c', 'a'])
most_common = counter_value.most_common(2)  # [('a', 3), ('b', 1)]
# テキスト分析、投票集計、インベントリ管理などに有用

# OrderedDict: 挿入順序を保持する辞書。順序が重要な場合に使用
ordered_dict = collections.OrderedDict([('a', 1), ('b', 2)])
ordered_dict['c'] = 3  # 挿入順で保持
# Python 3.7以降では通常のdictも順序を保持するが、明示的な意図の表現に使用

# defaultdict: キーが存在しない場合にデフォルト値を提供する辞書
default_dict = collections.defaultdict(int)  # 存在しないキーに対して0を返す
default_dict['a'] += 1  # 'a'が存在しなくても、エラーにならず1になる
# グループ化や頻度カウントなどに便利
word_counts = collections.defaultdict(int)
for word in ["apple", "banana", "apple", "orange"]:
    word_counts[word] += 1

# 型ヒント関連（Python 3.5以降）-----------------------------------------
print("型ヒント関連")
from typing import List, Dict, Set, Tuple, Union, Optional, Any, Callable

# 基本的な型ヒント: コードの意図を明確にし、静的型チェックを可能にする
def greet(name: str) -> str:
    """名前を受け取り、挨拶を返す関数"""
    return f"Hello, {name}!"

# List: 特定の型のリスト。要素の型を統一したいコレクションに使用
numbers: List[int] = [1, 2, 3]
# 数値のみのリストであることを明示

# Dict: キーと値の型を指定した辞書。構造化データの型定義に使用
name_ages: Dict[str, int] = {"Alice": 30, "Bob": 25}
# 文字列をキー、整数を値とする辞書であることを明示

# Set: 特定の型の集合。一意の値のコレクションの型定義に使用
unique_numbers: Set[int] = {1, 2, 3}
# 整数のセットであることを明示

# Tuple: 複数の型からなるタプル。固定長の異なる型の集合に使用
coordinates: Tuple[float, float] = (10.5, 20.3)
# 2つの浮動小数点数からなる座標のような構造

# Union: 複数の型のいずれか。多様な型を受け入れる場合に使用
result: Union[int, str] = "success"
# 整数か文字列のいずれかであることを示す
def process_input(value: Union[int, str, float]) -> str:
    return str(value)

# Optional: 特定の型またはNone。値が存在しない可能性がある場合に使用
maybe_name: Optional[str] = None  # str | None と同等
# 文字列またはNoneであることを示す
def find_user(id: int) -> Optional[Dict[str, Any]]:
    # ユーザーが見つからない場合はNoneを返す可能性がある
    pass

# Any: 任意の型。型制約がない場合に使用（なるべく避けるべき）
anything: Any = 42  # どんな型でも許容
# 型チェックを一部分だけ無効にしたい場合や、動的な型の場合に使用

# Callable: 呼び出し可能なオブジェクト。関数やメソッドの型定義に使用
callback: Callable[[int, int], int] = lambda x, y: x + y
# 2つのintを引数に取り、intを返す関数であることを示す
def apply_operation(x: int, y: int, operation: Callable[[int, int], int]) -> int:
    return operation(x, y)