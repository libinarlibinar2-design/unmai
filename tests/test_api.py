<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>UNMAI</title>
    <link rel="stylesheet" href="/static/styles.css" />
  </head>
  <body>
    <div class="container">
      <header class="hero">
        <h1>UNMAI</h1>
        <p>
          Evidence-based claim verification for text and images. Check whether
          a story or message is likely true, misleading, or unverified before
          sharing it.
        </p>
      </header>

      <main class="layout">
        <section class="panel">
          <form id="verifyForm">
            <div>
              <label for="regionSelect">Verification region</label>
              <select id="regionSelect">
                <option value="global">Global</option>
                <option value="india">India</option>
                <option value="us">United States</option>
                <option value="other">Other region</option>
              </select>
            </div>

            <div style="margin-top: 20px;">
              <label for="claimInput">Claim, message, or article text</label>
              <textarea id="claimInput" placeholder="Paste a headline, forwarded message, article excerpt, or a claim you want to verify."></textarea>
            </div>

            <div style="margin-top: 20px;">
              <label for="imageInput">Upload an image or screenshot</label>
              <input id="imageInput" type="file" accept="image/png,image/jpeg,image/webp" />
            </div>

            <div class="actions">
              <button class="primary" type="submit">Verify</button>
              <button class="secondary" type="button" id="copyBtn">Copy summary</button>
            </div>
          </form>

          <div class="sample-title">Try a sample claim</div>
          <div id="sampleList" class="sample-list"></div>
        </section>

        <aside class="right-column">
          <section class="panel result-card" id="resultPanel">
            <div class="badge" id="statusBadge">Unverified</div>

            <div class="meta-block">
              <div class="meta-box">
                <span>Confidence</span>
                <strong id="confidenceValue">0%</strong>
              </div>
              <div class="meta-box">
                <span>Verdict</span>
                <strong id="resultStatus">Pending</strong>
              </div>
            </div>

            <h2>Original claim</h2>
            <p id="claimSummary">No claim submitted yet.</p>

            <h3>AI-assisted explanation</h3>
            <p id="explanationText">The app will explain the evidence and confidence here.</p>

            <h3>Supporting evidence</h3>
            <ul id="evidenceList" class="evidence-list"></ul>

            <h3>Reference links</h3>
            <ul id="sourcesList" class="source-list"></ul>

            <h3>Warnings</h3>
            <ul id="warningsList" class="warning-list"></ul>

            <div class="actions" style="margin-top: 24px;">
              <button class="secondary" type="button" id="shareBtn">Share result</button>
            </div>
          </section>
        </aside>
      </main>
    </div>

    <script src="/static/app.js"></script>
  </body>
</html>
