# Social Browser Publisher for Codex

一個可安裝的 Codex Skill，讓 Codex 使用學員**已登入的 Chrome**，先預覽並核對帳號，再把獲得明確授權的貼文發佈到 Instagram、Facebook 與 Threads。

## 安全原則

- Skill 不要求、不保存帳號密碼、2FA、Cookie、Token 或 Chrome Profile 資料。
- 登入與驗證只能由使用者直接在 Chrome 完成。
- 建議建立獨立的 Chrome Profile：`Codex Social`。
- 預設先預覽；只有明確授權當下那一批內容後，Codex 才能點最後的發佈按鈕。
- 發佈前會從可見畫面核對目前帳號／Facebook 目的地。

## 安裝

需求：Codex 與已啟用的 Chrome browser-control 外掛。

使用 Codex 內建安裝器：

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo jacky391977/social-browser-publisher \
  --path social-browser-publisher
```

安裝後重新啟動 Codex，或開始新的對話。

也可以從 GitHub 下載 ZIP，將其中的 `social-browser-publisher` 資料夾放到：

```text
~/.codex/skills/social-browser-publisher
```

## 第一次設定

對 Codex 說：

```text
使用 $social-browser-publisher 幫我做第一次設定與 doctor，先不要發文。
```

或自行執行：

```bash
python3 ~/.codex/skills/social-browser-publisher/scripts/init_config.py
python3 ~/.codex/skills/social-browser-publisher/scripts/doctor.py
```

設定只會保存非敏感的預期帳號名稱與 Facebook 目的地，位置是：

```text
~/.config/codex-social-publisher/config.json
```

## 建議測試順序

1. 執行 setup 與 doctor。
2. 請 Codex 檢查三個平台是否已登入，但不要發文。
3. 準備測試圖片，要求產生三平台預覽。
4. 執行 dry run，確認停在最後發佈按鈕之前。
5. 使用自己的測試帳號與無敏感內容進行一次真實發佈測試。

範例：

```text
使用 $social-browser-publisher，根據這張圖片分別寫 IG、Facebook、Threads 貼文。
先顯示完整預覽並跑 dry run，絕對不要發布。
```

## 限制

社群網站會改版，瀏覽器流程可能需要跟著更新。這個 Skill 適合一般人工頻率的貼文，不適合大量排程、洗版、互動機器人或繞過平台安全機制。若要高頻、企業級排程，應改用平台官方 API。

## 授權

[MIT License](LICENSE)
