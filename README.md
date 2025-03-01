# daily-coding

## ルール
- src内に、day(n)_yyyy-mm-ddというディレクトリを作成してその中のREADME.mdに内容を書いておく
    - create_folder.pyを実行するとフォルダが自動作成される
- なるべく毎日やるが、できない日があってもいい
- 開発環境とか特に作らずpython以外はシンプルにやる
- 言語
    - python
        ```
        . .venv/bin/activate
        python hello.py
        ```
    - Java
        ``` 
        javac Hello.java
        java Hello
        ```
    - JavaScript(Node.js)
        ```
        node hello.js
        ```

    - Rust
        ```
        rustc hello.rs
        ./hello.rs
        ``` 
    - C++
        ```
        g++ -o hello hello.cpp
        or
        g++ -std=c++17 type.cpp -o type
        ./hello
        ```

    - Scala
        ```
        scalac Hello.scala
        scala -cp . -M Hello
        
        or 
        
        scala Hello.scala
        ```
  
    - Go
        ```
        go run hello.go
        or 
        go build hello.go
        ./hello
        ```


``` 言語に関しては下記の方法で進める
# プログラミング言語の基礎的要素

## 1. データと型
- 基本データ型（整数、浮動小数点数、文字、論理値など）
- 複合データ型（配列、リスト、辞書/マップ、タプルなど）
- 型システム（静的型付け vs 動的型付け、強い型付け vs 弱い型付け）
- 型変換とキャスト
- 定数と変数

## 2. 演算子と式
- 算術演算子（+, -, *, /, %）
- 比較演算子（==, !=, <, >, <=, >=）
- 論理演算子（AND, OR, NOT）
- ビット演算子（&, |, ^, ~, <<, >>）
- 代入演算子（=, +=, -=など）
- 演算子の優先順位と結合性

## 3. 制御フロー
- 条件分岐（if-else, switch-case）
- ループ（for, while, do-while）
- ジャンプ文（break, continue, return, goto）
- 例外処理（try-catch-finally）

## 4. 関数とプロシージャ
- 関数定義と宣言
- パラメータ渡し（値渡し、参照渡し）
- 戻り値
- 再帰
- ラムダ式と無名関数
- クロージャ
- 高階関数

## 5. モジュール性とスコープ
- 名前空間
- モジュールとパッケージ
- インポート/エクスポートの仕組み
- スコープとライフタイム（グローバル、ローカル）
- 可視性修飾子（public, private, protectedなど）

## 6. オブジェクト指向の概念
- クラスとオブジェクト
- 継承
- カプセル化
- ポリモーフィズム
- インターフェース
- 抽象クラス
- メソッドオーバーライドとオーバーロード

## 7. 構造体とデータ構造
- 構造体の定義と利用
- ユーザー定義型
- 列挙型（enum）
- 共用体（union）

## 8. メモリ管理
- スタックとヒープ
- ガベージコレクション vs 手動メモリ管理
- ポインタとリファレンス

## 9. 並行処理と非同期プログラミング
- スレッドとプロセス
- 同期プリミティブ（ミューテックス、セマフォなど）
- 非同期プログラミングモデル（Promise, async/await）
- イベント駆動プログラミング

## 10. ジェネリックプログラミング
- テンプレートとジェネリクス
- 型パラメータ
- 制約と境界
```