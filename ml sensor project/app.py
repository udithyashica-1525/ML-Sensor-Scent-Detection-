from flask import Flask, render_template_string
import requests
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO

app = Flask(__name__)

CHANNEL_ID = "3328349"
READ_API = "YF2OQX8E8ALUJS2V"

URL = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API}&results=20"

def get_data():
    data = requests.get(URL).json()
    vals = []
    for f in data['feeds']:
        if f.get('field1'):
            try:
                vals.append(float(f['field1']))
            except:
                pass
    return vals

def graph(vals):
    time_axis = list(range(len(vals)))
    plt.figure(figsize=(6,3))
    plt.plot(time_axis, vals, marker='o', linewidth=2)
    plt.xlabel("Time (5 sec interval)")
    plt.ylabel("Gas Value")
    plt.title("Live Gas Monitoring")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    img = base64.b64encode(buf.getvalue()).decode()
    plt.close()
    return img

@app.route("/")
def home():
    vals = get_data()
    value = int(vals[-1])

    # ===== STATUS =====
    if value < 260:
        status = "UREA"
        color = "#00ff00"
        degree = 40
        voice = "System is safe"
        points = [
            "Urea is an organic compound and high-nitrogen fertilizer produced from ammonia and carbon dioxide.",
            " It supplies ~46% nitrogen, promoting fast plant growth and higher crop yield.",
            "Chemical formula: CO(NH₂)₂",
            " Carbon, oxygen, nitrogen, and hydrogen (with amine –NH₂ and carbonyl C=O groups).",
            "Safe texture: White, dry, crystalline granules (smooth and odorless).",
            "Hazard texture: Sticky/clumpy when moist and may release ammonia smell on decomposition"
        ]
        img = "https://loyalfertilizer.com/wp-content/uploads/2024/04/5-2024-04-20T112851.892.png"

    else:
        status = "MIXED"
        color = "#ff0000"
        degree = 140
        voice = "Danger detected"
        points = [
            "A combination of two or more nutrients (mainly nitrogen, phosphorus, and potassium) in one fertilizer.",
            "Provides balanced nutrition to plants, improving overall growth, yield, and soil fertility.",
            "No single formula; commonly represented as NPK (e.g., 17-17-17).",
            " Nitrogen compounds (urea/ammonium), phosphates (DAP/MAP), and potassium compounds (potash like KCl).",
            "Safe texture: Granular or powder form, dry and free-flowing.",
            "Hazard texture: Becomes clumpy when moist and may produce dust that can irritate skin or eyes."
        ]
        img = "https://image.made-in-china.com/202f0j00grOclTFROGuq/Urea-Potassium-NPK-Fertilizer-23-10-5-Compact-Granular-Fertilizer.webp"

    img_graph = graph(vals)

    return render_template_string(f"""
    <html>
    <head>

    <meta http-equiv="refresh" content="5">

    <style>
    body {{
        background:{color};
        text-align:center;
        font-family:Arial;
        animation: blink 1s infinite;
    }}

    @keyframes blink {{
        50% {{opacity:0.6;}}
    }}

    .card {{
        background:white;
        padding:20px;
        margin:5%;
        border-radius:20px;
        box-shadow:0 0 20px black;
    }}

    /* 🔥 GAUGE */
    .gauge {{
        width:200px;
        height:100px;
        border:6px solid black;
        border-radius:100px 100px 0 0;
        margin:auto;
        position:relative;
    }}

    .needle {{
        width:4px;
        height:90px;
        background:black;
        position:absolute;
        bottom:0;
        left:50%;
        transform-origin: bottom;
        animation: moveNeedle 2s ease-out forwards;
    }}

    @keyframes moveNeedle {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate({degree}deg); }}
    }}
    </style>

    <script>
    function speakLoop(text){{
        let msg = new SpeechSynthesisUtterance(text);
        msg.volume = 1;

        function repeat(){{
            speechSynthesis.speak(msg);
        }}

        repeat();
        setInterval(repeat, 8000); // repeat voice
    }}

    function beep(){{
        let ctx = new (window.AudioContext || window.webkitAudioContext)();
        let osc = ctx.createOscillator();
        osc.connect(ctx.destination);
        osc.start();
        osc.stop(ctx.currentTime + 0.3);
    }}

    window.onload = function(){{
        beep();
        speakLoop("{voice}");
    }}
    </script>

    </head>

    <body>

    <div class="card">

    <h1>🌱 AI Fertilizer Detection System</h1>

    <h2>{status}</h2>
    <h3>Gas Value: {value}</h3>

    <!-- 🔥 GAUGE -->
    <div class="gauge">
        <div class="needle"></div>
    </div>

    <br>

    <img src="{img}" width="200"><br><br>

    <!-- 🔥 CLEAN POINTS -->
    <ul style="text-align:left; display:inline-block;">
        {"".join([f"<li>{p}</li>" for p in points])}
    </ul>

    <h3>Live Monitoring</h3>

    <img src="data:image/png;base64,{img_graph}" width="500">

    </div>

    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=False)
