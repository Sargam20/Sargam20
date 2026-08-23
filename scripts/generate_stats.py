import os
import json
import urllib.request
import datetime

TOKEN = os.getenv("GITHUB_API_TOKEN")
USER = os.getenv("GITHUB_REPOSITORY_OWNER")

# Match brand guidelines exactly
COLORS = {
    "dark": {"bg": "#070A0F", "border": "#21262D", "text": "#F0F6FC", "secondary": "#8B949E", "blue": "#58A6FF"},
    "light": {"bg": "#ffffff", "border": "#d0d7de", "text": "#24292f", "secondary": "#57606a", "blue": "#0969da"}
}

def run_graphql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json"
        }
    )
    try:
        with urllib.request.urlopen(req) as response:
            return json.loads(response.read().decode())
    except Exception as e:
        print(f"API Request Failed: {e}")
        return None

def fetch_github_data():
    query = """
    query($login: String!) {
      user(login: $login) {
        contributionsCollection {
          contributionCalendar {
            totalContributions
          }
          restrictedContributionsCount
        }
        repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
          totalCount
          nodes {
            stargazerCount
          }
        }
      }
    }
    """
    data = run_graphql(query, {"login": USER})
    if not data or "errors" in data or "data" not in data or data["data"]["user"] is None:
        return None
    return data["data"]["user"]

def generate_svg(data, theme="dark"):
    c = COLORS[theme]
    cal = data["contributionsCollection"]["contributionCalendar"]
    total_public_contribs = cal["totalContributions"]
    total_private_contribs = data["contributionsCollection"]["restrictedContributionsCount"]
    total_contribs = total_public_contribs + total_private_contribs
    
    repos = data["repositories"]["nodes"]
    stars = sum(r["stargazerCount"] for r in repos)
    original_repos = data["repositories"]["totalCount"]
    
    timestamp = datetime.datetime.now().strftime("%d %b %Y").upper()
    
    # SVG string using the correct visual system styling
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="600" height="200" viewBox="0 0 600 200">
  <style>
    .bg {{ fill: {c["bg"]}; stroke: {c["border"]}; stroke-width: 1; rx: 8; }}
    .title {{ font-family: Inter, ui-sans-serif, sans-serif; font-size: 16px; font-weight: 700; fill: {c["text"]}; }}
    .metric {{ font-family: Inter, ui-sans-serif, sans-serif; font-size: 28px; font-weight: 700; fill: {c["blue"]}; }}
    .label {{ font-family: "SFMono-Regular", Consolas, monospace; font-size: 10px; font-weight: 700; fill: {c["secondary"]}; letter-spacing: 1.5px; }}
    .meta {{ font-family: "SFMono-Regular", Consolas, monospace; font-size: 9px; font-weight: 700; fill: {c["secondary"]}; letter-spacing: 1px; }}
  </style>
  <rect class="bg" width="598" height="198" x="1" y="1" />
  
  <text x="30" y="45" class="title">ENGINEERING ACTIVITY</text>
  
  <!-- GitHub Contributions (Public + Anonymized Private) -->
  <text x="30" y="100" class="metric">{total_contribs}</text>
  <text x="30" y="125" class="label">GITHUB CONTRIBUTIONS</text>
  
  <!-- Original Repositories -->
  <text x="230" y="100" class="metric">{original_repos}</text>
  <text x="230" y="125" class="label">ORIGINAL REPOSITORIES</text>
  
  <!-- Stars -->
  <text x="430" y="100" class="metric">{stars}</text>
  <text x="430" y="125" class="label">STARS EARNED</text>
  
  <!-- Data Freshness / Last Updated -->
  <text x="570" y="180" text-anchor="end" class="meta">LAST UPDATED · {timestamp}</text>
</svg>"""
    return svg

def main():
    if not TOKEN or not USER:
        print("Missing GITHUB_API_TOKEN or GITHUB_REPOSITORY_OWNER environment variables. Aborting.")
        exit(1)
        
    print(f"Fetching GitHub data for {USER}...")
    data = fetch_github_data()
    
    if not data:
        print("Error: Failed to fetch valid data from GitHub API.")
        print("Keeping last known-good SVG (if any) and aborting generation to prevent broken images.")
        exit(1)
        
    print("Data validated successfully. Generating SVGs...")
    
    with open("assets/github/overview.dark.svg", "w") as f:
        f.write(generate_svg(data, "dark"))
        
    with open("assets/github/overview.light.svg", "w") as f:
        f.write(generate_svg(data, "light"))
        
    print("Dashboard SVGs generated successfully.")

if __name__ == "__main__":
    main()
