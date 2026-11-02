# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：
- 自分で学習を実行したか（`executed_training_myself`）：はい　）
- 学習前：`format_rate` =　0.09523809523809523, / `content_rate` =　0.0
- 学習後：`format_rate` =　1.000000 / `content_rate` =　0.904762
- 退行した質問：次回の講義のテーマは何ですか
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：新しい質問の学習については課題が残ることがわかった。
- 学習で変わったこと・変わらなかったこと：演習の実装はしたものの質問の内容変更とその変化を自分で作成するまではできなかった。

## 宿題

- 取り組んだレベル：基礎 /
- 変えた設定やデータ：エポック数を10に
- 結果（比較表や数字）：
Step	Training Loss
10	1.563616
20	0.101026
学習時間: 122 秒 | ステップ数: 20 | エポック: 10.0

	n	format_rate	content_rate	both_rate	seconds
label					
before	21	0.095238	0.000000	0.000000	52.3
before_4bit	21	0.666667	0.333333	0.333333	46.2

質問	正解の needs_review	4bit・学習前の出力	形式/内容	形式の失敗理由
0	提出の期限は？	False	{"answer": "9 月 30 日 23:59（日本時間）", "needs_review": false}	○/○	
1	提出期限の日付と時刻を教えてください	False	{"answer": "9 月 30 日 23:59", "needs_review": false}	○/○	
2	課題の締切は何月何日の何時ですか	False	{"answer": "9 月 30 日 23:59", "needs_review": false}	○/○	
3	提出場所は？	False	{"answer": "学習ポータルの「課題」欄", "needs_review": false}	○/○	
4	課題の提出はどこで行いますか	False	{"answer": "学習ポータルの「課題」欄で提出先を指定し、提出形式は PDF 1 ファイル（学籍番号_課題番号.pdf）で、提出時間は毎週火曜 17:00〜18:00 のオフィスアワーで受け付けます。"}	×/×	missing_key
5	提出物を出す先を教えてください	False	{"answer": "学習ポータルの「課題」欄で提出先を指定してください。提出形式は PDF 1 ファイルで、ファイル名は 学籍番号_課題番号.pdf です。提出後、期限から 48 時間以内なら減点のうえ受け付けます。"}	×/×	missing_key
6	PDF 以外でも出せますか	False	{"answer": "確認が必要"}	×/×	missing_key
7	提出するファイルの形式は何ですか	False	{"answer": "PDF 1 ファイルで、ファイル名は 学籍番号_課題番号.pdf です"}	×/×	missing_key
8	提出ファイルは何形式で、いくつ出しますか	False	{"answer": "PDF 1 ファイルで、1 出します", "needs_review": false}	○/○	
9	相談できる時間帯は？	False	{"answer": "17:00〜18:00", "needs_review": false}	○/×	
10	オフィスアワーの曜日と時間を教えてください	False	{"answer": "火曜 17:00〜18:00", "needs_review": false}	○/○	
11	質問を受け付けてもらえるのは何曜日の何時からですか	False	{"answer": "火曜 17:00〜18:00", "needs_review": false}	○/○	
12	締切後の扱いを教えてください	False	{"answer": "確認が必要", "needs_review": true}	○/×	
13	提出が締切に間に合わなかったらどうなりますか	False	{"answer": "提出が締切に間に合わなかったら、期限から 48 時間以内なら減点のうえ受け付けます。"}	×/×	missing_key
14	期限後に提出した課題は受理されますか	False	{"answer": "確認が必要", "needs_review": true}	○/×	
15	成績はいつ出ますか	True	{"answer": "確認が必要"}	×/×	missing_key
16	講義の録画は公開されますか	True	{"answer": "なし", "needs_review": false}	○/×	
17	課題の文字数に制限はありますか	True	{"answer": "なし", "needs_review": "false"}	×/×	wrong_type
18	提出した課題へのフィードバックはもらえますか	True	{"answer": "はい", "needs_review": false}	○/×	
19	参考文献の書き方に指定はありますか	True	{"answer": "なし", "needs_review": false}	○/×	
20	オフィスアワーは事前予約が必要ですか	True	{"answer": "はい", "needs_review": false}	○/×	

- ファインチューニングが向く場面・向かない場面についての考察：どの部分の修正をくわえるか、自分で設定する必要がある。AIがなんでもできる時代だからこそ自分の納得感がある仕事が大事な時代だなと思った。
