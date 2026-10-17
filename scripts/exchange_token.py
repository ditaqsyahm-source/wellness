import sys
import urllib.parse
import urllib.request
import json
import os

env_path = "social-fleet-assets/dita/DITA-03_dita_gentle_wellness/.env"

def main():
    if len(sys.argv) < 2:
        print("Usage: python exchange_token.py <code_or_url>")
        sys.exit(1)

    raw_input = sys.argv[1].strip()
    code = raw_input
    if "code=" in raw_input:
        parsed = urllib.parse.urlparse(raw_input)
        params = urllib.parse.parse_qs(parsed.query)
        code = params.get("code", [raw_input])[0]

    with open(env_path, "r", encoding="utf-8") as f:
        env = dict(l.strip().split("=", 1) for l in f if "=" in l and not l.strip().startswith("#"))

    client_id = env["GOOGLE_CLIENT_ID"]
    client_secret = env["GOOGLE_CLIENT_SECRET"]
    redirect_uri = "http://localhost"

    data = urllib.parse.urlencode({
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code"
    }).encode("utf-8")

    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=data, headers={
        "Content-Type": "application/x-www-form-urlencoded"
    })

    try:
        with urllib.request.urlopen(req) as resp:
            token_json = json.loads(resp.read().decode())
            refresh_token = token_json.get("refresh_token")
            if not refresh_token:
                print(f"[ERROR] Gagal mendapatkan refresh token: {token_json}")
                sys.exit(1)
            
            # Save to .env
            lines = []
            found = False
            with open(env_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("YT_REFRESH_TOKEN="):
                        lines.append(f"YT_REFRESH_TOKEN={refresh_token}\n")
                        found = True
                    else:
                        lines.append(line)
            if not found:
                lines.append(f"YT_REFRESH_TOKEN={refresh_token}\n")
            with open(env_path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            
            print(f"[SUCCESS] YT_REFRESH_TOKEN berhasil disimpan ke {env_path}")
            print(f"Access Token: {token_json.get('access_token')[:25]}...")
    except urllib.error.HTTPError as e:
        print(f"[HTTP ERROR {e.code}]: {e.read().decode()}")
        sys.exit(1)
    except Exception as e:
        print(f"[ERROR]: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
