# Visual Presentation Production

以宿主原生繪圖能力製作完整 16:9 投影片的可攜 Agent Skill，支援 Codex 與 ChatGPT Work。

## 安裝

### Codex

在終端機執行：

```bash
git clone https://github.com/FW1201/visual-presentation-production.git ~/.codex/skills/visual-presentation-production
```

重新開啟 Codex 後，即可要求它使用 `$visual-presentation-production`。

### ChatGPT Work

1. 下載 [visual-presentation-production.zip](https://github.com/FW1201/visual-presentation-production/archive/refs/heads/main.zip)。
2. 開啟 ChatGPT Work，進入「個人頭像 → Skills → New skill → Upload from your computer」。
3. 上傳下載的 ZIP，完成安裝。

> 將 ZIP 直接附在一般對話中，只會成為參考檔案，不會安裝成 Skill。

## 快速開始

安裝後直接提出需求，例如：

```
請使用 visual-presentation-production 製作一份 16:9 簡報。
主題：……
受眾：……
用途：……
```

Skill 會依序處理 brief、頁數確認、逐頁大綱與版面描述、風格鎖定、樣張、逐張生成與 QA，最後輸出單一 PDF。尚未完成必要確認前，不會開始生成。

## 特色

- 支援品牌輸入與可續作的視覺 style profile。
- 對齊用途、受眾、內容來源、內容組織、精確頁數、品牌／參考素材與視覺風格。
- 不使用圖像 API、API key、外部圖像 CLI 或程式繪製投影片。

完整流程請閱讀繁體中文 [使用說明.md](使用說明.md)。
