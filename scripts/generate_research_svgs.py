import os

def create_svg(filename, title, subtitle):
    svg_content = f"""<svg width="400" height="150" viewBox="0 0 400 150" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#070A0F" rx="8" />
  <rect x="2" y="2" width="396" height="146" fill="transparent" stroke="#21262D" stroke-width="2" rx="8" />
  
  <text x="30" y="55" font-family="sans-serif" font-size="12" fill="#58A6FF" font-weight="bold" letter-spacing="1.5">{subtitle.upper()}</text>
  <text x="30" y="85" font-family="sans-serif" font-size="18" fill="#F0F6FC" font-weight="bold">{title}</text>
  
  <circle cx="370" cy="75" r="15" fill="#8B5CF6" fill-opacity="0.2" />
  <circle cx="370" cy="75" r="6" fill="#8B5CF6" />
</svg>"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)

def create_map(filename):
    svg_content = """<svg width="800" height="300" viewBox="0 0 800 300" xmlns="http://www.w3.org/2000/svg">
  <rect width="100%" height="100%" fill="#070A0F" />
  
  <!-- Flow Lines -->
  <path d="M 400,30 L 400,90" stroke="#8B949E" stroke-width="2" />
  <path d="M 200,90 L 600,90" stroke="#8B949E" stroke-width="2" />
  <path d="M 200,90 L 200,120" stroke="#8B949E" stroke-width="2" />
  <path d="M 400,90 L 400,120" stroke="#8B949E" stroke-width="2" />
  <path d="M 600,90 L 600,120" stroke="#8B949E" stroke-width="2" />
  <path d="M 200,180 L 200,210" stroke="#8B949E" stroke-width="2" />
  <path d="M 400,180 L 400,210" stroke="#8B949E" stroke-width="2" />
  <path d="M 600,180 L 600,210" stroke="#8B949E" stroke-width="2" />
  <path d="M 200,210 L 600,210" stroke="#8B949E" stroke-width="2" />
  <path d="M 400,210 L 400,240" stroke="#8B949E" stroke-width="2" />
  
  <!-- SARGAM SHARMA Root -->
  <text x="400" y="25" font-family="sans-serif" font-size="14" fill="#F0F6FC" font-weight="bold" letter-spacing="2" text-anchor="middle">SARGAM SHARMA</text>
  
  <!-- Domain Titles -->
  <text x="200" y="140" font-family="sans-serif" font-size="12" fill="#58A6FF" font-weight="bold" letter-spacing="1" text-anchor="middle">PHYSIOLOGICAL AI</text>
  <text x="400" y="140" font-family="sans-serif" font-size="12" fill="#8B5CF6" font-weight="bold" letter-spacing="1" text-anchor="middle">MULTIMODAL SECURITY</text>
  <text x="600" y="140" font-family="sans-serif" font-size="12" fill="#22D3EE" font-weight="bold" letter-spacing="1" text-anchor="middle">CYBERSECURITY</text>
  
  <!-- Projects -->
  <text x="200" y="165" font-family="sans-serif" font-size="16" fill="#F0F6FC" font-weight="bold" text-anchor="middle">PhysioFM</text>
  <text x="400" y="165" font-family="sans-serif" font-size="16" fill="#F0F6FC" font-weight="bold" text-anchor="middle">Semantic Drift</text>
  <text x="600" y="165" font-family="sans-serif" font-size="16" fill="#F0F6FC" font-weight="bold" text-anchor="middle">SentinelAI</text>
  
  <!-- Bottom Node -->
  <text x="400" y="260" font-family="sans-serif" font-size="12" fill="#58A6FF" font-weight="bold" letter-spacing="1" text-anchor="middle">INTELLIGENT TRANSPORT</text>
  <text x="400" y="285" font-family="sans-serif" font-size="16" fill="#F0F6FC" font-weight="bold" text-anchor="middle">IMPACT</text>
</svg>"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(svg_content)

if __name__ == "__main__":
    base_dir = "assets/research"
    create_svg(f"{base_dir}/physiofm.svg", "PhysioFM", "01 / PHYSIOLOGICAL AI")
    create_svg(f"{base_dir}/semantic-drift.svg", "Semantic Drift Before Inference", "02 / MULTIMODAL SECURITY")
    create_svg(f"{base_dir}/sentinelai.svg", "SentinelAI", "03 / CYBERSECURITY")
    create_svg(f"{base_dir}/impact.svg", "IMPACT", "04 / INTELLIGENT TRANSPORTATION")
    create_map(f"{base_dir}/research-map.svg")
    print("Research SVGs generated.")
