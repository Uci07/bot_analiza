import yfinance as yf


def analiza_companie(simbol):
    try:
        ticker = yf.Ticker(simbol)
        info = ticker.info

        # Extragem câteva date esențiale pentru checklist
        revenue_growth = info.get("revenueGrowth")
        ebitda = info.get("ebitda")
        net_income = info.get("netIncomeToCommon")
        free_cashflow = info.get("freeCashflow")
        gross_margin = info.get("grossMargins")
        operating_margin = info.get("operatingMargins")
        net_margin = info.get("netMargins")
        capex = info.get("capitalExpenditures")
        roa = info.get("returnOnAssets")
        roe = info.get("returnOnEquity")
        current_ratio = info.get("currentRatio")
        quick_ratio = info.get("quickRatio")
        debt_to_equity = info.get("debtToEquity")
        total_assets = info.get("totalAssets")
        operating_cf = info.get("operatingCashflow")
        net_debt = info.get("totalDebt") - info.get("cash")

        checklist = []

        # Criterii simplificate – exemplu
        checklist.append(("1. Vânzări în creștere >5%", f"{revenue_growth}", "✅" if revenue_growth and revenue_growth > 0.05 else "❌"))
        checklist.append(("2. EBITDA pozitiv", f"{ebitda}", "✅" if ebitda and ebitda > 0 else "❌"))
        checklist.append(("3. Profit net pozitiv", f"{net_income}", "✅" if net_income and net_income > 0 else "❌"))
        checklist.append(("4. Free Cash Flow pozitiv", f"{free_cashflow}", "✅" if free_cashflow and free_cashflow > 0 else "❌"))
        checklist.append(("6. Gross Margin > 40%", f"{gross_margin}", "✅" if gross_margin and gross_margin > 0.4 else "❌"))
        checklist.append(("7. Operating Margin > 15%", f"{operating_margin}", "✅" if operating_margin and operating_margin > 0.15 else "❌"))
        checklist.append(("8. Net Margin > 10%", f"{net_margin}", "✅" if net_margin and net_margin > 0.1 else "❌"))
        checklist.append(("13. ROA > 5%", f"{roa}", "✅" if roa and roa > 0.05 else "❌"))
        checklist.append(("15. ROE > 15%", f"{roe}", "✅" if roe and roe > 0.15 else "❌"))
        checklist.append(("18. Current Ratio > 1.5", f"{current_ratio}", "✅" if current_ratio and current_ratio > 1.5 else "❌"))
        checklist.append(("19. Quick Ratio > 1", f"{quick_ratio}", "✅" if quick_ratio and quick_ratio > 1 else "❌"))
        checklist.append(("21. Debt/Equity < 1", f"{debt_to_equity}", "✅" if debt_to_equity and debt_to_equity < 100 else "❌"))
        checklist.append(("30. Net Debt/EBITDA < 3", f"{net_debt}/{ebitda}", "✅" if ebitda and net_debt and (net_debt/ebitda) < 3 else "❌"))

        # Scoruri
        total_criterii = len(checklist)
        scor_total = sum(1 for c in checklist if c[2] == "✅")

        rezultat = f"\n📊 ANALIZĂ PENTRU {simbol.upper()}\n"
        rezultat += f"Scor total: {scor_total}/{total_criterii} ({round(100*scor_total/total_criterii)}%)\n"
        rezultat += "\n✅ CHECKLIST:\n"
        for idx, (nume, valoare, bifa) in enumerate(checklist, 1):
            rezultat += f"{idx}. {nume} → {valoare} {bifa}\n"

        return rezultat

    except Exception as e:
        return f"Eroare în analiza simbolului {simbol}: {e}"