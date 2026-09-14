# Awesome Agent Harness Benchmarks

エージェントの目的に合う評価を選ぶために。スコアの前に、タスク・採点方法・限界を確かめる。

## [検索できる評価カタログを開く →](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)

能力別に絞り込み、原典・実行環境・評価の限界を確認できます。

[English](README.md) · [简体中文](README.zh-CN.md) · 日本語 · [한국어](README.ko.md)

資料の基準日：2026-09-13 · 収録 115 件 · 評価スイート 97 件 · 13 分野

ここでいう **harness** は、モデルの周りでツール呼び出し、コンテキスト、メモリ、権限、実行の制御を担う仕組みです。このカタログでは、それぞれを試すための公開評価を探し、結果から何が言えるのかを確認できます。

## 何を確かめたいですか？

用途に応じた出発点をまとめました。ランキングではありません。全件カタログには、ほかのタスクやバージョン、比較研究も収録しています。

| 確かめたいこと | 最初に見る評価 | 採点方法 | 比較する際の注意点 |
| --- | --- | --- | --- |
| 実際のリポジトリで不具合を修正する | [SWE-bench family](https://github.com/SWE-bench/SWE-bench) | 修正確認テストと回帰テスト | トラックごとにタスク・言語・評価方法が異なり、スコアは直接比較できません。 |
| 複雑なターミナル作業を完了する | [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) | タスクごとの検証プログラム | データセットの版を固定してください。成績にはモデルと harness の両方が影響します。 |
| 状態を保ちながらツールを使う | [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox) | 途中の到達点と最終状態 | ユーザーシミュレータとツールのインターフェースも結果を左右します。 |
| Web サイト上で作業を完了する | [WebArena](https://github.com/web-arena-x/webarena) | Web アプリの機能・状態の検査 | 環境設定、タスク、評価器の修正を含め、バージョンを揃える必要があります。 |
| 複数のデスクトップアプリを操作する | [OSWorld / OSWorld-Verified](https://github.com/xlang-ai/OSWorld) | 実行結果に基づく検査 | 仮想マシンのイメージ、操作回数の上限、評価の版を揃えてください。 |
| 長い会話履歴から情報を取り出す | [LongMemEval](https://github.com/xiaowu0162/LongMemEval) | 履歴に関する質問への正答率 | 履歴全体を与えるベースラインが必要です。質問応答は一連の作業の完了とは異なります。 |
| ツール利用中のプロンプトインジェクションに対処する | [AgentDojo](https://github.com/ethz-spylab/agentdojo) | 通常タスクの成績と攻撃成功率 | 脅威モデルと攻撃の予算を固定し、安全性と実用性を併せて見ます。 |
| ツールを使って情報を集め、推論する | [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) | 最終回答の正答率 | 最終回答だけでは、途中の副作用や実行の安全性はわかりません。 |

## スコアからわかること

多くの評価が測るのは、エージェント全体の性能です。harness による差を調べるには、同じモデル・タスク・予算で条件を揃えて比較する必要があります。収録したすべてのプロジェクトが、その実験を行っているわけではありません。

- **benchmark**：タスクと評価器を備えた、テストを実行するためのスイート。
- **study**：比較研究。実験設計や、すでに得られた根拠を確認するための資料。
- **infrastructure**：評価の実行や監査を支えるツール。タスク集そのものではありません。
- **watchlist**：公開初期、または対象が限定的な候補。追加の確認が必要です。

比較テンプレートや評価の提案は実験設計のためのもので、実測結果やランキングではありません。

## 分野から探す

説明と原典を含む[全件カタログ](docs/catalog.md)も用意しています。各分野へ直接進めます：

[Harness の直接比較](docs/catalog.md#direct) · [コード・ターミナル](docs/catalog.md#coding) · [ツール・状態管理](docs/catalog.md#tools)

[ブラウザ](docs/catalog.md#browser) · [デスクトップ・モバイル](docs/catalog.md#computer) · [汎用タスク](docs/catalog.md#general)

[メモリ・コンテキスト](docs/catalog.md#memory) · [長時間のタスク](docs/catalog.md#long-horizon) · [安全性](docs/catalog.md#safety)

[複数エージェントの協調](docs/catalog.md#multi-agent) · [研究タスク](docs/catalog.md#research) · [スキル・指示](docs/catalog.md#skills) · [評価基盤](docs/catalog.md#infrastructure)

## 自分で比較するには

[比較記録テンプレート](docs/comparison-template.md)を使い、実験条件と結果をまとめて残してください：

1. モデル、プロンプト、ツールの仕様、タスクの版、環境、予算、再試行方針を固定する。
2. 完了率、ばらつき、費用、所要時間、安全性の問題を分けて報告し、実行履歴と検証結果を保存する。
3. [調査ノート](docs/research.md)で根拠の強さと比較条件を確認してから、差を解釈する。

## エージェントから利用する

自動で検索・整理する場合は、次の入口を利用できます：

- [説明付き Markdown カタログ](site/agent.md)
- [構造化データ](data/catalog.json)
- [フィールド定義](data/catalog.schema.json)
- [リポジトリの保守ルール](AGENTS.md)

## 出典と改善への参加

公式リポジトリ、論文、プロジェクトページを優先しています。[出典の確認記録](data/source-audit.json)は、ある時点のアクセス可否とメタデータを記録したもので、独立した追試ではありません。掲載は推奨を意味せず、公開・非公開の全評価を網羅するものでもありません。

掲載漏れ、リンク切れ、説明の誤りを見つけたら、[コントリビューションガイド](CONTRIBUTING.md)に沿って issue や PR をお寄せください。原典と、評価の具体的な限界も添えていただけると助かります。評価方法やベンチマーク比較の相談は、[ディスカッション](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)へどうぞ。
