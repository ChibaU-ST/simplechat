# Example 1
## Input
{
  "body": "{\"message\": \"東京都は首都ですか？\"}"
}

## Result
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  },
  "body": "{\"generated_text\": \"**答え:**  はい、東京都は日本の首都です。\"}"
}

# Example 2
## Input
{
  "body": "{\"message\": \"LLMとは何ですか？\"}"
}

## Result
{
  "statusCode": 200,
  "headers": {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*"
  },
  "body": "{\"generated_text\": \"Large Language Model (LLM) は、大量のテキストデータで学習された、人間のような自然言語処理 (NLP) モデルです。\\n\\n**LLM の特徴:**\\n\\n* **自然言語理解:**  LLM は文章の構造や意味を理解し、質問に答える、文章を要約する、翻訳するなど、自然言語処理のタスクを実行できます。\\n* **多様なタスク:**  LLM は、文章生成、コード生成、会話生成など、様々なタスクを実行できます。\\n* **学習データの広さ:**  LLM は、膨大なテキストデータで学習するため、幅広い知識や経験を持つことができます。\\n\\n\\n**LLM の例:**\\n\\n* **ChatGPT:** OpenAI が開発した会話型 LLM\\n* **Bard:** Google が開発した LLM\\n* **LaMDA:** Google が開発した LLM\\n* **BLOOM:**  オープンソースの LLM\\n\\n\\n**LLM の利用シーン:**\\n\\n* **カスタマーサポート:**  自動チャットボットの開発\\n* **コンテンツ生成:**  ブログ記事、記事、詩、小説の生成\\n* **翻訳:**  多言語のテキストの自動翻訳\\n* **コード生成:**  プログラミングコードの自動生成\\n* **質問応答:**  質問に対して、適切な回答を生成\\n* **教育:**  学習教材の生成、質問への回答\\n\\n\\n**LLM の課題:**\\n\\n* **偏見:**  LLM は、学習データに含まれる偏見を反映するため、偏った回答を出力することがあります。\\n* **倫理的な問題:**  LLM の利用に際して、倫理的な問題が提起されています。\\n* **セキュリティ:**  LLM を不正に利用したり、悪用したりする可能性があります。\"}"
}