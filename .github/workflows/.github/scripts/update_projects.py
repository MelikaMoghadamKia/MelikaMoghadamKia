"""Rebuild the Projects section of README.md from this account's repositories
that carry the GitHub topic TOPIC. Run by .github/workflows/update-projects.yml."""
import html, json, os, re, urllib.request

USER = "MelikaMoghadamKia"
TOPIC = "portfolio"
START, END = "<!--PROJECTS:START-->", "<!--PROJECTS:END-->"


def fetch_repos():
    url = f"https://api.github.com/users/{USER}/repos?per_page=100&type=owner&sort=pushed"
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def card(repo):
    name = html.escape(repo["name"])
    url = repo["html_url"]
    desc = html.escape(repo.get("description") or "Details inside the repository.")
    lang = repo.get("language")
    topics = [t for t in repo.get("topics", []) if t != TOPIC][:4]
    meta = []
    if lang:
        meta.append(f"<code>{html.escape(lang)}</code>")
    meta += [f"<code>{html.escape(t)}</code>" for t in topics]
    meta_line = " ".join(meta)
    return (
        f'<td width="50%" valign="top">\n'
        f'<h3><a href="{url}">📁 {name}</a></h3>\n'
        f"<p>{desc}</p>\n"
        f"<p>{meta_line}</p>\n"
        f'<p><a href="{url}"><b>View project →</b></a></p>\n'
        f"</td>"
    )


def render(repos):
    picked = [
        r for r in repos
        if TOPIC in r.get("topics", []) and not r.get("fork") and not r.get("archived")
        and r["name"].lower() not in (USER.lower(), f"{USER.lower()}.github.io")
    ]
    if not picked:
        return "_Projects will appear here soon._"
    cells = [card(r) for r in picked]
    if len(cells) % 2:
        cells.append('<td width="50%"></td>')
    rows = [f"<tr>\n{cells[i]}\n{cells[i+1]}\n</tr>" for i in range(0, len(cells), 2)]
    return "<table>\n" + "\n".join(rows) + "\n</table>"


def main():
    with open("README.md", encoding="utf-8") as f:
        text = f.read()
    if START not in text or END not in text:
        raise SystemExit("Markers not found in README.md")
    block = f"{START}\n{render(fetch_repos())}\n{END}"
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda m: block, text, flags=re.S)
    if new != text:
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(new)
        print("README.md updated")
    else:
        print("No changes")


if __name__ == "__main__":
    main()
