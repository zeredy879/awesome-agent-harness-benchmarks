# Awesome Agent Harness Benchmarks

AI エージェントで試したい作業に合うベンチマークを選び、評価内容・採点方法・限界を確認できます。

**[ベンチマークを検索する →](https://zeredy879.github.io/awesome-agent-harness-benchmarks/)**

[English](README.md) · [简体中文](README.zh-CN.md) · 日本語 · [한국어](README.ko.md)

公開ベンチマークや関連資料を 115 件、13 分野にわたって収録しています。

## 試したい作業から選ぶ

| 試したいこと | まず見るベンチマーク |
| --- | --- |
| コードの不具合を修正する | [SWE-bench](https://github.com/SWE-bench/SWE-bench) |
| ターミナルで作業を完了する | [Terminal-Bench](https://github.com/harbor-framework/terminal-bench) |
| 状態を管理しながらツールを使う | [ToolSandbox](https://github.com/apple-aiml-research/ToolSandbox) |
| Web サイト上で作業する | [WebArena](https://github.com/web-arena-x/webarena) |
| デスクトップアプリを使う | [OSWorld](https://github.com/xlang-ai/OSWorld) |
| 過去の会話を覚えて情報を取り出す | [LongMemEval](https://github.com/xiaowu0162/LongMemEval) |
| ツール出力からのプロンプトインジェクションを防ぐ | [AgentDojo](https://github.com/ethz-spylab/agentdojo) |
| 情報を調べ、ツールを使って問題を解く | [GAIA](https://huggingface.co/datasets/gaia-benchmark/GAIA) |

ほかの候補は[全件カタログ](docs/catalog.md)にまとめています。各項目で採点方法、実行環境、評価の限界を確認できます。

## Harness を比較する

**Agent harness** は、モデルのツール利用、会話の文脈や記憶、権限、エラーからの復旧を管理するソフトウェアです。これらを調べるには、次のプロジェクトが参考になります。

- [Harness-Bench](https://github.com/Qihoo360/harness-bench)：モデルと harness の組み合わせを、ローカルの作業環境で比較します。
- [ShellBench](https://github.com/openclaw/shellbench)：旧 ClawBench。実行記録と繰り返しの試行から、エージェント全体の信頼性を評価します。
- [SkillsBench](https://github.com/benchflow-ai/skillsbench)：スキルパッケージの有無で、タスクの成績がどう変わるかを調べます。

## データと比較方法

多くのベンチマークが測るのは、エージェント全体の性能です。harness を比較する際は、何を変えるかを先に決めます。構成全体の比較なら、各構成のプロンプト、ツール、標準設定を含めて比較できます。一つの機能の効果を調べるなら、その機能だけを変えます。モデル、タスク、環境、予算、採点基準など、比較対象に含めない条件は揃えます。

完了率、繰り返したときの安定性、費用、所要時間、安全性を分けて記録し、実行履歴と検証結果を残します。[比較記録テンプレート](docs/comparison-template.md)と[調査・方法論ノート](docs/research.md)を利用できます。

エージェント向け：[Markdown 要約](site/agent.md) · [JSON データ](data/catalog.json) · [フィールド定義](data/catalog.schema.json) · [保守ルール](AGENTS.md)

出典にアクセスできるかを毎週確認しています。掲載は独立した追試を意味しません。詳しくは[データと出典について](data/README.md)をご覧ください。

## 改善に参加する

掲載漏れ、説明の誤り、リンク切れは、[貢献ガイド](CONTRIBUTING.md)に沿って issue や PR でお知らせください。原典へのリンクと短い説明があれば十分です。評価方法や比較の相談には[ディスカッション](https://github.com/zeredy879/awesome-agent-harness-benchmarks/discussions)をご利用ください。
