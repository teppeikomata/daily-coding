/**
 * Node.jsのデータ型と使用例
 * 
 * このファイルは、Node.jsで使用できる様々なデータ型とその操作を示しています。
 * 実行方法: node データ型.js
 */

// ファイル操作用のモジュール（必要に応じて）
const fs = require('fs');
// イベントエミッタを使用する場合
const EventEmitter = require('events');

/**
 * プリミティブ型（基本型）
 */
console.log('\n===== プリミティブ型 =====');

// 数値型 (Number)
const integer = 42;                   // 整数
const float = 3.14;                   // 浮動小数点数
const infinity = Infinity;            // 無限大
const notANumber = NaN;               // Not a Number

console.log('数値型の例:');
console.log(`整数: ${integer}`);
console.log(`浮動小数点数: ${float}`);
console.log(`Infinity: ${infinity}`);
console.log(`NaN: ${notANumber}`);
console.log(`数値の型: ${typeof integer}`);

// BigInt型（非常に大きな整数を扱える - ES2020から）
const bigInteger = 9007199254740991n; // nサフィックスでBigIntリテラル
const anotherBigInt = BigInt("9007199254740992");

console.log('\nBigInt型の例:');
console.log(`BigInt: ${bigInteger}`);
console.log(`BigIntの型: ${typeof bigInteger}`);
console.log(`最大の安全な整数: ${Number.MAX_SAFE_INTEGER}`);
console.log(`BigIntでの演算: ${bigInteger + 1n}`);

// 文字列型 (String)
const singleQuote = 'シングルクォート文字列';
const doubleQuote = "ダブルクォート文字列";
const templateString = `テンプレート文字列: ${integer}を埋め込める`;

console.log('\n文字列型の例:');
console.log(singleQuote);
console.log(doubleQuote);
console.log(templateString);
console.log(`文字列の型: ${typeof singleQuote}`);

// 文字列操作
const str = "Hello, JavaScript!";
console.log(`文字列の長さ: ${str.length}`);
console.log(`大文字変換: ${str.toUpperCase()}`);
console.log(`部分文字列: ${str.substring(0, 5)}`);
console.log(`文字列の分割: ${str.split(', ')}`);
console.log(`文字列の検索: ${str.indexOf('Java')}`);
console.log(`文字列の置換: ${str.replace('JavaScript', 'Node.js')}`);

// 論理型 (Boolean)
const trueValue = true;
const falseValue = false;

console.log('\n論理型の例:');
console.log(`真: ${trueValue}`);
console.log(`偽: ${falseValue}`);
console.log(`論理型の型: ${typeof trueValue}`);

// undefined
let undefinedValue;  // 値を代入していない変数

console.log('\nundefinedの例:');
console.log(`未定義値: ${undefinedValue}`);
console.log(`undefinedの型: ${typeof undefinedValue}`);

// null
const nullValue = null;  // 意図的に「値がない」ことを示す

console.log('\nnullの例:');
console.log(`null値: ${nullValue}`);
console.log(`nullの型: ${typeof nullValue}`); // 注意: "object"と表示される（JavaScriptの仕様）

// Symbol型（ES2015から）- ユニークで不変のプリミティブ値
const symbol1 = Symbol('説明');
const symbol2 = Symbol('説明'); // 同じ説明でも別のシンボル

console.log('\nSymbol型の例:');
console.log(`Symbol: ${String(symbol1)}`);
console.log(`Symbolの型: ${typeof symbol1}`);
console.log(`symbol1 === symbol2: ${symbol1 === symbol2}`); // false

/**
 * オブジェクト型（参照型）
 */
console.log('\n===== オブジェクト型 =====');

// オブジェクト (Object)
const person = {
    name: '山田太郎',
    age: 30,
    greeting: function() {
        return `こんにちは、${this.name}です。`;
    }
};

console.log('オブジェクトの例:');
console.log(person);
console.log(`オブジェクトのプロパティアクセス: ${person.name}`);
console.log(`オブジェクトのメソッド呼び出し: ${person.greeting()}`);
console.log(`オブジェクトの型: ${typeof person}`);

// ES2015以降のオブジェクト操作
const { name, age } = person;  // 分割代入
console.log(`分割代入: ${name}, ${age}`);

const updatedPerson = { ...person, job: 'エンジニア' };  // スプレッド構文
console.log('スプレッド構文でのオブジェクト拡張:');
console.log(updatedPerson);

// Object.keysとObject.valuesとObject.entries
console.log('オブジェクトのプロパティ一覧:');
console.log(Object.keys(person));
console.log('オブジェクトの値一覧:');
console.log(Object.values(person));
console.log('オブジェクトのエントリー一覧:');
console.log(Object.entries(person));

// 配列 (Array)
const array = [1, 2, 3, 4, 5];
const mixedArray = [1, 'string', true, { key: 'value' }, [6, 7]];

console.log('\n配列の例:');
console.log(array);
console.log(`配列の長さ: ${array.length}`);
console.log(`配列の要素アクセス: ${array[2]}`);
console.log(`配列の型: ${typeof array}`); // 注意: "object"と表示される
console.log(`配列かどうかの判定: ${Array.isArray(array)}`);

// 配列操作
console.log('配列操作の例:');
console.log(`末尾に追加: ${array.push(6)} (新しい長さを返す)`);
console.log(`配列: ${array}`);
console.log(`末尾から削除: ${array.pop()} (削除された要素を返す)`);
console.log(`配列: ${array}`);
console.log(`先頭に追加: ${array.unshift(0)} (新しい長さを返す)`);
console.log(`配列: ${array}`);
console.log(`先頭から削除: ${array.shift()} (削除された要素を返す)`);
console.log(`配列: ${array}`);
console.log(`結合: ${array.concat([6, 7, 8])}`);
console.log(`スライス: ${array.slice(1, 3)}`);
console.log(`インデックス検索: ${array.indexOf(3)}`);

// 配列のメソッドチェーン
const names = ['Alice', 'Bob', 'Charlie', 'Dave'];
const filteredAndMapped = names
    .filter(name => name.length > 3)
    .map(name => name.toUpperCase());
console.log(`メソッドチェーン: ${filteredAndMapped}`);

// 関数 (Function)
function regularFunction(a, b) {
    return a + b;
}

const arrowFunction = (a, b) => a + b;

const functionWithDefaultParams = (a, b = 1) => a + b;

console.log('\n関数の例:');
console.log(`通常の関数: ${regularFunction(2, 3)}`);
console.log(`アロー関数: ${arrowFunction(2, 3)}`);
console.log(`デフォルトパラメータ: ${functionWithDefaultParams(2)}`);
console.log(`関数の型: ${typeof regularFunction}`);

// 高階関数（関数を引数や戻り値として扱う関数）
function operation(a, b, func) {
    return func(a, b);
}

console.log(`高階関数: ${operation(5, 3, (a, b) => a * b)}`);

// クロージャ
function createCounter() {
    let count = 0;
    return function() {
        return ++count;
    };
}

const counter = createCounter();
console.log(`クロージャ: ${counter()}`);  // 1
console.log(`クロージャ: ${counter()}`);  // 2

// 即時実行関数式 (IIFE)
const result = (function() {
    const privateVar = 'これは外部からアクセスできません';
    return 'IIFEからの結果';
})();

console.log(`IIFE: ${result}`);

// 日付 (Date)
const now = new Date();
const customDate = new Date(2023, 0, 1); // 2023年1月1日（月は0から始まる）

console.log('\n日付型の例:');
console.log(`現在時刻: ${now}`);
console.log(`カスタム日付: ${customDate}`);
console.log(`年: ${now.getFullYear()}`);
console.log(`月: ${now.getMonth() + 1}`); // 0から始まるので+1
console.log(`日: ${now.getDate()}`);
console.log(`時間: ${now.getHours()}`);
console.log(`分: ${now.getMinutes()}`);
console.log(`秒: ${now.getSeconds()}`);
console.log(`ミリ秒: ${now.getMilliseconds()}`);
console.log(`タイムスタンプ: ${now.getTime()}`);

// 日付の書式変換
console.log(`ISO文字列: ${now.toISOString()}`);
console.log(`ローカル日時文字列: ${now.toLocaleString()}`);
console.log(`ローカル日付文字列: ${now.toLocaleDateString()}`);
console.log(`ローカル時刻文字列: ${now.toLocaleTimeString()}`);

// 正規表現 (RegExp)
const regex1 = /[a-z]+/g;  // リテラル記法
const regex2 = new RegExp('[a-z]+', 'g');  // コンストラクタ記法

const testString = 'Hello123World';
console.log('\n正規表現の例:');
console.log(`マッチ: ${regex1.test(testString)}`);
console.log(`マッチした部分: ${testString.match(regex1)}`);
console.log(`正規表現で置換: ${testString.replace(regex1, 'JS')}`);
console.log(`正規表現の型: ${typeof regex1}`);

// Map（キーと値のペアのコレクション - ES2015から）
const map = new Map();
map.set('key1', 'value1');
map.set('key2', 'value2');
map.set(person, 'オブジェクトをキーとして使用');

console.log('\nMapの例:');
console.log(`Mapのサイズ: ${map.size}`);
console.log(`key1の値: ${map.get('key1')}`);
console.log(`key3は存在するか: ${map.has('key3')}`);
console.log(`personオブジェクトの値: ${map.get(person)}`);

console.log('Mapの反復処理:');
map.forEach((value, key) => {
    console.log(`${key}: ${value}`);
});

// Set（ユニークな値のコレクション - ES2015から）
const set = new Set([1, 2, 3, 3, 4, 5, 5]); // 重複は自動的に削除される

console.log('\nSetの例:');
console.log(`Setのサイズ: ${set.size}`);
console.log(`3は存在するか: ${set.has(3)}`);
console.log(`6は存在するか: ${set.has(6)}`);
set.add(6);
console.log(`要素追加後: ${[...set]}`);
set.delete(1);
console.log(`要素削除後: ${[...set]}`);

// WeakMap・WeakSet（ES2015から）
// キーへの参照が弱参照になっている（ガベージコレクションの対象になる）
console.log('\nWeakMap・WeakSetの例:');
console.log('WeakMapとWeakSetはオブジェクトへの弱参照を保持します');
console.log('これらはガベージコレクションの妨げにならず、列挙できません');

// Promise（非同期処理 - ES2015から）
console.log('\nPromiseの例:');

function asyncOperation() {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            const success = true;
            if (success) {
                resolve('処理成功');
            } else {
                reject(new Error('処理失敗'));
            }
        }, 1000);
    });
}

console.log('Promise処理開始...');
asyncOperation()
    .then(result => console.log(`非同期処理結果: ${result}`))
    .catch(error => console.error(`エラー: ${error.message}`))
    .finally(() => console.log('Promise処理完了'));

// async/await（ES2017から）
console.log('\nasync/awaitの例:');

async function asyncFunction() {
    try {
        console.log('async/await処理開始...');
        // 通常はawaitを使うが、ここでは実行順序を示すためにPromiseをそのまま返す
        return await asyncOperation();
    } catch (error) {
        console.error(`async/awaitエラー: ${error.message}`);
        return null;
    }
}

asyncFunction().then(result => {
    if (result) console.log(`async/await結果: ${result}`);
    console.log('async/await処理完了');
});

// Buffer（Node.js特有の型）
console.log('\nBufferの例（Node.js特有）:');
const buffer = Buffer.from('Hello, Node.js!');
console.log(`Buffer: ${buffer}`);
console.log(`Buffer（16進数）: ${buffer.toString('hex')}`);
console.log(`Buffer（Base64）: ${buffer.toString('base64')}`);
console.log(`Buffer→文字列: ${buffer.toString()}`);
console.log(`Bufferの長さ: ${buffer.length}`);

// Stream（Node.js特有）
console.log('\nStreamの例（Node.js特有）:');
console.log('Streamはデータの流れを表し、大きなデータを扱うのに適しています');
console.log('例: fs.createReadStream(), process.stdin, process.stdout など');

// TypedArray（型付き配列 - ES2015から）
console.log('\n型付き配列の例:');
const int8Array = new Int8Array([1, 2, 3]);
const uint8Array = new Uint8Array(3);
uint8Array[0] = 10;
uint8Array[1] = 20;
uint8Array[2] = 30;

console.log(`Int8Array: ${int8Array}`);
console.log(`Uint8Array: ${uint8Array}`);
console.log(`Uint8Arrayの長さ: ${uint8Array.length}`);
console.log(`Uint8Array[1]: ${uint8Array[1]}`);

// DataView（型付き配列のバッファからデータを読み書きする - ES2015から）
const buffer2 = new ArrayBuffer(16);
const view = new DataView(buffer2);
view.setInt32(0, 42);
view.setFloat64(4, 3.14);

console.log(`DataView getInt32(0): ${view.getInt32(0)}`);
console.log(`DataView getFloat64(4): ${view.getFloat64(4)}`);

/**
 * Node.js特有の例
 */
console.log('\n===== Node.js特有のオブジェクト =====');

// グローバルオブジェクト
console.log('グローバルオブジェクト:');
console.log(`__dirname: ${__dirname}`); // 現在のディレクトリ名
console.log(`__filename: ${__filename}`); // 現在のファイル名

// process（Node.jsプロセス情報）
console.log('\nprocess:');
console.log(`Node.jsのバージョン: ${process.version}`);
console.log(`プラットフォーム: ${process.platform}`);
console.log(`環境変数（PATH）: ${process.env.PATH.substring(0, 50)}...`);

// EventEmitter（イベント処理）
console.log('\nEventEmitter:');
const myEmitter = new EventEmitter();
myEmitter.on('event', (a, b) => {
    console.log(`イベント発生: ${a}, ${b}`);
});
myEmitter.emit('event', 'arg1', 'arg2');

// 型変換の例
console.log('\n===== 型変換の例 =====');

// 文字列への変換
console.log(`数値→文字列: ${String(123)}`);
console.log(`論理値→文字列: ${String(true)}`);
console.log(`オブジェクト→文字列: ${String({name: 'John'})}`);
console.log(`配列→文字列: ${String([1, 2, 3])}`);

// 数値への変換
console.log(`文字列→数値: ${Number('123')}`);
console.log(`論理値→数値: ${Number(true)}`); // true → 1
console.log(`不正な文字列→数値: ${Number('abc')}`); // NaN

// 整数への変換
console.log(`文字列→整数（10進数）: ${parseInt('123')}`);
console.log(`文字列→整数（16進数）: ${parseInt('FF', 16)}`);
console.log(`浮動小数点→整数: ${parseInt('123.45')}`); // 小数点以下は切り捨て

// 論理値への変換
console.log(`数値→論理値: ${Boolean(1)}`); // 0以外は true
console.log(`文字列→論理値: ${Boolean('')}`); // 空文字は false
console.log(`null→論理値: ${Boolean(null)}`); // false
console.log(`undefined→論理値: ${Boolean(undefined)}`); // false
console.log(`NaN→論理値: ${Boolean(NaN)}`); // false

console.log('\n処理が非同期なため、上記のPromiseとasync/awaitの結果は後で表示されます。');