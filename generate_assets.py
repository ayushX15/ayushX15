import os

# Create assets directory if it doesn't exist
os.makedirs("assets", exist_ok=True)

# Common SVG Header / Styles
COMMON_DEFS = """
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap');
      
      .text-title {
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-weight: 800;
      }
      .text-body {
        font-family: 'Outfit', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        font-weight: 400;
      }
      .text-mono {
        font-family: 'JetBrains Mono', monospace;
      }
      
      /* Animation keyframes */
      @keyframes pulse-cyan {
        0% { transform: scale(1) translate(0px, 0px); opacity: 0.3; }
        50% { transform: scale(1.2) translate(30px, -20px); opacity: 0.5; }
        100% { transform: scale(1) translate(0px, 0px); opacity: 0.3; }
      }
      @keyframes pulse-pink {
        0% { transform: scale(1.1) translate(0px, 0px); opacity: 0.25; }
        50% { transform: scale(0.9) translate(-40px, 30px); opacity: 0.40; }
        100% { transform: scale(1.1) translate(0px, 0px); opacity: 0.25; }
      }
      @keyframes pulse-purple {
        0% { transform: scale(1) translate(0px, 0px); opacity: 0.2; }
        50% { transform: scale(1.2) translate(-20px, -20px); opacity: 0.4; }
        100% { transform: scale(1) translate(0px, 0px); opacity: 0.2; }
      }
      @keyframes pulse-gold {
        0% { transform: scale(1) translate(0px, 0px); opacity: 0.2; }
        50% { transform: scale(1.15) translate(20px, 20px); opacity: 0.4; }
        100% { transform: scale(1) translate(0px, 0px); opacity: 0.2; }
      }
      @keyframes card-hover {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-4px); }
      }
      @keyframes float-node {
        0% { transform: translateY(0px) translateX(0px); }
        50% { transform: translateY(-10px) translateX(5px); }
        100% { transform: translateY(0px) translateX(0px); }
      }
      @keyframes scan-line {
        0% { top: 0%; opacity: 0; }
        10% { opacity: 0.5; }
        90% { opacity: 0.5; }
        100% { top: 100%; opacity: 0; }
      }
      @keyframes border-shimmer {
        0% { stroke-dashoffset: 600; }
        100% { stroke-dashoffset: 0; }
      }
      
      .blob-cyan { animation: pulse-cyan 12s ease-in-out infinite; transform-origin: 150px 100px; }
      .blob-pink { animation: pulse-pink 14s ease-in-out infinite; transform-origin: 650px 200px; }
      .blob-purple { animation: pulse-purple 16s ease-in-out infinite; transform-origin: 400px 150px; }
      .blob-gold { animation: pulse-gold 10s ease-in-out infinite; transform-origin: 300px 150px; }
      
      .node-anim { animation: float-node 6s ease-in-out infinite alternate; }
      .node-anim-delay { animation: float-node 8s ease-in-out infinite alternate-reverse; }
      
      /* Card scaling styling for embedding directly */
      .glass-card {
        transition: all 0.3s ease;
      }
      .glass-card:hover {
        stroke: url(#card-border-hover);
        filter: drop-shadow(0 12px 24px rgba(0, 242, 254, 0.15));
      }
    </style>

    <!-- Filters -->
    <filter id="blur-filter" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="55" />
    </filter>
    <filter id="shadow-filter" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000" flood-opacity="0.6"/>
    </filter>
    
    <!-- Gradients -->
    <linearGradient id="card-bg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0c16" stop-opacity="0.75" />
      <stop offset="100%" stop-color="#04050a" stop-opacity="0.9" />
    </linearGradient>
    <linearGradient id="card-border" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0.18" />
      <stop offset="40%" stop-color="#ffffff" stop-opacity="0.03" />
      <stop offset="100%" stop-color="#00f2fe" stop-opacity="0.3" />
    </linearGradient>
    <linearGradient id="card-border-hover" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.6" />
      <stop offset="50%" stop-color="#7f00ff" stop-opacity="0.3" />
      <stop offset="100%" stop-color="#ff007f" stop-opacity="0.6" />
    </linearGradient>
    
    <linearGradient id="neon-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe" />
      <stop offset="100%" stop-color="#4facfe" />
    </linearGradient>
    <linearGradient id="neon-pink" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff0844" />
      <stop offset="100%" stop-color="#ffb199" />
    </linearGradient>
    <linearGradient id="neon-purple" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#b100ff" />
      <stop offset="100%" stop-color="#00e1ff" />
    </linearGradient>
    <linearGradient id="neon-gold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f6d365" />
      <stop offset="100%" stop-color="#fda085" />
    </linearGradient>
    
    <linearGradient id="header-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe" stop-opacity="0.8" />
      <stop offset="50%" stop-color="#7f00ff" stop-opacity="0.8" />
      <stop offset="100%" stop-color="#ff007f" stop-opacity="0.8" />
    </linearGradient>
  </defs>
"""

# 1. Hero Banner
def generate_hero_banner():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 320" width="850" height="320" fill="none">
  {COMMON_DEFS}
  
  <!-- BACKGROUND NEON GLOWS -->
  <g filter="url(#blur-filter)">
    <circle cx="150" cy="120" r="100" fill="#00f2fe" opacity="0.35" class="blob-cyan" />
    <circle cx="680" cy="200" r="110" fill="#ff007f" opacity="0.25" class="blob-pink" />
    <circle cx="420" cy="160" r="90" fill="#7f00ff" opacity="0.2" class="blob-purple" />
  </g>
  
  <!-- GRID OVERLAY FOR CYBERPUNK FEEL -->
  <path d="M 0,40 L 850,40 M 0,80 L 850,80 M 0,120 L 850,120 M 0,160 L 850,160 M 0,200 L 850,200 M 0,240 L 850,240 M 0,280 L 850,280" stroke="#ffffff" stroke-opacity="0.015" stroke-width="1" />
  <path d="M 100,0 L 100,320 M 200,0 L 200,320 M 300,0 L 300,320 M 400,0 L 400,320 M 500,0 L 500,320 M 600,0 L 600,320 M 700,0 L 700,320 M 800,0 L 800,320" stroke="#ffffff" stroke-opacity="0.015" stroke-width="1" />

  <!-- MAIN GLASS CARD -->
  <rect x="25" y="25" width="800" height="270" rx="20" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5" filter="url(#shadow-filter)" class="glass-card" />
  
  <!-- CYBER CORNER BRACKETS -->
  <path d="M 40,50 L 40,40 L 50,40" stroke="#00f2fe" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>
  <path d="M 810,50 L 810,40 L 800,40" stroke="#00f2fe" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>
  <path d="M 40,270 L 40,280 L 50,280" stroke="#ff007f" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>
  <path d="M 810,270 L 810,280 L 800,280" stroke="#ff007f" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>

  <!-- AI / GRAPH GRAPHICS (Right side) -->
  <g opacity="0.65">
    <!-- Links -->
    <line x1="580" y1="120" x2="660" y2="90" stroke="#ffffff" stroke-opacity="0.15" stroke-width="1.5" />
    <line x1="660" y1="90" x2="740" y2="130" stroke="#ffffff" stroke-opacity="0.15" stroke-width="1.5" />
    <line x1="740" y1="130" x2="700" y2="210" stroke="#ffffff" stroke-opacity="0.15" stroke-width="1.5" />
    <line x1="700" y1="210" x2="610" y2="200" stroke="#ffffff" stroke-opacity="0.15" stroke-width="1.5" />
    <line x1="610" y1="200" x2="580" y2="120" stroke="#ffffff" stroke-opacity="0.15" stroke-width="1.5" />
    
    <line x1="660" y1="90" x2="680" y2="150" stroke="#00f2fe" stroke-opacity="0.3" stroke-width="2" />
    <line x1="580" y1="120" x2="680" y2="150" stroke="#ff007f" stroke-opacity="0.3" stroke-width="2" />
    <line x1="700" y1="210" x2="680" y2="150" stroke="#7f00ff" stroke-opacity="0.3" stroke-width="2" />
    <line x1="740" y1="130" x2="680" y2="150" stroke="#ffffff" stroke-opacity="0.2" stroke-width="1.5" />
    
    <!-- Nodes -->
    <circle cx="580" cy="120" r="6" fill="#00f2fe" filter="drop-shadow(0 0 6px #00f2fe)" class="node-anim" />
    <circle cx="660" cy="90" r="5" fill="#ffffff" filter="drop-shadow(0 0 4px #fff)" class="node-anim-delay" />
    <circle cx="740" cy="130" r="7" fill="#ff007f" filter="drop-shadow(0 0 6px #ff007f)" class="node-anim" />
    <circle cx="700" cy="210" r="5" fill="#7f00ff" filter="drop-shadow(0 0 5px #7f00ff)" class="node-anim-delay" />
    <circle cx="610" cy="200" r="6" fill="#00f2fe" filter="drop-shadow(0 0 6px #00f2fe)" class="node-anim" />
    <circle cx="680" cy="150" r="9" fill="url(#neon-cyan)" filter="drop-shadow(0 0 10px #00f2fe)" class="node-anim" />
  </g>
  
  <!-- TEXT CONTENT -->
  <!-- Hello Tag -->
  <rect x="60" y="70" width="135" height="26" rx="13" fill="#ffffff" fill-opacity="0.05" stroke="#ffffff" stroke-opacity="0.1" />
  <circle cx="73" cy="83" r="4" fill="#00f2fe" filter="drop-shadow(0 0 4px #00f2fe)"/>
  <text x="85" y="87" fill="#00f2fe" font-size="12" class="text-mono" font-weight="bold" letter-spacing="1">HELLO WORLD</text>
  
  <!-- Title / Name -->
  <text x="60" y="140" fill="#ffffff" font-size="42" class="text-title" font-weight="900" letter-spacing="-0.5">Ayush Sharma</text>
  
  <!-- Subtitle -->
  <text x="60" y="180" fill="url(#neon-cyan)" font-size="20" class="text-title" font-weight="700">AI/ML Engineer | Backend Developer</text>
  
  <!-- Tagline -->
  <text x="60" y="212" fill="#ffffff" fill-opacity="0.6" font-size="14" class="text-body">Building Intelligent Systems &amp; Scalable Products</text>
  
  <!-- Badges / Tech Capsules -->
  <g transform="translate(60, 235)">
    <!-- CSE AIML -->
    <rect x="0" y="0" width="105" height="24" rx="12" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.08" />
    <text x="12" y="16" fill="#ffffff" fill-opacity="0.8" font-size="11" class="text-mono"># CSE-AIML</text>
    
    <!-- MLOps -->
    <rect x="115" y="0" width="85" height="24" rx="12" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.08" />
    <text x="127" y="16" fill="#ffffff" fill-opacity="0.8" font-size="11" class="text-mono"># MLOps</text>
    
    <!-- LLM Stack -->
    <rect x="210" y="0" width="115" height="24" rx="12" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.08" />
    <text x="222" y="16" fill="#ffffff" fill-opacity="0.8" font-size="11" class="text-mono"># LLM-Engg</text>
  </g>
</svg>
"""
    with open("assets/hero_banner.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# 2. Section Headers
def generate_section_headers():
    headers = {
        "about": ("ABOUT ME", "🔭", "neon-cyan"),
        "skills": ("TECH ARSENAL", "⚡", "neon-purple"),
        "projects": ("FEATURED PROJECTS", "🚀", "neon-pink"),
        "stats": ("GITHUB ANALYTICS", "📊", "neon-cyan"),
        "profiles": ("CODING DASHBOARD", "🏆", "neon-gold"),
        "achievements": ("MILESTONES & CERTIFICATIONS", "🎓", "neon-purple")
    }
    
    for filename, (title, emoji, grad) in headers.items():
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 450 65" width="450" height="65" fill="none">
  {COMMON_DEFS}
  
  <!-- Outer Glow Capsule -->
  <rect x="5" y="5" width="440" height="50" rx="25" fill="#0c0e18" fill-opacity="0.8" stroke="url(#card-border)" stroke-width="1.2" />
  
  <!-- Side highlight pill -->
  <rect x="15" y="15" width="6" height="30" rx="3" fill="url(#{grad})" />
  
  <!-- Emoji and Title Text -->
  <text x="35" y="36" fill="#ffffff" font-size="20" class="text-title" font-weight="800" letter-spacing="1.5">
    <tspan fill-opacity="0.9">{emoji}  {title}</tspan>
  </text>
  
  <!-- Tech Details decoration -->
  <circle cx="410" cy="30" r="3" fill="url(#{grad})" />
  <circle cx="420" cy="30" r="3" fill="#ffffff" fill-opacity="0.2" />
  <circle cx="430" cy="30" r="3" fill="#ffffff" fill-opacity="0.1" />
</svg>
"""
        with open(f"assets/section_{filename}.svg", "w", encoding="utf-8") as f:
            f.write(svg)

# 3. Project Cards
def generate_project_cards():
    projects = [
        {
            "filename": "project_liveness.svg",
            "title": "Face Liveness Detection",
            "desc": "Binary CNN classifier model detecting anti-spoofing attacks (photo, video replay). Optimized and deployed via ONNX runtime for low-latency inference.",
            "tags": ["PyTorch", "ONNX", "OpenCV", "FastAPI"],
            "grad": "neon-pink",
            "blob_color": "#ff007f",
            "stat": "Accuracy: 98.7%"
        },
        {
            "filename": "project_interview.svg",
            "title": "AI Interview Assistant",
            "desc": "Generative agent parsing resumes, conducting voice/text mock technical interviews, scoring responses, and providing semantic improvements.",
            "tags": ["OpenAI", "LangChain", "FastAPI", "Python"],
            "grad": "neon-purple",
            "blob_color": "#7f00ff",
            "stat": "Response Time: &lt;1.2s"
        },
        {
            "filename": "project_rag.svg",
            "title": "Enterprise RAG Chatbot",
            "desc": "Production-grade Q&amp;A pipeline using semantic search, hybrid vector index retrieval (dense/sparse), query rewriting, and LLM answer generation.",
            "tags": ["LlamaIndex", "VectorDB", "FastAPI", "Docker"],
            "grad": "neon-cyan",
            "blob_color": "#00f2fe",
            "stat": "MRR Score: 0.92"
        },
        {
            "filename": "project_dsa.svg",
            "title": "DSA Tracker &amp; Library",
            "desc": "Optimized C++ library housing advanced algorithms &amp; custom data structure templates (segment trees, graphs) designed to solve complex DSA problems.",
            "tags": ["C++", "STL", "Algorithms", "Optimization"],
            "grad": "neon-gold",
            "blob_color": "#fda085",
            "stat": "Problems Solved: 500+"
        }
    ]
    
    for proj in projects:
        # Construct tags XML
        tags_xml = ""
        x_offset = 24
        for idx, tag in enumerate(proj["tags"]):
            # Calculate width based on text length (approx 8px per char + padding)
            w = len(tag) * 8 + 16
            tags_xml += f"""
    <rect x="{x_offset}" y="128" width="{w}" height="22" rx="11" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.08" />
    <text x="{x_offset + w/2}" y="142" text-anchor="middle" fill="#ffffff" fill-opacity="0.7" font-size="10" class="text-mono">{tag}</text>
"""
            x_offset += w + 8
            
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 390 180" width="390" height="180" fill="none">
  {COMMON_DEFS}
  
  <!-- Glowing blob in background -->
  <g filter="url(#blur-filter)">
    <circle cx="340" cy="40" r="50" fill="{proj["blob_color"]}" opacity="0.2" class="blob-purple" />
  </g>
  
  <!-- Main Card Rect -->
  <rect x="10" y="10" width="370" height="160" rx="16" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.2" filter="url(#shadow-filter)" class="glass-card" />
  
  <!-- Decorative top gradient bar -->
  <path d="M 22,10 L 80,10" stroke="url(#{proj["grad"]})" stroke-width="2" stroke-linecap="round" />
  
  <!-- Project Title -->
  <text x="24" y="42" fill="#ffffff" font-size="17" class="text-title" font-weight="700">{proj["title"]}</text>
  
  <!-- Project Description (Wrap manually or use foreignObject. For compatibility, we use text block or clean structure) -->
  <text x="24" y="66" fill="#ffffff" fill-opacity="0.55" font-size="11.5" class="text-body" font-weight="400">
    <tspan x="24" dy="0">{proj["desc"][:52]}...</tspan>
    <tspan x="24" dy="16">{proj["desc"][52:108]}...</tspan>
    <tspan x="24" dy="16">{proj["desc"][108:] if len(proj["desc"]) > 108 else ""}</tspan>
  </text>
  
  <!-- Tags -->
  {tags_xml}
  
  <!-- Bottom Stat Widget -->
  <g transform="translate(24, 8)">
    <!-- Info Icon -->
    <path d="M 310,132 A 6 6 0 1 1 310,132.01" stroke="url(#{proj["grad"]})" stroke-width="2" stroke-linecap="round" />
    <text x="342" y="144" text-anchor="end" fill="url(#{proj["grad"]})" font-size="10.5" class="text-mono" font-weight="bold">{proj["stat"]}</text>
  </g>
</svg>
"""
        with open(f"assets/{proj['filename']}", "w", encoding="utf-8") as f:
            f.write(svg)

# 4. Footer Banner
def generate_footer_banner():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 70" width="850" height="70" fill="none">
  {COMMON_DEFS}
  
  <!-- Glowing blobs in the background -->
  <g filter="url(#blur-filter)">
    <circle cx="425" cy="35" r="40" fill="#7f00ff" opacity="0.3" class="blob-purple" />
    <circle cx="200" cy="35" r="30" fill="#00f2fe" opacity="0.2" class="blob-cyan" />
    <circle cx="650" cy="35" r="30" fill="#ff007f" opacity="0.2" class="blob-pink" />
  </g>

  <!-- Glass card -->
  <rect x="25" y="10" width="800" height="50" rx="25" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.2" />
  
  <!-- Footer Content -->
  <text x="425" y="40" text-anchor="middle" fill="#ffffff" fill-opacity="0.9" font-size="15" class="text-title" font-weight="700" letter-spacing="1">
    Thanks for visiting! Happy Coding <tspan fill="url(#neon-cyan)">🚀</tspan>
  </text>
  
  <!-- Decorative Dots -->
  <circle cx="50" cy="35" r="4" fill="#00f2fe" opacity="0.8" />
  <circle cx="65" cy="35" r="3" fill="#ffffff" opacity="0.2" />
  <circle cx="77" cy="35" r="2" fill="#ffffff" opacity="0.1" />
  
  <circle cx="800" cy="35" r="4" fill="#ff007f" opacity="0.8" />
  <circle cx="785" cy="35" r="3" fill="#ffffff" opacity="0.2" />
  <circle cx="773" cy="35" r="2" fill="#ffffff" opacity="0.1" />
</svg>
"""
    with open("assets/footer_banner.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    print("Generating custom glassmorphic SVG assets...")
    generate_hero_banner()
    generate_section_headers()
    generate_project_cards()
    generate_footer_banner()
    print("All assets generated successfully in assets/ directory!")
