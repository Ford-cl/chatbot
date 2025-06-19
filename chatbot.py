# chatbot.py

cryptos = [
    {
        "name": "Bitcoin",
        "symbol": "BTC",
        "price_usd": 67000,
        "trend": "up",
        "energy_efficiency": "low",
        "project_viability": "high"
    },
    {
        "name": "Ethereum",
        "symbol": "ETH",
        "price_usd": 3500,
        "trend": "up",
        "energy_efficiency": "medium",
        "project_viability": "high"
    },
    {
        "name": "Dogecoin",
        "symbol": "DOGE",
        "price_usd": 0.12,
        "trend": "down",
        "energy_efficiency": "high",
        "project_viability": "low"
    },
    {
        "name": "Cardano",
        "symbol": "ADA",
        "price_usd": 0.42,
        "trend": "up",
        "energy_efficiency": "high",
        "project_viability": "medium"
    }
]

def get_crypto_by_name(name):
    for crypto in cryptos:
        if crypto["name"].lower() == name.lower() or crypto["symbol"].lower() == name.lower():
            return crypto
    return None

def give_advice(crypto):
    print(f"\n📊 Analyzing {crypto['name']} ({crypto['symbol']})...")

    # Profitability
    if crypto["trend"] == "up":
        print("📈 Trend: Price is rising. Potential short-term gain.")
    else:
        print("📉 Trend: Price is falling. Might be risky to invest now.")

    # Energy Efficiency
    if crypto["energy_efficiency"] == "high":
        print("🔋 Energy: Very energy-efficient.")
    elif crypto["energy_efficiency"] == "medium":
        print("⚡ Energy: Moderate energy use.")
    else:
        print("🔥 Energy: High consumption. Not eco-friendly.")

    # Viability
    if crypto["project_viability"] == "high":
        print("📌 Viability: Strong long-term potential.")
    elif crypto["project_viability"] == "medium":
        print("📌 Viability: Moderate potential.")
    else:
        print("⚠️ Viability: Project is unstable. High risk.")

    print("✅ Recommendation complete.\n")
