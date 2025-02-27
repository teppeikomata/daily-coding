fn main(){
    // === 基本型 ===
    // 整数型: 通常はi32（符号付き）かu32（符号なし）を使う
    let integer: i32 = 42;
    println!("{}",integer);
    // 浮動小数点: 通常はf64を使う
    let float: f64 = 3.14;
    println!("{}",float);
    // 真偽値
    let boolean: bool = true;
    println!("{}",boolean);

    // 文字と文字列
    let character_char: char = 'A';
    let string_literal: &str = "こんにちは";// 文字列スライス(借用)
    let mut string: String = String::from("Hello");//所有権のある文字列
    string.push_str(", World!"); // 文字列の変更

    println!("文字: {}", character_char);
    println!("文字列: {}", string_literal);
    println!("文字列: {}",string);

    // ===== 基本的なコレクション =====
    // 配列（固定長、同じ型）
    let array = [1,2,3,4,5];
    println!("3番目:{}",array[2]);

    // ベクタ（可変長配列、同じ型）- 最もよく使うコレクション
    let mut vec = vec![1,2,3]; // マクロでの初期化
    vec.push(4);
    vec.push(5);
    println!("ベクタの長さ: {}",vec.len());

    // ハッシュマップ（キーと値のペア）
    use std::collections::HashMap;
    let mut scores = HashMap::new();
    scores.insert(String::from("青チーム"),10);
    scores.insert(String::from("青チーム"),50);

    // 値の取得（Option型を返す）
    if let Some(score) = scores.get("青チーム"){
        // ない場合はNoneが返却
        println!("青チームのスコア: {}",score);
    }

    match scores.get("黒チーム") {
        Some(score) => {
            println!("青チームのスコア: {}", score);
        }
        None => {
            println!("なんもない");
        } 
    }

    // ===== 所有権と借用（Rustの中核概念） =====
    
    // 所有権の移動
    let s1 = String::from("hello");
    let s2 = s1; // s1からs2へ所有権が移動。s1はもう使えない
    println!("{}", s2); // これはコンパイルエラーになる
    
    // 借用（参照）
    let s3 = String::from("hello");
    let len = calculate_length(&s3); // s3を借用
    println!("文字列 '{}' の長さは {} です", s3, len);
    
    fn calculate_length(s: &String) -> usize { // 参照を受け取る
        s.len()
    } // 借用したものが関数スコープを出ても、s3は使える
    
    // 可変参照
    let mut s4 = String::from("hello");
    change(&mut s4); // 可変参照を渡す
    println!("変更後: {}", s4);
    
    fn change(s: &mut String) {
        s.push_str(", world");
    }
    
    // ===== Option型（null安全性） =====
    
    // nullの代わりにOption型を使用
    fn find_user(id: i32) -> Option<String> {
        if id == 1 {
            Some(String::from("Alice"))
        } else {
            None
        }
    }
    
    // Option型の扱い方
    let user_name = find_user(1);
    match user_name {
        Some(name) => println!("ユーザー名: {}", name),
        None => println!("ユーザーが見つかりません"),
    }
    
    // if let構文（簡潔なパターンマッチング）
    if let Some(name) = find_user(1) {
        println!("見つかったユーザー: {}", name);
    }
}