#!/usr/bin/env python3
import os
import re
from datetime import datetime

def create_day_folder(base_path="src"):
    """
    'day-NNNNN_yyyy-mm-dd'形式のフォルダを作成する関数
    
    既存のフォルダを確認して次の連番を割り当て、同じ日付のフォルダが作成されないよう制御する。
    フォルダ名のNNNNNは5桁の0埋め数字（最大99999まで対応）で、GitHubでの表示順を
    正しく保つために使用する。フォルダ作成に成功した場合はREADME.mdも自動生成する。
    
    Args:
        base_path (str): フォルダを作成する基本パス。デフォルトは"src"
    
    Returns:
        str: 作成したフォルダのパス。同日付のフォルダが既に存在する場合はNone
    """
    # 基本パスがなければ作成する
    if not os.path.exists(base_path):
        os.makedirs(base_path)
        print(f"基本パス '{base_path}' を作成しました")
    
    # 今日の日付を取得（YYYY-MM-DD形式）
    today = datetime.now().strftime("%Y-%m-%d")
    
    # 既存のフォルダリストを取得
    existing_folders = os.listdir(base_path)
    
    # 今日の日付のフォルダが既に存在するかチェックするためのフラグ
    today_folder_exists = False
    today_folder = ""
    
    # 最大の日付番号を追跡（次の番号決定のため）
    max_day_num = 0
    
    # フォルダ名のパターンを定義（day-NNNNN_YYYY-MM-DD形式）
    # 0埋めありとなしの両方に対応（既存のフォルダ形式との互換性のため）
    pattern = re.compile(r'day-0*(\d+)_(\d{4}-\d{2}-\d{2})')
    
    # 既存の全フォルダを走査して最大の日数と今日の日付のフォルダをチェック
    for folder in existing_folders:
        match = pattern.match(folder)
        if match:
            # パターンにマッチした場合、日付番号と日付文字列を抽出
            day_num = int(match.group(1))  # 数値部分を整数に変換
            date_str = match.group(2)      # 日付部分
            
            # 最大の日付番号を更新
            if day_num > max_day_num:
                max_day_num = day_num
            
            # 今日の日付のフォルダが存在するかチェック
            if date_str == today:
                today_folder_exists = True
                today_folder = folder
    
    # 同日のフォルダが既に存在する場合は作成をスキップ
    if today_folder_exists:
        print(f"警告: 今日の日付({today})のフォルダ '{today_folder}' は既に存在します")
        return None
    
    # 次の番号を割り当て（最大値 + 1）
    next_day_num = max_day_num + 1
    
    # 新しいフォルダ名（day-NNNNN_YYYY-MM-DD形式）
    # 5桁で0埋め（最大99999日/約273年まで対応）
    new_folder_name = f"day-{next_day_num:05d}_{today}"
    new_folder_path = os.path.join(base_path, new_folder_name)
    
    # フォルダを作成
    os.makedirs(new_folder_path)
    print(f"新しいフォルダ '{new_folder_path}' を作成しました")
    
    # README.mdファイルを作成
    readme_path = os.path.join(new_folder_path, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        # README.mdの内容テンプレート
        f.write(f"# Day {next_day_num} ({today})\n\n")
        f.write("## 今日の内容\n\n- \n\n")
    
    print(f"README.mdファイルを '{readme_path}' に作成しました")
    
    return new_folder_path

if __name__ == "__main__":
    # スクリプトが直接実行された場合の処理
    created_folder = create_day_folder()
    if created_folder:
        print(f"作成成功: {created_folder}")
    else:
        print("フォルダは作成されませんでした")