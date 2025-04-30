import json
import os
import urllib.request
import urllib.error
import traceback

# Colab 側の FastAPI URL を Lambda の環境変数として設定（例: https://8a42-35-240-137-135.ngrok-free.app）
API_URL = os.environ.get("LLM_API_URL")
ENDPOINT = "/generate"

def lambda_handler(event, context):
    try:
        # リクエストのメッセージを取得
        body = json.loads(event.get("body") or "{}")
        message = body.get("message")
        if not message:
            return _response(400, {"error": "message is required"})

        # Colab API に送るリクエストペイロード
        payload = json.dumps({
            "prompt": message,
            "max_new_tokens": 512,
            "temperature": 0.7,
            "top_p": 0.9,
            "do_sample": True
        }).encode("utf-8")

        # API にリクエスト送信
        req = urllib.request.Request(
            url=f"{API_URL}{ENDPOINT}",
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST"
        )

        with urllib.request.urlopen(req, timeout=60) as res:
            res_body = json.load(res)

        return _response(200, {"generated_text": res_body.get("generated_text", "No response")})

    except urllib.error.URLError as e:
        return _response(502, {"error": f"API unreachable: {e}"})
    except Exception as e:
        traceback.print_exc()
        return _response(500, {"error": str(e)})

# レスポンスフォーマット統一
def _response(status_code, body_dict):
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "*"
        },
        "body": json.dumps(body_dict, ensure_ascii=False)
    }
