package main

import (
	"fmt"
	"math"
	"reflect"
	"strconv"
	"strings"
	"time"
)

// 構造体の定義
type Person struct {
	Name    string
	Age     int
	Married bool
}

// 構造体にメソッドを追加
func (p Person) Greet() string {
	return fmt.Sprintf("こんにちは、%sです。%d歳です。", p.Name, p.Age)
}

// ポインタレシーバを使ったメソッド（値を変更できる）
func (p *Person) HaveBirthday() {
	p.Age++
}

// インターフェースの定義
type Greeter interface {
	Greet() string
}

func main() {
	fmt.Println("================ Go言語の基本データ型 ================")

	// -------------------- 基本型 --------------------
	fmt.Println("\n-- 基本型 --")

	// 整数型
	var i int = 42
	var i8 int8 = 127       // -128～127
	var i16 int16 = 32767   // -32768～32767
	var i32 int32 = 2147483647
	var i64 int64 = 9223372036854775807
	
	// 符号なし整数型
	var ui uint = 42
	var ui8 uint8 = 255      // 0～255
	var ui16 uint16 = 65535  // 0～65535
	
	fmt.Println("整数型:")
	fmt.Printf("int: %v, 型: %T\n", i, i)
	fmt.Printf("int8: %v, 型: %T\n", i8, i8)
	fmt.Printf("int16: %v, 型: %T\n", i16, i16)
	fmt.Printf("int32: %v, 型: %T\n", i32, i32)
	fmt.Printf("int64: %v, 型: %T\n", i64, i64)
	fmt.Printf("uint: %v, 型: %T\n", ui, ui)
	fmt.Printf("uint8: %v, 型: %T\n", ui8, ui8)
	fmt.Printf("uint16: %v, 型: %T\n", ui16, ui16)
	
	// 浮動小数点型
	var f32 float32 = 3.14159265358979323846
	var f64 float64 = 3.14159265358979323846
	
	fmt.Println("\n浮動小数点型:")
	fmt.Printf("float32: %v, 型: %T\n", f32, f32)
	fmt.Printf("float64: %v, 型: %T\n", f64, f64)
	fmt.Printf("float32の精度制限: %.20f\n", f32) // 精度が失われることを示す
	
	// 複素数型
	var c64 complex64 = complex(1, 2)    // (1+2i)
	var c128 complex128 = complex(3, 4)  // (3+4i)
	
	fmt.Println("\n複素数型:")
	fmt.Printf("complex64: %v, 型: %T\n", c64, c64)
	fmt.Printf("complex128: %v, 型: %T\n", c128, c128)
	fmt.Printf("実部: %v, 虚部: %v\n", real(c64), imag(c64))
	fmt.Printf("complex128の実部: %v, 虚部: %v\n", real(c128), imag(c128))
	
	// ブール型
	var t bool = true
	var f bool = false
	
	fmt.Println("\nブール型:")
	fmt.Printf("true: %v, false: %v\n", t, f)
	fmt.Printf("論理演算: %v && %v = %v\n", t, f, t && f)
	fmt.Printf("論理演算: %v || %v = %v\n", t, f, t || f)
	fmt.Printf("否定: !%v = %v\n", t, !t)
	
	// 文字列型
	var s string = "こんにちは、Go言語"
	var multiline string = `これは
複数行の
文字列です。`
	
	fmt.Println("\n文字列型:")
	fmt.Printf("文字列: %v\n", s)
	fmt.Printf("長さ（バイト数）: %v\n", len(s))
	fmt.Printf("RuneCount（文字数）: %v\n", len([]rune(s)))
	fmt.Printf("複数行文字列: \n%v\n", multiline)
	
	// 文字列操作
	fmt.Println("\n文字列操作:")
	fmt.Printf("部分文字列: %v\n", s[0:5]) // 注意: バイト単位なので日本語は壊れる
	fmt.Printf("文字列結合: %v\n", s + "です。")
	fmt.Printf("文字列に含まれるか: %v\n", strings.Contains(s, "Go"))
	fmt.Printf("文字列分割: %v\n", strings.Split("a,b,c", ","))
	fmt.Printf("文字列置換: %v\n", strings.Replace(s, "Go", "Golang", 1))
	
	// ルーン型（Unicode文字）
	var r rune = 'あ'
	
	fmt.Println("\nルーン型:")
	fmt.Printf("ルーン: %v, 型: %T, Unicode: %U\n", r, r, r)
	
	// 文字列を1文字ずつ処理（正しい方法）
	for i, runeValue := range s {
		fmt.Printf("位置 %d: %c (%U)\n", i, runeValue, runeValue)
		if i > 5 {
			break // 出力を短くするため
		}
	}
	
	// バイト型（uint8の別名）
	var b byte = 65
	fmt.Println("\nバイト型:")
	fmt.Printf("バイト: %v, 文字として: %c\n", b, b)
	
	// -------------------- 変数宣言と型推論 --------------------
	fmt.Println("\n-- 変数宣言と型推論 --")
	
	// 通常の宣言
	var name string = "太郎"
	
	// 型推論を使用した宣言
	var age = 30 // int型と推論される
	
	// 短縮宣言（関数内でのみ使用可能）
	shortDecl := "これは短縮宣言です"
	
	fmt.Printf("name: %v, 型: %T\n", name, name)
	fmt.Printf("age: %v, 型: %T\n", age, age)
	fmt.Printf("shortDecl: %v, 型: %T\n", shortDecl, shortDecl)
	
	// 定数
	const Pi = 3.14159265358979323846
	const (
		Monday    = iota // 0
		Tuesday          // 1
		Wednesday        // 2
		Thursday         // 3
		Friday           // 4
	)
	
	fmt.Println("\n定数:")
	fmt.Printf("Pi: %v\n", Pi)
	fmt.Printf("曜日定数: %v, %v, %v\n", Monday, Tuesday, Wednesday)
	
	// -------------------- 複合型 --------------------
	fmt.Println("\n-- 複合型 --")
	
	// 配列（固定長）
	var arr [5]int = [5]int{1, 2, 3, 4, 5}
	var arr2 = [...]int{1, 2, 3} // サイズが自動的に決まる
	
	fmt.Println("配列:")
	fmt.Printf("arr: %v, 長さ: %d\n", arr, len(arr))
	fmt.Printf("arr2: %v, 長さ: %d\n", arr2, len(arr2))
	
	// 配列要素へのアクセス
	arr[0] = 10
	fmt.Printf("arr[0]: %v, arr[1]: %v\n", arr[0], arr[1])
	
	// 多次元配列
	var matrix [2][3]int = [2][3]int{{1, 2, 3}, {4, 5, 6}}
	fmt.Printf("多次元配列: %v\n", matrix)
	
	// スライス（可変長）
	var slice []int = []int{1, 2, 3, 4, 5}
	slice2 := make([]int, 3)      // 長さ3、容量3のスライス
	slice3 := make([]int, 3, 5)   // 長さ3、容量5のスライス
	
	fmt.Println("\nスライス:")
	fmt.Printf("slice: %v, 長さ: %d, 容量: %d\n", slice, len(slice), cap(slice))
	fmt.Printf("slice2: %v, 長さ: %d, 容量: %d\n", slice2, len(slice2), cap(slice2))
	fmt.Printf("slice3: %v, 長さ: %d, 容量: %d\n", slice3, len(slice3), cap(slice3))
	
	// スライスの操作
	slice = append(slice, 6, 7)       // 要素の追加
	fmt.Printf("append後: %v\n", slice)
	
	sliceCopy := make([]int, len(slice))
	copy(sliceCopy, slice)            // スライスのコピー
	fmt.Printf("コピーしたスライス: %v\n", sliceCopy)
	
	subSlice := slice[1:4]            // スライシング（インデックス1から3まで）
	fmt.Printf("サブスライス: %v\n", subSlice)
	
	// マップ（キーと値のペア）
	var m map[string]int = map[string]int{
		"apple":  100,
		"banana": 200,
	}
	m2 := make(map[string]int)
	m2["one"] = 1
	m2["two"] = 2
	
	fmt.Println("\nマップ:")
	fmt.Printf("m: %v\n", m)
	fmt.Printf("m2: %v\n", m2)
	
	// マップの操作
	m["orange"] = 300               // 要素の追加
	fmt.Printf("orange追加後: %v\n", m)
	
	delete(m, "banana")             // 要素の削除
	fmt.Printf("banana削除後: %v\n", m)
	
	value, exists := m["apple"]     // 存在確認と値の取得
	fmt.Printf("apple存在: %v, 値: %v\n", exists, value)
	
	// マップの反復処理
	fmt.Println("マップの反復処理:")
	for key, value := range m {
		fmt.Printf("  %v: %v\n", key, value)
	}
	
	// 構造体
	p1 := Person{
		Name:    "山田太郎",
		Age:     30,
		Married: false,
	}
	
	fmt.Println("\n構造体:")
	fmt.Printf("人物: %+v\n", p1) // +vは構造体のフィールド名も表示する
	fmt.Printf("名前: %v, 年齢: %v\n", p1.Name, p1.Age)
	
	// メソッドの呼び出し
	fmt.Printf("挨拶: %v\n", p1.Greet())
	
	// ポインタレシーバメソッドの呼び出し
	p1.HaveBirthday()
	fmt.Printf("誕生日後の年齢: %v\n", p1.Age)
	
	// インターフェース
	var g Greeter = p1
	fmt.Printf("インターフェース経由の挨拶: %v\n", g.Greet())
	
	// -------------------- ポインタ --------------------
	fmt.Println("\n-- ポインタ --")
	
	x := 10
	var p *int = &x    // xのアドレスを取得
	
	fmt.Printf("x: %v, p: %v, *p: %v\n", x, p, *p)
	
	*p = 20            // ポインタ経由で値を変更
	fmt.Printf("値変更後 x: %v\n", x)
	
	// -------------------- 型変換 --------------------
	fmt.Println("\n-- 型変換 --")
	
	var xInt int = 10
	var xFloat float64 = float64(xInt)
	var xUint uint = uint(xInt)
	
	fmt.Printf("int→float64: %v→%v\n", xInt, xFloat)
	fmt.Printf("int→uint: %v→%v\n", xInt, xUint)
	
	// 文字列変換
	var xStr string = strconv.Itoa(xInt)       // int→string
	xInt2, err := strconv.Atoi(xStr)           // string→int
	
	fmt.Printf("int→string: %v→%v\n", xInt, xStr)
	fmt.Printf("string→int: %v→%v, エラー: %v\n", xStr, xInt2, err)
	
	// -------------------- 日時 --------------------
	fmt.Println("\n-- 日時 --")
	
	now := time.Now()
	fmt.Printf("現在時刻: %v\n", now)
	fmt.Printf("フォーマット: %v\n", now.Format("2006-01-02 15:04:05"))
	
	tomorrow := now.Add(24 * time.Hour)
	fmt.Printf("明日: %v\n", tomorrow)
	
	duration := tomorrow.Sub(now)
	fmt.Printf("差分: %v\n", duration)
	
	// -------------------- リフレクション --------------------
	fmt.Println("\n-- リフレクション --")
	
	typeOf := reflect.TypeOf(p1)
	valueOf := reflect.ValueOf(p1)
	
	fmt.Printf("TypeOf: %v\n", typeOf)
	fmt.Printf("ValueOf: %v\n", valueOf)
	fmt.Printf("フィールド数: %v\n", typeOf.NumField())
	fmt.Printf("最初のフィールド: %v\n", typeOf.Field(0).Name)
	
	// -------------------- 数学関数 --------------------
	fmt.Println("\n-- 数学関数 --")
	
	fmt.Printf("Abs(-10): %v\n", math.Abs(-10))
	fmt.Printf("Sqrt(16): %v\n", math.Sqrt(16))
	fmt.Printf("Max(10, 20): %v\n", math.Max(10, 20))
	fmt.Printf("Sin(Pi/2): %v\n", math.Sin(math.Pi/2))

	fmt.Println("\n================ End of Go Data Types ================")
}