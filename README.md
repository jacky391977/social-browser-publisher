# Social Browser Publisher for Codex

一個可安裝的整合型 Codex Skill，包含：

- 學習**每位使用者自己的語氣**
- 搜尋近期熱門內容，附來源日期、連結、可信度與限制
- 14 天內容規劃與成效回顧
- 分別產生 Instagram、Facebook、Threads 原生文案
- 依平台加入自然分行分段，發佈前比對空行是否一致
- 製作與預覽 IG／FB 圖片小卡
- 使用學員已登入的 Chrome 安全發佈

這個最終版已整合舊 `social-post` 的泛用語氣學習與內容策略概念，但**不包含任何人的私人 `style_profile.md`、固定作者語氣、帳號資料或實戰數據**。每位學員安裝後都要用自己的貼文建立獨立語氣設定檔。

## 學員使用手冊

- [GitHub 完整繁體中文手冊](social-browser-publisher/USER_GUIDE.zh-TW.md)
- [Notion 線上閱讀版](https://app.notion.com/p/3cf4e6997823811b9fe8ce35b7b9989c?pvs=204)

手冊包含完整功能說明、安全與隱私設計、安裝設定、個人語氣訓練、熱門內容搜尋、三平台文案、圖片小卡、dry run、正式發佈與常見問題排除。

## 安全原則

- 不要求或保存帳號密碼、2FA、Cookie、Token 或 Chrome Profile 資料。
- 登入與驗證只能由使用者直接在 Chrome 完成。
- 使用者語氣／品牌／內容計畫保存在 `~/.config/codex-social-publisher/profiles/<profile-id>/`，不會寫入 Skill 或 GitHub。
- 每個人或品牌使用不同 `profile-id`，禁止跨使用者借用語氣。
- 預設先預覽；只有明確授權當下那一批內容後才發佈。
- 發佈前會核對可見帳號，並關閉沒有授權的跨發平台。

## 安裝

需求：Codex、Google Chrome，以及在 **Settings → Computer use** 啟用的 ChatGPT Chrome 擴充功能。

將下面整段文字直接貼到 Codex，不需要自行開啟終端機：

```text
幫我安裝這個 skill，安裝好後教我怎麼設定
https://github.com/jacky391977/social-browser-publisher/releases/latest
```

安裝後依 Codex 畫面提示重新啟動或開啟新對話。學員只需要安裝這一個 Skill，不需要再另外安裝舊 `social-post`。

## 第一次設定

### 1. 開啟 Chrome 本機檔案權限

若要上傳圖片或影片到 Instagram／Facebook：

1. 在 Chrome 開啟 `chrome://extensions/`。
2. 找到 ChatGPT 擴充功能，點「詳細資料」。
3. 開啟「允許存取檔案網址」（Allow access to file URLs）。
4. 關掉權限開啟前已存在的 IG／FB 建立貼文視窗或檔案選擇視窗。
5. 回到 Codex，重新開始一次全新的 Chrome 發佈任務。

不要沿用開權限前的舊 composer。官方說明：[Chrome extension file uploads](https://developers.openai.com/codex/app/chrome-extension#upload-files)。

### 2. 建立安全設定與獨立使用者檔案

將下面整段文字貼到 Codex，讓 Codex 直接完成可執行的設定：

```text
請使用 $social-browser-publisher 幫我完成第一次安全設定。
請建立我的私人 profile、引導我填寫 Instagram、Facebook、Threads 的顯示帳號或發佈目的地，並執行 Doctor 安全檢查。
能由你執行的設定請直接幫我完成，不要叫我開終端機。
不要要求我提供密碼、驗證碼、Cookie 或 Token。
```

多位使用者或多品牌請使用不同代號，例如可直接對 Codex 說：

```text
請使用 $social-browser-publisher 幫我新增一個 fruit-store profile，保留現有平台目的地設定，完成後切換到 fruit-store 並執行 Doctor。
```

切換 profile 不會清掉 IG、FB、Threads 目的地設定。實際發文前仍會從 Chrome 可見畫面再次核對帳號。

若從舊版升級，直接請 Codex「重新檢查目前 profile 並補齊缺少的私人設定檔」。現有語氣、品牌與內容計畫不會被覆寫。

### 3. 用自己的貼文學語氣

```text
使用 $social-browser-publisher，作用中的 profile-id 是 fruit-store。
請只分析我接下來提供的貼文，建立我的語氣設定檔；先給我三點分析和一篇測試草稿，不要發文。
```

也可以明確提供自己的 FB／IG／Threads 頁面並授權 Codex 從已登入 Chrome 讀取。Skill 不會猜網址，也不會把內建範例當成你的語氣。

## 使用範例

搜尋近期熱門內容：

```text
使用 $social-browser-publisher，搜尋最近 7 天水果相關的熱門討論，列出 5 個候選主題、來源日期與連結、可信度和限制。先讓我選角度，不要發布。
```

熱門搜尋必須使用即時資料，不以模型記憶冒充「近期熱門」。預設提供五個可檢查候選，分成 A／B／C 可信度；若無法直接看到平台證據，會明確標為網路／新聞熱度。Skill 只提取事實與討論張力，不抄寫或近似改寫其他創作者文案。

產生三平台草稿：

```text
使用 $social-browser-publisher，以 fruit-store 的語氣，根據這個主題分別寫 IG、Facebook、Threads 版本。先完整預覽，不要發布。
```

草稿會依平台使用自然段落：Instagram 通常分開開場、正文、CTA 與標籤；Facebook 在敘事或觀點轉折處換段；較長 Threads 內容分成 2–4 個閱讀節奏。發佈前會從 composer 重新讀回文字，逐字核對內容與空行。

製作 IG 圖片小卡：

```text
使用 $social-browser-publisher，把這篇內容做成 1080×1350 的 4:5 IG 小卡，先讓我看圖片與文案，不要發布。
```

安全測試：

```text
使用 $social-browser-publisher 跑 IG dry run。核對帳號、4:5 裁切與跨發開關，停在最後「分享」按鈕前。
```

## 已修正的 IG 發佈陷阱

- 開啟檔案權限後一定重新開 composer，不沿用舊視窗。
- `setFiles` 後等待「裁切／下一步」狀態，不因畫面短暫沒更新就重複上傳。
- 1080×1350 圖卡明確選 4:5，目視確認文字與 footer 沒被切掉。
- 預設保留原始色彩，不自動加濾鏡。
- Instagram 可能預設開啟 Facebook 跨發；未授權時選「不要分享此貼文」，不能誤選全域設定。
- 文案以包含 `\n` 的完整文字一次輸入，發佈前核對段落與空行，避免用 Enter 操作到錯誤 UI。
- 分享後需看到成功訊息，再到個人頁核對圖片、文案與公開連結。

## 舊 `social-post` 使用者

最終版已整合它的泛用能力。為保護個資，不會自動複製舊版 `style_profile.md`。請先用 `$social-browser-publisher` 明確測試新版；確認符合需求後，再自行決定是否移除舊 Skill，避免兩個 Skill 同時回應「發文」指令。

## 限制

社群網站會改版，因此發佈時以目前可見 UI 為準。這個 Skill 適合一般人工頻率的內容工作，不適合大量排程、洗版、互動機器人、未經請求的訊息或繞過平台安全機制。

## 授權與來源

[MIT License](social-browser-publisher/LICENSE)。第三方來源標註見 `social-browser-publisher/NOTICE.md`。
