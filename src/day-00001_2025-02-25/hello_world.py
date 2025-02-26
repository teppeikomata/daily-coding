import unittest
import io
import sys
from contextlib import redirect_stdout

def simple():
    print("Hello, World!!")


def var():
    message = 'Hello, World!!'
    print(message)


def concat_str(hello,world):
    print(hello+', '+ world + '!!')


def format_str(world):
    # フォーマット文字列(python 3.6+)
    print(f"Hello, {world}!!")

def format_method(world):
    # str.format()メソッド
    print("Hello, {}!!".format(world))

def main():

    hello = 'Hello'
    world = 'World'

    simple()
    var()
    concat_str(hello,world)
    format_str(world)
    format_method(world)

# Hello, world!!テストクラス
class TestHelloFiveLines(unittest.TestCase):

    def test_five_hello_lines(self):
        # main関数がHello, world!!を五行出力することをテスト
        
        # 標準出力をキャプチャ
        f = io.StringIO()
        with redirect_stdout(f):
            main()
        
        # 出力を取得して行ごとに分割
        output = f.getvalue()
        output_lines = output.splitlines()
        #行数の確認
        self.assertEqual(len(output_lines),5,f"lines : {len(output_lines)}")
        # 各行がHello, world!!であることを検証
        for idx,line in enumerate(output_lines):
            self.assertEqual(line,f"Hello, World!!","{idx}:Expected Hello, World!! :{line}")

    def test_output_content(self):
        # 出力内容が期待通りであることをテスト
        expected_output = "Hello, World!!\n" * 5

        # 標準出力をキャプチャ
        f = io.StringIO()
        with redirect_stdout(f):
            main()
        
        # 出力全体を検証
        self.assertEqual(f.getvalue(), expected_output, "出力が期待通りではありません")
        

if __name__ == "__main__":
    main()
    unittest.main()
