# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`

## [2026-05-23] create | Wiki initialized
- Domain: AI/ML technology news and trends
- Structure created with SCHEMA.md, index.md, log.md
- Wiki path: /root/wiki

## [2026-05-23] ingest | ESG招标日报
- Source: 采招网 bidcenter.com.cn — ESG关键词搜索
- Raw: raw/articles/esg-bidding-daily-2026-05-23.md — 7条招标信息
- Updated: concepts/esg-tendering.md — 新增5月23日重要招标项目
  - Updated: index.md — added [[esg-tendering]] entry, Total pages: 1
  - Highlights:
  - 防城港海上风电项目ESG咨询服务采购 — 78万元 — 广西
  - 财信产业基金ESG专项服务采购项目 — 70万元 — 湖南

## [2026-05-23] ingest | ESG招标日报（第二轮）
- Source: 采招网 bidcenter.com.cn — ESG关键词搜索（第二轮抓取）
- Raw: raw/articles/esg-bidding-daily-2026-05-23.md — 9条招标信息（含链接）
- Updated: concepts/esg-tendering.md — 新增链接、能源管理类条目、补充条目7-8
- New findings:
  - 资产、能源管理体系认证服务项目采购公告 — 山西 — 招标中
  - 山东省第10期中青年企业家培训班 — 53.23万元 — 山东
- All entries now have clickable bidcenter.com.cn URLs

## [2026-05-23] ingest | ESG招标日报（第三轮）
- Source: 采招网 bidcenter.com.cn — API直连GetSearchProHandler.ashx
- Raw: raw/articles/esg-bidding-daily-2026-05-23.md — 1条招标信息（标题含ESG且正在招标中）
- Updated: concepts/esg-tendering.md — 添加当日快照、最新搜索数据
- Notes: 当日标题含ESG且正在招标中的项目仅1条——财信产业基金ESG专项服务采购项目（70万，湖南，截止2026-06-05）

## [2026-05-23] ingest | ESG招标日报（第四轮）
- Source: 采招网 bidcenter.com.cn — 浏览器抓取ESG关键词搜索
- Raw: raw/articles/esg-bidding-daily-2026-05-23.md — 1条招标信息（标题含ESG且正在招标中）
- Updated: concepts/esg-tendering.md — 添加2026-05-23第二轮当日快照
- Notes: 当日标题含ESG且正在招标中的项目仅1条——财信产业基金ESG专项服务采购项目（70万，湖南，截止2026-06-05），与前几日为同一项目，无新增ESG招标项目

## [2026-05-24] ingest | ESG招标日报
- Source: 采招网 bidcenter.com.cn — ESG关键词搜索（浏览器抓取）
- Raw: raw/articles/esg-bidding-daily-2026-05-24.md — 1条招标信息（标题含ESG且正在招标中）
- Updated: concepts/esg-tendering.md — 添加2026-05-24当日快照
- Notes: 当日标题含ESG且正在招标中的项目仅1条——财信产业基金ESG专项服务采购项目（70万，湖南，截止2026-06-05），与前几日报为同一项目，无新增ESG招标项目

## [2026-05-25] ingest | ESG招标日报
- Source: 采招网 bidcenter.com.cn — API接口直连（AES解密）
- Raw: raw/articles/esg-bidding-daily-2026-05-25.md — 2条招标信息（标题含ESG且正在招标中）
- Updated: concepts/esg-tendering.md — 添加2026-05-25当日快照，新增重庆ESG信息披露项目
- New findings:
  - 关于为ESG信息披露服务公开选取机构的公告 — 20万元 — 重庆 — 2026-05-25（新增）
  - 财信产业基金ESG专项服务采购项目 — 70万元 — 湖南 — 截止2026-06-05（持续招标中）
- Highlights: 今日新增1条重庆ESG信息披露招标公告，财信产业基金项目仍在招标期内

## [2026-05-26] ingest | ESG招标日报
- Source: 采招网 bidcenter.com.cn — ESG关键词搜索（浏览器抓取，筛选条件：标题搜索+招标公告+近三天）
- Raw: raw/articles/esg-bidding-daily-2026-05-26.md — 2条招标信息（标题含ESG且正在招标中）
- Updated: concepts/esg-tendering.md — 添加2026-05-26当日快照，新增辽宁ESG蓝皮书项目
- New findings:
  - 《辽宁省国资国企社会责任ESG蓝皮书2026》编制服务-谈判采购公告 — 7万元 — 辽宁 — 2026-05-25（新增）
  - 关于为ESG信息披露服务公开选取机构的公告 — 20万元 — 重庆 — 2026-05-25（持续招标中，⚠️5月28日截止）
- Highlights: 今日新增1条辽宁ESG蓝皮书编制招标，重庆ESG信息披露项目选取时间临近（5月28日）

## [2026-05-27] ingest | ESG招标日报
- Source: 采招网 bidcenter.com.cn — ESG关键词搜索（浏览器抓取，筛选条件：标题搜索+招标公告+近三天）
- Raw: raw/articles/esg-bidding-daily-2026-05-27.md — 6条招标信息（标题含ESG且正在招标中），新增3条
- Updated: concepts/esg-tendering.md — 添加2026-05-27当日快照，新增3条重点推荐项目
  - Updated: index.md — updated last-modified date
  - New files: raw/articles/esg-bidding-daily-2026-05-27.md
- New findings:
  - 石柱土家族自治县建源建材股份有限公司ESG信息披露服务 — 20万元 — 重庆 — 2026-05-27（🔴新增）
  - 恒丰银行ESG风险管理系统外数切换及模型指标优化项目-竞争性磋商公告二次 — 山东 — 2026-05-27（🔴新增，二次公告）
  - 招标I社会责任ESG蓝皮书2026编制服务:7万 — 7万元 — 辽宁 — 2026-05-27（🔴新增）
  - 持续招标项目：辽宁ESG蓝皮书（7万，截止6月4日）、重庆ESG信息披露（20万，⚠️5月28日截止）
- Highlights: 今日新增3条ESG招标公告，为近几日最多。重庆ESG信息披露服务项目将于5月28日截止！
