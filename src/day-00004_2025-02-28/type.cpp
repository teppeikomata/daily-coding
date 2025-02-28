#include <iostream>  // 標準入出力
#include <string>    // 文字列
#include <vector>    // 可変長配列
#include <map>       // 連想配列
#include <set>       // 集合
#include <array>     // 固定長配列
#include <tuple>     // タプル
#include <memory>    // スマートポインタ

int main() {
    // ==================== 基本データ型 ====================
    
    // 整数型
    int intValue = 42;                      // 通常の整数型 (大体 4 バイト)
    short shortValue = 123;                 // 短い整数型 (大体 2 バイト)
    long longValue = 123456789L;            // 長い整数型 (最低でも 4 バイト)
    long long longLongValue = 123456789LL;  // より長い整数型 (最低でも 8 バイト)
    
    // 符号なし整数型（非負整数のみ）
    unsigned int uintValue = 42;
    unsigned short ushortValue = 123;
    size_t sizeValue = 100;                 // サイズや長さを表すのによく使う
    
    // 浮動小数点型
    float floatValue = 3.14f;               // 単精度浮動小数点 (約7桁の精度)
    double doubleValue = 3.14159265359;     // 倍精度浮動小数点 (約15桁の精度)
    long double ldoubleValue = 3.14159265359L; // 拡張倍精度
    
    // 文字型
    char charValue = 'A';                   // 1文字（1バイト ASCII文字）
    wchar_t wideChar = L'あ';               // ワイド文字（複数バイト Unicode文字）
    char16_t char16Value = u'あ';           // 16ビットUnicode文字
    char32_t char32Value = U'😊';           // 32ビットUnicode文字
    
    // 論理型
    bool boolValue = true;                  // true または false
    
    // 型の大きさ（バイト数）を確認
    std::cout << "整数型のサイズ:\n";
    std::cout << "int: " << sizeof(int) << " バイト\n";
    std::cout << "short: " << sizeof(short) << " バイト\n";
    std::cout << "long: " << sizeof(long) << " バイト\n";
    std::cout << "long long: " << sizeof(long long) << " バイト\n\n";
    
    // ==================== 文字列 ====================
    
    // C形式の文字列 (char配列)
    char cStyleString[] = "Hello";          // NULL終端文字列
    
    // C++形式の文字列 (std::string)
    std::string message = "Hello, C++!";    // 標準的な文字列
    std::wstring wideMessage = L"ワイド文字列"; // ワイド文字列
    
    // 文字列の操作
    std::string firstName = "John";
    std::string lastName = "Doe";
    std::string fullName = firstName + " " + lastName;  // 連結
    
    // 部分文字列の取得
    std::string substring = fullName.substr(0, 4);  // "John"
    
    // 文字列の長さ
    size_t length = fullName.length();      // 8 ("John Doe"の長さ)
    
    // 文字列の検索
    size_t pos = fullName.find("Doe");      // 5 (位置は0から始まる)
    
    std::cout << "文字列操作例:\n";
    std::cout << "連結結果: " << fullName << "\n";
    std::cout << "部分文字列: " << substring << "\n";
    std::cout << "長さ: " << length << "\n";
    std::cout << "検索位置: " << pos << "\n\n";
    
    // ==================== 配列 ====================
    
    // 固定長配列
    int numbers[5] = {1, 2, 3, 4, 5};       // 従来の配列
    std::array<int, 5> modernArray = {1, 2, 3, 4, 5}; // C++11の固定長配列
    
    // 可変長配列 (vector)
    std::vector<int> dynamicArray = {10, 20, 30}; // 初期値を設定
    dynamicArray.push_back(40);             // 末尾に追加
    dynamicArray.push_back(50);
    
    // vectorへのアクセス
    std::cout << "ベクトル操作例:\n";
    std::cout << "要素数: " << dynamicArray.size() << "\n";
    std::cout << "最初の要素: " << dynamicArray[0] << "\n";
    std::cout << "最後の要素: " << dynamicArray.back() << "\n";
    std::cout << "すべての要素: ";
    for (int num : dynamicArray) {          // 範囲ベースforループ
        std::cout << num << " ";
    }
    std::cout << "\n\n";
    
    // ==================== 連想配列 (map, unordered_map) ====================
    
    // mapはキーでソートされる
    std::map<std::string, int> scores;
    scores["Alice"] = 95;
    scores["Bob"] = 87;
    scores["Charlie"] = 92;
    
    // mapへのアクセス
    std::cout << "マップ操作例:\n";
    std::cout << "Aliceのスコア: " << scores["Alice"] << "\n";
    
    // キーと値のペアを反復処理
    std::cout << "すべてのスコア:\n";
    for (const auto& [name, score] : scores) {  // C++17の構造化束縛
        std::cout << name << ": " << score << "\n";
    }
    std::cout << "\n";
    
    // ==================== 集合 (set, unordered_set) ====================
    
    // setは重複を許さず、ソートされる
    std::set<int> uniqueNumbers = {3, 1, 4, 1, 5, 9, 2, 6, 5};
    
    std::cout << "セット操作例:\n";
    std::cout << "セットの要素: ";
    for (int num : uniqueNumbers) {
        std::cout << num << " ";  // 自動的にソートされ、重複は除去される
    }
    std::cout << "\n\n";
    
    // ==================== タプル ====================
    
    // 異なる型の値をグループ化
    std::tuple<std::string, int, double> person("Alice", 30, 1.75);
    
    // タプルの要素へのアクセス
    std::string name = std::get<0>(person);
    int age = std::get<1>(person);
    double height = std::get<2>(person);
    
    std::cout << "タプル操作例:\n";
    std::cout << "名前: " << name << "\n";
    std::cout << "年齢: " << age << "\n";
    std::cout << "身長: " << height << "m\n\n";
    
    // C++17の構造化束縛を使用
    auto [personName, personAge, personHeight] = person;
    
    // ==================== ポインタ ====================
    
    // 生ポインタ
    int* rawPointer = new int(42);          // メモリ確保
    std::cout << "ポインタ操作例:\n";
    std::cout << "ポインタの値: " << *rawPointer << "\n";
    delete rawPointer;                       // メモリ解放（忘れないこと！）
    
    // スマートポインタ
    std::unique_ptr<int> uniquePtr = std::make_unique<int>(100);  // C++14
    std::shared_ptr<int> sharedPtr = std::make_shared<int>(200);
    
    // 共有ポインタを複数の変数で共有
    std::shared_ptr<int> sharedPtr2 = sharedPtr;  // 参照カウントが2になる
    
    std::cout << "スマートポインタの値: " << *uniquePtr << "\n";
    std::cout << "共有ポインタの値: " << *sharedPtr << "\n";
    std::cout << "参照カウント: " << sharedPtr.use_count() << "\n\n";  // 2を表示
    
    // ==================== 列挙型 ====================
    
    // 古典的な列挙型
    enum Color { RED, GREEN, BLUE };
    Color color = BLUE;
    
    // スコープ付き列挙型 (C++11)
    enum class Fruit { APPLE, BANANA, ORANGE };
    Fruit fruit = Fruit::BANANA;
    
    std::cout << "列挙型操作例:\n";
    std::cout << "カラーの値: " << static_cast<int>(color) << "\n";  // 2
    std::cout << "フルーツの値: " << static_cast<int>(fruit) << "\n\n";  // 1
    
    // ==================== 構造体と共用体 ====================
    
    // 構造体
    struct Person {
        std::string name;
        int age;
        double height;
    };
    
    Person p1 = {"Bob", 25, 1.80};
    
    // 共用体（全てのメンバーが同じメモリ領域を共有）
    union Value {
        int intValue;
        float floatValue;
        char charValue;
    };
    
    Value v;
    v.intValue = 42;
    std::cout << "共用体操作例:\n";
    std::cout << "整数値: " << v.intValue << "\n";
    
    v.floatValue = 3.14f;  // intValueを上書き
    std::cout << "浮動小数点値: " << v.floatValue << "\n";
    return 0;
}