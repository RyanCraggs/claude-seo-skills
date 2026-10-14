# Installing this skill

## 1. Install the skill
**Claude desktop / claude.ai:** upload the zipped `weekly-gsc-seo-report` folder under Settings → Capabilities → Skills.

**Claude Code:** unzip the folder to:
```
~/.claude/skills/weekly-gsc-seo-report/
  SKILL.md
  config.json
  SETUP.md
  reference/gsc-queries.md
  reference/voice.md
```
To share with the team, put it in a project's `.claude/skills/` instead, or upload it to your org's skill library.

## 2. Connect Google Search Console (required)
The skill needs a GSC MCP server that exposes `get_advanced_search_analytics` (explicit start/end dates, dimensions, page filters, sort, `data_state`). The original install used a local server registered as `gscServer` (uvx `mcp-search-console`).
- Authenticate with a Google account that can see your property.
- Call `list_properties`, confirm your property is listed, and put it in `site.site_url` in `config.json`.
- If the server or tool names differ, update `tool_prefixes.gsc` in `config.json`.

## 3. Connect Slack (optional)
- Connect the Slack connector and authorize it for your workspace.
- The tool prefix will differ per install. Find it with ToolSearch `slack_send_message` and update `tool_prefixes.slack` in `config.json`.
- Look up the recipient's user or channel ID (`slack_search_users`), put it in `delivery.slack_recipient_id`, and set `delivery.method` to `"slack"`.
- No Slack? Leave `delivery.method` as `"chat"`.

## 4. Validate
Pick two recent weeks, check the sitewide and /blog/ totals by hand in the GSC dashboard (Performance, `data_state` = all), and record them in the validation table in `reference/gsc-queries.md`. Then ask: *"Run the weekly SEO report for <those dates>, show in chat only."* The totals should match.

## 5. Schedule it (optional)
Because the GSC server runs locally, use a **local** scheduled task (Claude desktop "Scheduled"), not a cloud routine. Local tasks only run while the app is open. Suggested: Thursdays 9:00am.

Task prompt to paste:
```
Run the weekly-gsc-seo-report skill. Read SKILL.md, config.json, reference/gsc-queries.md and reference/voice.md first. current_week = the most recent fully completed Monday–Sunday before today (America/New_York); prior_week = the 7 days before it. Deliver per config.json without asking. If any GSC pull fails, don't fabricate numbers: send a short note saying the report couldn't run and why. If the Slack send fails, leave the full report in the final output.
```

## Left out on purpose
- AI-visibility (Gumshoe / Semrush AI Visibility). It's monthly data, not weekly.
