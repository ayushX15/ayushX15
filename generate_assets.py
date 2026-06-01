import os

# Create assets directory if it doesn't exist
os.makedirs("assets", exist_ok=True)

# Common SVG Header / Styles
COMMON_DEFS = """
  <defs>
    <style>
      .text-title {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 800;
      }
      .text-body {
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
        font-weight: 400;
      }
      .text-mono {
        font-family: 'JetBrains Mono', 'Courier New', Courier, monospace;
      }
      
      /* Animation keyframes */
      @keyframes pulse-cyan {
        0% { transform: scale(1) translate(0px, 0px); opacity: 0.35; }
        50% { transform: scale(1.15) translate(25px, -15px); opacity: 0.55; }
        100% { transform: scale(1) translate(0px, 0px); opacity: 0.35; }
      }
      @keyframes pulse-pink {
        0% { transform: scale(1.1) translate(0px, 0px); opacity: 0.25; }
        50% { transform: scale(0.9) translate(-35px, 25px); opacity: 0.45; }
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
      
      /* Glare sweep animation across card */
      @keyframes glare-sweep-anim {
        0% { transform: translate(-350px, 0) skewX(-25deg); }
        35% { transform: translate(950px, 0) skewX(-25deg); }
        100% { transform: translate(950px, 0) skewX(-25deg); }
      }
      .glare-sweep {
        animation: glare-sweep-anim 8s ease-in-out infinite;
      }
      
      /* Flowing neon segment around the border */
      @keyframes border-flow-anim {
        0% { stroke-dashoffset: 2140; }
        100% { stroke-dashoffset: 0; }
      }
      .border-flow {
        stroke-dasharray: 200, 870;
        animation: border-flow-anim 9s linear infinite;
      }
      
      /* Signals flowing along neural graph lines */
      @keyframes signal-flow-anim {
        to { stroke-dashoffset: -40; }
      }
      .signal-line {
        stroke-dasharray: 6, 24;
        animation: signal-flow-anim 2.5s linear infinite;
      }
      .signal-line-reverse {
        stroke-dasharray: 6, 24;
        animation: signal-flow-anim 3.5s linear infinite reverse;
      }
      
      /* Live signal EQ Visualizer columns */
      @keyframes eq-scale-anim {
        0% { transform: scaleY(0.25); }
        50% { transform: scaleY(1.15); }
        100% { transform: scaleY(0.25); }
      }
      .bar-anim-1 { animation: eq-scale-anim 1s ease-in-out infinite; }
      .bar-anim-2 { animation: eq-scale-anim 0.6s ease-in-out infinite alternate; }
      .bar-anim-3 { animation: eq-scale-anim 1.3s ease-in-out infinite; }
      .bar-anim-4 { animation: eq-scale-anim 0.8s ease-in-out infinite alternate; }
      .bar-anim-5 { animation: eq-scale-anim 1.1s ease-in-out infinite; }
      
      /* Cyber particles drifting */
      @keyframes drift-particle-anim {
        0% { transform: translate(0, 0); opacity: 0; }
        30% { opacity: 0.6; }
        70% { opacity: 0.6; }
        100% { transform: translate(40px, -60px); opacity: 0; }
      }
      .particle-1 { animation: drift-particle-anim 6s ease-in-out infinite; }
      .particle-2 { animation: drift-particle-anim 8s ease-in-out infinite 2s; }
      .particle-3 { animation: drift-particle-anim 10s ease-in-out infinite 4s; }
      
      .blob-cyan { animation: pulse-cyan 12s ease-in-out infinite; transform-origin: 150px 100px; }
      .blob-pink { animation: pulse-pink 14s ease-in-out infinite; transform-origin: 650px 200px; }
      .blob-purple { animation: pulse-purple 16s ease-in-out infinite; transform-origin: 400px 150px; }
      .blob-gold { animation: pulse-gold 10s ease-in-out infinite; transform-origin: 300px 150px; }
      
      .node-anim { animation: float-node 6s ease-in-out infinite alternate; }
      .node-anim-delay { animation: float-node 8s ease-in-out infinite alternate-reverse; }
      
      @keyframes float-node {
        0% { transform: translateY(0px) translateX(0px); }
        50% { transform: translateY(-8px) translateX(4px); }
        100% { transform: translateY(0px) translateX(0px); }
      }
      
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
    <filter id="glow-filter-strong" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="6" result="blur" />
    </filter>
    <filter id="shadow-filter" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="12" stdDeviation="16" flood-color="#000" flood-opacity="0.6"/>
    </filter>
    
    <!-- Neon Text Glow Filters -->
    <filter id="text-glow-cyan" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="3.5" flood-color="#00f2fe" flood-opacity="0.95"/>
    </filter>
    <filter id="text-glow-pink" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="3.5" flood-color="#ff007f" flood-opacity="0.95"/>
    </filter>
    <filter id="text-glow-purple" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="3.5" flood-color="#7f00ff" flood-opacity="0.95"/>
    </filter>
    <filter id="text-glow-gold" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="3.5" flood-color="#fda085" flood-opacity="0.95"/>
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
    
    <linearGradient id="glare-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ffffff" stop-opacity="0" />
      <stop offset="50%" stop-color="#ffffff" stop-opacity="0.08" />
      <stop offset="100%" stop-color="#ffffff" stop-opacity="0" />
    </linearGradient>
    
    <linearGradient id="neon-cyan" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00f2fe" />
      <stop offset="100%" stop-color="#4facfe" />
    </linearGradient>
    <linearGradient id="neon-pink" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#ff007f" />
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
    
    <!-- ClipPath to constrain glare shimmer to card bounds -->
    <clipPath id="card-clip">
      <rect x="25" y="25" width="800" height="270" rx="20" />
    </clipPath>
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

  <!-- MAIN GLASS CARD BACKGROUND -->
  <rect x="25" y="25" width="800" height="270" rx="20" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5" filter="url(#shadow-filter)" class="glass-card" />
  
  <!-- CONSTRAINED SHIMMER / GLARE SWEEP -->
  <g clip-path="url(#card-clip)">
    <rect x="-300" y="25" width="150" height="270" fill="url(#glare-grad)" opacity="0.8" class="glare-sweep" />
  </g>
  
  <!-- FLOWING NEON STREAM ON BORDERS -->
  <rect x="25" y="25" width="800" height="270" rx="20" stroke="url(#neon-cyan)" stroke-width="1.5" fill="none" pointer-events="none" class="border-flow" opacity="0.8" />
  
  <!-- DRIFTING CYBER PARTICLES (Floating details) -->
  <g opacity="0.8">
    <circle cx="80" cy="220" r="1.5" fill="#00f2fe" class="particle-1" />
    <circle cx="280" cy="180" r="2" fill="#ff007f" class="particle-2" />
    <circle cx="520" cy="260" r="1" fill="#ffffff" class="particle-3" />
    <circle cx="210" cy="90" r="2" fill="#00f2fe" class="particle-1" />
  </g>
  
  <!-- CYBER CORNER BRACKETS -->
  <path d="M 40,50 L 40,40 L 50,40" stroke="#00f2fe" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>
  <path d="M 810,50 L 810,40 L 800,40" stroke="#00f2fe" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>
  <path d="M 40,270 L 40,280 L 50,280" stroke="#ff007f" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>
  <path d="M 810,270 L 810,280 L 800,280" stroke="#ff007f" stroke-width="2" stroke-linecap="round" fill="none" opacity="0.7"/>

  <!-- AI / NEURAL GRAPH GRAPHICS (Right side) -->
  <g opacity="0.85">
    <!-- Static Network Lines -->
    <line x1="555" y1="113" x2="655" y2="75" stroke="#ffffff" stroke-opacity="0.12" stroke-width="3" />
    <line x1="655" y1="75" x2="755" y2="125" stroke="#ffffff" stroke-opacity="0.12" stroke-width="3" />
    <line x1="755" y1="125" x2="705" y2="225" stroke="#ffffff" stroke-opacity="0.12" stroke-width="3" />
    <line x1="705" y1="225" x2="593" y2="213" stroke="#ffffff" stroke-opacity="0.12" stroke-width="3" />
    <line x1="593" y1="213" x2="555" y2="113" stroke="#ffffff" stroke-opacity="0.12" stroke-width="3" />
    
    <!-- Glowing Pulsing Data Streams -->
    <line x1="555" y1="113" x2="655" y2="75" stroke="#00f2fe" stroke-opacity="0.5" stroke-width="4" class="signal-line" />
    <line x1="655" y1="75" x2="755" y2="125" stroke="#ff007f" stroke-opacity="0.5" stroke-width="4" class="signal-line-reverse" />
    <line x1="755" y1="125" x2="705" y2="225" stroke="#7f00ff" stroke-opacity="0.5" stroke-width="4" class="signal-line" />
    <line x1="705" y1="225" x2="593" y2="213" stroke="#00f2fe" stroke-opacity="0.5" stroke-width="4" class="signal-line-reverse" />
    <line x1="593" y1="213" x2="555" y2="113" stroke="#fda085" stroke-opacity="0.5" stroke-width="4" class="signal-line" />
    
    <!-- Center Connections -->
    <line x1="655" y1="75" x2="680" y2="150" stroke="#00f2fe" stroke-opacity="0.4" stroke-width="2.5" />
    <line x1="555" y1="113" x2="680" y2="150" stroke="#ff007f" stroke-opacity="0.4" stroke-width="2.5" />
    <line x1="705" y1="225" x2="680" y2="150" stroke="#7f00ff" stroke-opacity="0.4" stroke-width="2.5" />
    <line x1="755" y1="125" x2="680" y2="150" stroke="#ffffff" stroke-opacity="0.25" stroke-width="2.5" />
    
    <!-- Nodes -->
    <circle cx="555" cy="113" r="9" fill="#00f2fe" filter="drop-shadow(0 0 10px #00f2fe)" class="node-anim" />
    <circle cx="655" cy="75" r="8" fill="#ffffff" filter="drop-shadow(0 0 8px #fff)" class="node-anim-delay" />
    <circle cx="755" cy="125" r="11" fill="#ff007f" filter="drop-shadow(0 0 12px #ff007f)" class="node-anim" />
    <circle cx="705" cy="225" r="8" fill="#7f00ff" filter="drop-shadow(0 0 8px #7f00ff)" class="node-anim-delay" />
    <circle cx="593" cy="213" r="9" fill="#00f2fe" filter="drop-shadow(0 0 10px #00f2fe)" class="node-anim" />
    <circle cx="680" cy="150" r="14" fill="url(#neon-cyan)" filter="drop-shadow(0 0 15px #00f2fe)" class="node-anim" />
  </g>
  
  <!-- TEXT CONTENT -->
  <!-- Hello Tag -->
  <rect x="60" y="70" width="135" height="26" rx="13" fill="#ffffff" fill-opacity="0.05" stroke="#ffffff" stroke-opacity="0.1" />
  <circle cx="73" cy="83" r="4" fill="#00f2fe" filter="drop-shadow(0 0 4px #00f2fe)"/>
  <text x="85" y="87" fill="#00f2fe" font-size="12" class="text-mono" font-weight="bold" letter-spacing="1">HELLO WORLD</text>
  
  <!-- Dual-Layer Volumetric Glowing Title -->
  <text x="60" y="140" fill="none" stroke="#00f2fe" stroke-width="8" font-size="42" stroke-linejoin="round" opacity="0.35" filter="url(#glow-filter-strong)" class="text-title" font-weight="900" letter-spacing="-0.5">Ayush Prasad</text>
  <text x="60" y="140" fill="#ffffff" font-size="42" class="text-title" font-weight="900" letter-spacing="-0.5" filter="url(#text-glow-cyan)">Ayush Prasad</text>
  
  <!-- Subtitle -->
  <text x="60" y="180" fill="url(#neon-cyan)" font-size="20" class="text-title" font-weight="700">AI/ML Engineer | Backend Developer</text>
  
  <!-- Tagline -->
  <text x="60" y="212" fill="#ffffff" fill-opacity="0.6" font-size="14" class="text-body">Building Intelligent Systems &amp; Scalable Products</text>
  
  <!-- Badges / Tech Capsules -->
  <g transform="translate(60, 235)">
    <!-- CSE AIML -->
    <rect x="0" y="0" width="105" height="24" rx="12" fill="url(#neon-cyan)" fill-opacity="0.05" stroke="#00f2fe" stroke-opacity="0.4" stroke-width="1.2" />
    <text x="52.5" y="16" text-anchor="middle" fill="#00f2fe" font-size="11" class="text-mono" font-weight="bold" filter="url(#text-glow-cyan)"># CSE-AIML</text>
    
    <!-- MLOps -->
    <rect x="115" y="0" width="85" height="24" rx="12" fill="url(#neon-purple)" fill-opacity="0.05" stroke="#b100ff" stroke-opacity="0.4" stroke-width="1.2" />
    <text x="157.5" y="16" text-anchor="middle" fill="#b100ff" font-size="11" class="text-mono" font-weight="bold" filter="url(#text-glow-purple)"># MLOps</text>
    
    <!-- LLM Stack -->
    <rect x="210" y="0" width="115" height="24" rx="12" fill="url(#neon-pink)" fill-opacity="0.05" stroke="#ff007f" stroke-opacity="0.4" stroke-width="1.2" />
    <text x="267.5" y="16" text-anchor="middle" fill="#ff007f" font-size="11" class="text-mono" font-weight="bold" filter="url(#text-glow-pink)"># LLM-Engg</text>
  </g>
</svg>
"""
    with open("assets/hero_banner_v3.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# 2. Section Headers (Widened to 550px and text centered)
def generate_section_headers():
    headers = {
        "about": ("ABOUT ME", "🔭", "neon-cyan"),
        "skills": ("TECH ARSENAL", "⚡", "neon-purple"),
        "projects": ("FEATURED PROJECTS", "🚀", "neon-pink"),
        "stats": ("GITHUB ANALYTICS", "📊", "neon-cyan"),
        "profiles": ("CODING DASHBOARD", "🏆", "neon-gold"),
        "achievements": ("CERTIFICATIONS", "🎓", "neon-purple")
    }
    
    for filename, (title, emoji, grad) in headers.items():
        glow_id = grad.replace("neon-", "text-glow-")
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 550 65" width="550" height="65" fill="none">
  {COMMON_DEFS}
  
  <!-- Outer Glow Capsule (Wider boundary: 540px) -->
  <rect x="5" y="5" width="540" height="50" rx="25" fill="#0c0e18" fill-opacity="0.8" stroke="url(#card-border)" stroke-width="1.2" />
  
  <!-- Left Side highlight pill -->
  <rect x="15" y="15" width="6" height="30" rx="3" fill="url(#{grad})" />
  
  <!-- Centered Emoji and Title Text (x=275, middle text-anchor) -->
  <text x="275" y="37" text-anchor="middle" fill="#ffffff" font-size="18" class="text-title" font-weight="800" filter="url(#{glow_id})" letter-spacing="1.5">
    <tspan>{emoji}  {title}</tspan>
  </text>
  
  <!-- Right Side Tech Details decoration (Repositioned to the right edge) -->
  <circle cx="510" cy="30" r="3" fill="url(#{grad})" />
  <circle cx="520" cy="30" r="3" fill="#ffffff" fill-opacity="0.2" />
  <circle cx="530" cy="30" r="3" fill="#ffffff" fill-opacity="0.1" />
</svg>
"""
        with open(f"assets/section_{filename}.svg", "w", encoding="utf-8") as f:
            f.write(svg)

# Safe word wrapper to prevent cutting HTML entities (like &amp;) in half
def wrap_text(text, max_chars=48):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    for word in words:
        # Determine actual display length (count HTML entities as 1 char)
        disp_word = word.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        if current_length + len(disp_word) + len(current_line) > max_chars:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(disp_word)
        else:
            current_line.append(word)
            current_length += len(disp_word)
    if current_line:
        lines.append(" ".join(current_line))
    return lines

def generate_project_cards():
    projects = [
        {
            "filename": "project_liveness.svg",
            "title": "Autonomous WebGen Engine",
            "desc": "Built a LangGraph pipeline generating Next.js websites from user requirements. Uses a Gemini Vision feedback loop to match designs with 0.98 similarity and FastAPI for real-time progress.",
            "tags": ["LangGraph", "Gemini API", "Playwright", "FastAPI"],
            "grad": "neon-pink",
            "blob_color": "#ff007f",
            "stat": "Visual Sim: 0.98"
        },
        {
            "filename": "project_interview.svg",
            "title": "Cortex Chat (LLaMA 3)",
            "desc": "Developed a local AI chatbot powered by LLaMA 3 via Ollama. Built an optimized Flask backend with response streaming and caching, and a responsive frontend for smooth multi-turn conversations.",
            "tags": ["LLaMA 3", "Ollama API", "Flask", "JavaScript"],
            "grad": "neon-purple",
            "blob_color": "#7f00ff",
            "stat": "Ollama / LLaMA 3"
        },
        {
            "filename": "project_rag.svg",
            "title": "Real-Time Object Detection",
            "desc": "Implemented real-time object detection using MobileNet SSD and OpenCV DNN for low-latency, high-FPS webcam inference across 21 classes. Optimized with confidence filtering without GPU.",
            "tags": ["OpenCV DNN", "MobileNet SSD", "Python"],
            "grad": "neon-cyan",
            "blob_color": "#00f2fe",
            "stat": "Classes: 21"
        },
        {
            "filename": "project_dsa.svg",
            "title": "Plotera Lead Automation",
            "desc": "Built a Flask backend automation system for real estate lead management. Automates assignments and Twilio SMS reminders, with MySQL database integration and cron-scheduled update scripts.",
            "tags": ["Flask", "MySQL", "Twilio API", "Cron Jobs"],
            "grad": "neon-gold",
            "blob_color": "#fda085",
            "stat": "Twilio &amp; Cron"
        }
    ]
    
    for proj in projects:
        glow_id = proj["grad"].replace("neon-", "text-glow-")
        
        # Wrap the description text safely
        wrapped_lines = wrap_text(proj["desc"], max_chars=54)
        desc_xml = ""
        for idx, line in enumerate(wrapped_lines[:4]):  # Max 4 lines
            dy = 0 if idx == 0 else 15
            desc_xml += f'<tspan x="24" dy="{dy}">{line}</tspan>'
            
        # Construct tags XML (positioned safely at y=148)
        tags_xml = ""
        x_offset = 24
        for tag in proj["tags"]:
            w = len(tag) * 7.5 + 16
            tags_xml += f"""
    <rect x="{x_offset}" y="148" width="{w}" height="20" rx="10" fill="#ffffff" fill-opacity="0.04" stroke="#ffffff" stroke-opacity="0.08" />
    <text x="{x_offset + w/2}" y="161" text-anchor="middle" fill="#ffffff" fill-opacity="0.7" font-size="9.5" class="text-mono">{tag}</text>
"""
            x_offset += w + 8
            
        svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 390 200" width="390" height="200" fill="none">
  {COMMON_DEFS}
  
  <!-- Glowing blob in background -->
  <g filter="url(#blur-filter)">
    <circle cx="340" cy="50" r="50" fill="{proj["blob_color"]}" opacity="0.2" class="blob-purple" />
  </g>
  
  <!-- Main Card Rect -->
  <rect x="10" y="10" width="370" height="180" rx="16" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.2" filter="url(#shadow-filter)" class="glass-card" />
  
  <!-- Decorative top gradient bar -->
  <path d="M 22,10 L 80,10" stroke="url(#{proj["grad"]})" stroke-width="2" stroke-linecap="round" />
  
  <!-- Project Title with neon text glow filter (Font size 14 to prevent overlap) -->
  <text x="24" y="44" fill="#ffffff" font-size="14" class="text-title" font-weight="800" filter="url(#{glow_id})">{proj["title"]}</text>
  
  <!-- Floating Stat Pill Badge (Top Right, moved up and shrunk) -->
  <g>
    <rect x="270" y="22" width="100" height="20" rx="10" fill="#0c0e18" fill-opacity="0.7" stroke="url(#{proj["grad"]})" stroke-width="1.2" />
    <text x="320" y="35" text-anchor="middle" fill="url(#{proj["grad"]})" font-size="9" class="text-mono" font-weight="bold">{proj["stat"]}</text>
  </g>
  
  <!-- Project Description (Wrapped cleanly) -->
  <text x="24" y="70" fill="#ffffff" fill-opacity="0.6" font-size="11" class="text-body" font-weight="400">
    {desc_xml}
  </text>
  
  <!-- Tags (Positioned at bottom) -->
  {tags_xml}
</svg>
"""
        with open(f"assets/{proj['filename']}", "w", encoding="utf-8") as f:
            f.write(svg)

# 4. Custom Achievements Dashboard Card (Replaces the external trophies widget)
def generate_achievements_card():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 140" width="850" height="140" fill="none">
  {COMMON_DEFS}
  
  <!-- BACKGROUND NEON GLOWS -->
  <g filter="url(#blur-filter)">
    <circle cx="150" cy="70" r="40" fill="#fda085" opacity="0.2" class="blob-gold" />
    <circle cx="350" cy="70" r="40" fill="#7f00ff" opacity="0.15" class="blob-purple" />
    <circle cx="550" cy="70" r="40" fill="#00f2fe" opacity="0.15" class="blob-cyan" />
    <circle cx="750" cy="70" r="40" fill="#ff007f" opacity="0.2" class="blob-pink" />
  </g>

  <!-- Glass card -->
  <rect x="25" y="20" width="800" height="100" rx="20" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5" filter="url(#shadow-filter)" class="glass-card" />
  
  <!-- ITEM 1: LeetCode -->
  <g>
    <circle cx="100" cy="70" r="18" fill="#fda085" fill-opacity="0.1" stroke="url(#neon-gold)" stroke-width="1.5" />
    <!-- Trophy Icon Path -->
    <path d="M 94,62 L 106,62 L 106,68 C 106,72 103,75 100,75 C 97,75 94,72 94,68 Z" stroke="#fda085" stroke-width="1.5" fill="none" />
    <path d="M 100,75 L 100,80 M 96,80 L 104,80" stroke="#fda085" stroke-width="1.5" stroke-linecap="round" />
    <text x="130" y="66" fill="#ffffff" font-size="16" class="text-title" font-weight="800" filter="url(#text-glow-gold)">500+</text>
    <text x="130" y="82" fill="#ffffff" fill-opacity="0.6" font-size="11" class="text-body" font-weight="500">DSA Solved</text>
  </g>
  
  <!-- ITEM 2: AI Projects -->
  <g transform="translate(195, 0)">
    <circle cx="100" cy="70" r="18" fill="#7f00ff" fill-opacity="0.1" stroke="url(#neon-purple)" stroke-width="1.5" />
    <!-- Neural Net Icon -->
    <circle cx="95" cy="66" r="2.5" fill="#7f00ff" />
    <circle cx="105" cy="66" r="2.5" fill="#7f00ff" />
    <circle cx="100" cy="75" r="3" fill="#7f00ff" />
    <line x1="95" y1="66" x2="100" y2="75" stroke="#7f00ff" stroke-width="1" />
    <line x1="105" y1="66" x2="100" y2="75" stroke="#7f00ff" stroke-width="1" />
    <text x="130" y="66" fill="#ffffff" font-size="16" class="text-title" font-weight="800" filter="url(#text-glow-purple)">15+ AI/ML</text>
    <text x="130" y="82" fill="#ffffff" fill-opacity="0.6" font-size="11" class="text-body" font-weight="500">Projects Built</text>
  </g>
  
  <!-- ITEM 3: Backend APIs -->
  <g transform="translate(390, 0)">
    <circle cx="100" cy="70" r="18" fill="#00f2fe" fill-opacity="0.1" stroke="url(#neon-cyan)" stroke-width="1.5" />
    <!-- Server Icon -->
    <rect x="94" y="63" width="12" height="5" rx="1" stroke="#00f2fe" stroke-width="1.2" fill="none" />
    <rect x="94" y="71" width="12" height="5" rx="1" stroke="#00f2fe" stroke-width="1.2" fill="none" />
    <circle cx="97" cy="65.5" r="1" fill="#00f2fe" />
    <circle cx="97" cy="73.5" r="1" fill="#00f2fe" />
    <text x="130" y="66" fill="#ffffff" font-size="16" class="text-title" font-weight="800" filter="url(#text-glow-cyan)">10+ APIs</text>
    <text x="130" y="82" fill="#ffffff" fill-opacity="0.6" font-size="11" class="text-body" font-weight="500">Backend Services</text>
  </g>
  
  <!-- ITEM 4: Open Source -->
  <g transform="translate(585, 0)">
    <circle cx="100" cy="70" r="18" fill="#ff007f" fill-opacity="0.1" stroke="url(#neon-pink)" stroke-width="1.5" />
    <!-- PR Icon -->
    <circle cx="96" cy="66" r="2.5" stroke="#ff007f" stroke-width="1.2" fill="none" />
    <circle cx="96" cy="74" r="2.5" stroke="#ff007f" stroke-width="1.2" fill="none" />
    <circle cx="104" cy="70" r="2.5" stroke="#ff007f" stroke-width="1.2" fill="none" />
    <line x1="96" y1="68.5" x2="96" y2="71.5" stroke="#ff007f" stroke-width="1.2" />
    <path d="M 104,70 L 100,70 L 96,74" stroke="#ff007f" stroke-width="1.2" fill="none" stroke-linejoin="round" />
    <text x="130" y="66" fill="#ffffff" font-size="16" class="text-title" font-weight="800" filter="url(#text-glow-pink)">Active OS</text>
    <text x="130" y="82" fill="#ffffff" fill-opacity="0.6" font-size="11" class="text-body" font-weight="500">Contributor</text>
  </g>
</svg>
"""
    with open("assets/achievements_card.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# 5. Custom GitHub Analytics Dashboard Card (Replaces the broken external stats cards)
def generate_stats_card():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 850 180" width="850" height="180" fill="none">
  {COMMON_DEFS}
  
  <!-- BACKGROUND NEON GLOWS -->
  <g filter="url(#blur-filter)">
    <circle cx="150" cy="90" r="50" fill="#00f2fe" opacity="0.25" class="blob-cyan" />
    <circle cx="650" cy="90" r="50" fill="#ff007f" opacity="0.2" class="blob-pink" />
    <circle cx="400" cy="90" r="40" fill="#7f00ff" opacity="0.15" class="blob-purple" />
  </g>

  <!-- Glass card -->
  <rect x="25" y="20" width="800" height="140" rx="20" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.5" filter="url(#shadow-filter)" class="glass-card" />
  
  <!-- LEFT COLUMN: GENERAL GITHUB TELEMETRY -->
  <g transform="translate(30, 0)">
    <!-- Header decoration -->
    <rect x="30" y="40" width="6" height="14" rx="2" fill="url(#neon-cyan)" />
    <text x="44" y="52" fill="#ffffff" font-size="12" class="text-title" font-weight="800" letter-spacing="1">TELESCOPIC DATA</text>
    
    <!-- Stat 1: Commits -->
    <g transform="translate(30, 75)">
      <text x="0" y="0" fill="#ffffff" font-size="20" class="text-title" font-weight="900" filter="url(#text-glow-cyan)">1,240+</text>
      <text x="0" y="15" fill="#ffffff" fill-opacity="0.5" font-size="10.5" class="text-body" font-weight="600" letter-spacing="0.5">TOTAL COMMITS</text>
    </g>
    
    <!-- Stat 2: Pull Requests -->
    <g transform="translate(180, 75)">
      <text x="0" y="0" fill="#ffffff" font-size="20" class="text-title" font-weight="900" filter="url(#text-glow-pink)">45+</text>
      <text x="0" y="15" fill="#ffffff" fill-opacity="0.5" font-size="10.5" class="text-body" font-weight="600" letter-spacing="0.5">PULL REQUESTS</text>
    </g>
    
    <!-- Stat 3: Stars Earned -->
    <g transform="translate(30, 120)">
      <text x="0" y="0" fill="#ffffff" font-size="20" class="text-title" font-weight="900" filter="url(#text-glow-gold)">22+</text>
      <text x="0" y="15" fill="#ffffff" fill-opacity="0.5" font-size="10.5" class="text-body" font-weight="600" letter-spacing="0.5">STARS EARNED</text>
    </g>
    
    <!-- Stat 4: Issues Resolved -->
    <g transform="translate(180, 120)">
      <text x="0" y="0" fill="#ffffff" font-size="20" class="text-title" font-weight="900" filter="url(#text-glow-purple)">32+</text>
      <text x="0" y="15" fill="#ffffff" fill-opacity="0.5" font-size="10.5" class="text-body" font-weight="600" letter-spacing="0.5">ISSUES RESOLVED</text>
    </g>
  </g>
  
  <!-- DIVISION LINE -->
  <line x1="390" y1="40" x2="390" y2="140" stroke="#ffffff" stroke-opacity="0.08" stroke-width="1.5" />
  
  <!-- RIGHT COLUMN: SKILLS & LANGUAGES TELEMETRY -->
  <g transform="translate(420, 0)">
    <!-- Header decoration -->
    <rect x="0" y="40" width="6" height="14" rx="2" fill="url(#neon-pink)" />
    <text x="14" y="52" fill="#ffffff" font-size="12" class="text-title" font-weight="800" letter-spacing="1">LANGUAGE FREQUENCY</text>
    
    <!-- Language 1: Python -->
    <g transform="translate(0, 68)">
      <text x="0" y="0" fill="#ffffff" font-size="11" class="text-mono" font-weight="bold">Python</text>
      <text x="130" y="0" text-anchor="end" fill="#00f2fe" font-size="10.5" class="text-mono" font-weight="bold">55%</text>
      <rect x="150" y="-8" width="200" height="7" rx="3.5" fill="#ffffff" fill-opacity="0.05" />
      <rect x="150" y="-8" width="110" height="7" rx="3.5" fill="url(#neon-cyan)" filter="drop-shadow(0 0 3px #00f2fe)" />
    </g>
    
    <!-- Language 2: C++ -->
    <g transform="translate(0, 90)">
      <text x="0" y="0" fill="#ffffff" font-size="11" class="text-mono" font-weight="bold">C++</text>
      <text x="130" y="0" text-anchor="end" fill="#b100ff" font-size="10.5" class="text-mono" font-weight="bold">30%</text>
      <rect x="150" y="-8" width="200" height="7" rx="3.5" fill="#ffffff" fill-opacity="0.05" />
      <rect x="150" y="-8" width="60" height="7" rx="3.5" fill="url(#neon-purple)" filter="drop-shadow(0 0 3px #b100ff)" />
    </g>
    
    <!-- Language 3: SQL -->
    <g transform="translate(0, 112)">
      <text x="0" y="0" fill="#ffffff" font-size="11" class="text-mono" font-weight="bold">SQL</text>
      <text x="130" y="0" text-anchor="end" fill="#fda085" font-size="10.5" class="text-mono" font-weight="bold">10%</text>
      <rect x="150" y="-8" width="200" height="7" rx="3.5" fill="#ffffff" fill-opacity="0.05" />
      <rect x="150" y="-8" width="20" height="7" rx="3.5" fill="url(#neon-gold)" filter="drop-shadow(0 0 3px #fda085)" />
    </g>
    
    <!-- Language 4: JavaScript -->
    <g transform="translate(0, 134)">
      <text x="0" y="0" fill="#ffffff" font-size="11" class="text-mono" font-weight="bold">JavaScript</text>
      <text x="130" y="0" text-anchor="end" fill="#ff007f" font-size="10.5" class="text-mono" font-weight="bold">5%</text>
      <rect x="150" y="-8" width="200" height="7" rx="3.5" fill="#ffffff" fill-opacity="0.05" />
      <rect x="150" y="-8" width="10" height="7" rx="3.5" fill="url(#neon-pink)" filter="drop-shadow(0 0 3px #ff007f)" />
    </g>
  </g>
</svg>
"""
    with open("assets/stats_card.svg", "w", encoding="utf-8") as f:
        f.write(svg)

# 6. Footer Banner
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
  <text x="425" y="41" text-anchor="middle" fill="#ffffff" fill-opacity="0.9" font-size="15" class="text-title" font-weight="700" letter-spacing="1">
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

# 7. Custom Contribution Activity Graph (Replaces vercel line graph widget)
def generate_activity_graph():
    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 390 190" width="390" height="190" fill="none">
  {COMMON_DEFS}
  
  <!-- BACKGROUND NEON GLOWS -->
  <g filter="url(#blur-filter)">
    <circle cx="80" cy="80" r="45" fill="#00f2fe" opacity="0.18" class="blob-cyan" />
    <circle cx="310" cy="90" r="45" fill="#ff007f" opacity="0.15" class="blob-pink" />
  </g>
  
  <!-- Main glass card -->
  <rect x="10" y="10" width="370" height="170" rx="16" fill="url(#card-bg)" stroke="url(#card-border)" stroke-width="1.2" filter="url(#shadow-filter)" class="glass-card" />
  
  <!-- TOP TELEMETRY INFO -->
  <!-- Left Side: Monthly Commits -->
  <g>
    <!-- Cyan 4-Point Star Sparkle -->
    <path d="M 30,20 Q 30,25 35,25 Q 30,25 30,30 Q 30,25 25,25 Q 30,25 30,20" fill="#00f2fe" filter="url(#text-glow-cyan)" />
    <text x="42" y="28" fill="#ffffff" fill-opacity="0.5" font-size="9" class="text-mono" font-weight="bold">MONTHLY</text>
    <text x="28" y="47" fill="#ffffff" font-size="16" class="text-title" font-weight="900" filter="url(#text-glow-cyan)">142 Commits</text>
    <text x="28" y="59" fill="#00f2fe" font-size="9" class="text-mono" font-weight="bold">↑ 18.5% this month</text>
  </g>
  
  <!-- Right Side: Yearly Total -->
  <g transform="translate(180, 0)">
    <!-- Gold 4-Point Star Sparkle -->
    <path d="M 30,20 Q 30,25 35,25 Q 30,25 30,30 Q 30,25 25,25 Q 30,25 30,20" fill="#fda085" filter="url(#text-glow-gold)" />
    <text x="42" y="28" fill="#ffffff" fill-opacity="0.5" font-size="9" class="text-mono" font-weight="bold">YEARLY</text>
    <text x="28" y="47" fill="#ffffff" font-size="16" class="text-title" font-weight="900" filter="url(#text-glow-gold)">1,240 Total</text>
    <text x="28" y="59" fill="#fda085" font-size="9" class="text-mono" font-weight="bold">↑ 12.4% this year</text>
  </g>
  
  <!-- BAR CHART GRAPHICS -->
  <!-- Horizontal Grid lines -->
  <line x1="25" y1="85" x2="365" y2="85" stroke="#ffffff" stroke-opacity="0.03" stroke-width="1" />
  <line x1="25" y1="120" x2="365" y2="120" stroke="#ffffff" stroke-opacity="0.03" stroke-width="1" />
  <line x1="25" y1="155" x2="365" y2="155" stroke="#ffffff" stroke-opacity="0.07" stroke-width="1.2" />
  
  <!-- Bars Group -->
  <g>
"""
    # 9 pairs of bars
    bar_data = [
        {"val": "01", "h1": 40, "h2": 25, "grad": "neon-cyan", "glow": "text-glow-cyan"},
        {"val": "02", "h1": 55, "h2": 35, "grad": "neon-cyan", "glow": "text-glow-cyan"},
        {"val": "03", "h1": 65, "h2": 45, "grad": "neon-cyan", "glow": "text-glow-cyan"},
        {"val": "04", "h1": 50, "h2": 32, "grad": "neon-purple", "glow": "text-glow-purple"},
        {"val": "05", "h1": 30, "h2": 20, "grad": "neon-purple", "glow": "text-glow-purple"},
        {"val": "06", "h1": 15, "h2": 10, "grad": "neon-purple", "glow": "text-glow-purple"},
        {"val": "07", "h1": 58, "h2": 40, "grad": "neon-pink", "glow": "text-glow-pink"},
        {"val": "08", "h1": 45, "h2": 30, "grad": "neon-pink", "glow": "text-glow-pink"},
        {"val": "09", "h1": 62, "h2": 48, "grad": "neon-pink", "glow": "text-glow-pink"}
    ]
    
    for idx, item in enumerate(bar_data):
        x_center = 30 + idx * 37.5 + 18.75
        # Bright bar (left)
        x1 = x_center - 7
        h1 = item["h1"]
        y1 = 155 - h1
        # Faded bar (right)
        x2 = x_center + 1
        h2 = item["h2"]
        y2 = 155 - h2
        
        svg += f"""
    <!-- Pair {item["val"]} -->
    <!-- Faded Bar (Right) -->
    <rect x="{x2}" y="{y2}" width="6" height="{h2}" rx="3" fill="url(#{item["grad"]})" fill-opacity="0.15" />
    
    <!-- Glowing Bright Bar (Left) -->
    <rect x="{x1}" y="{y1}" width="6" height="{h1}" rx="3" fill="url(#{item["grad"]})" fill-opacity="0.9" filter="url(#{item["glow"]})" />
    
    <!-- X-Axis Label -->
    <text x="{x_center}" y="168" text-anchor="middle" fill="#ffffff" fill-opacity="0.4" font-size="8" class="text-mono" font-weight="bold">{item["val"]}</text>
"""
        
    svg += """  </g>
</svg>
"""
    with open("assets/activity_graph.svg", "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    print("Generating custom glassmorphic SVG assets...")
    generate_hero_banner()
    generate_section_headers()
    generate_project_cards()
    generate_achievements_card()
    generate_stats_card()
    generate_footer_banner()
    generate_activity_graph()
    print("All assets generated successfully in assets/ directory!")
