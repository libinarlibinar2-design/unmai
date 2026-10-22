body {
  margin: 0;
  font-family: Inter, Arial, sans-serif;
  background: #f4f7fb;
  color: #0f172a;
}

* {
  box-sizing: border-box;
}

.container {
  max-width: 1100px;
  margin: 0 auto;
  padding: 24px 20px 60px;
}

header.hero {
  background: linear-gradient(135deg, #0f172a, #1d4ed8);
  color: white;
  border-radius: 22px;
  padding: 40px 30px;
  box-shadow: 0 18px 40px rgba(37, 99, 235, 0.2);
}

.hero h1 {
  margin: 0 0 12px;
  font-size: clamp(2rem, 4vw, 3.2rem);
}

.hero p {
  margin: 0;
  max-width: 760px;
  color: #dbeafe;
  line-height: 1.6;
}

.layout {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 26px;
  margin-top: 24px;
}

.panel {
  background: white;
  border: 1px solid #e2e8f0;
  border-radius: 20px;
  padding: 24px;
  box-shadow: 0 10px 30px rgba(15, 23, 42, 0.04);
}

label {
  display: block;
  margin-bottom: 8px;
  font-weight: 600;
}

textarea,
select,
input[type="file"] {
  width: 100%;
  padding: 14px 16px;
  border-radius: 12px;
  border: 1px solid #cbd5e1;
  font-size: 1rem;
  background: #f8fafc;
}

textarea {
  resize: vertical;
  min-height: 170px;
}

.actions {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-top: 20px;
}

button {
  border: none;
  border-radius: 12px;
  padding: 12px 18px;
  font-weight: 600;
  cursor: pointer;
  transition: 0.2s ease;
}

.primary {
  background: #2563eb;
  color: white;
}

.secondary {
  background: #e2e8f0;
  color: #0f172a;
}

button:hover {
  transform: translateY(-1px);
}

.sample-title {
  margin: 22px 0 12px;
  font-size: 1.05rem;
  font-weight: 700;
}

.sample-list {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.sample-button {
  background: #eff6ff;
  color: #1d4ed8;
  border: 1px solid #bfdbfe;
  padding: 10px 12px;
  border-radius: 10px;
  font-size: 0.9rem;
}

.right-column {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.badge {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  min-height: 36px;
  padding: 8px 12px;
  border-radius: 999px;
  background: #dbeafe;
  color: #1e3a8a;
  font-weight: 700;
}

.result-card {
  line-height: 1.6;
}

.result-card h2,
.result-card h3 {
  margin: 0 0 12px;
}

.meta-block {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 10px;
  margin: 18px 0;
}

.meta-box {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 14px;
}

.meta-box span {
  display: block;
  color: #64748b;
  font-size: 0.75rem;
  margin-bottom: 8px;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.evidence-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.evidence-list li {
  margin-bottom: 12px;
}

.evidence-item {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 14px;
}

.tag {
  display: inline-block;
  border-radius: 999px;
  padding: 4px 8px;
  font-size: 0.72rem;
  font-weight: 700;
  margin-bottom: 8px;
  text-transform: uppercase;
}

.tag.supporting {
  background: #dcfce7;
  color: #166534;
}

.tag.contradicting {
  background: #fee2e2;
  color: #991b1b;
}

.tag.neutral {
  background: #e2e8f0;
  color: #334155;
}

.meta {
  display: block;
  color: #64748b;
  font-size: 0.8rem;
  margin: 8px 0;
}

ul.source-list,
ul.warning-list {
  margin: 0;
  padding-left: 18px;
}

.empty-state {
  color: #64748b;
}

@media (max-width: 900px) {
  .layout {
    grid-template-columns: 1fr;
  }

  .meta-block {
    grid-template-columns: 1fr;
  }
}
