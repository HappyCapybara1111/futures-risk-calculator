# 定義一個 function，暫時未真正計任何東西
# 用戶口資金 × 風險百分比 ÷ 100，計完之後將答案交返出嚟就係return嘅用途
# 呢部計算機完成工作後，將計算結果交返畀叫它的人就係return嘅工作
# main() 可以理解成程式的「總指揮」或「由這裡開始做」

def calculate_risk_dollars(account_size, risk_percent):
    return account_size * risk_percent / 100


def calculate_contract_risk(stop_loss_points, point_value):
    return stop_loss_points * point_value


def calculate_max_contracts(risk_dollars, contract_risk):
    return risk_dollars / contract_risk


def main():
    account_size = float(input("Account size: "))
    risk_percent = float(input("Risk per trade (%): "))

    symbol = input("Enter your symbol: ")
    stop_loss_points = float(input("Stop loss points: "))
    point_value = float(input("Point value: "))

    risk_dollars = calculate_risk_dollars(account_size, risk_percent)
    contract_risk = calculate_contract_risk(stop_loss_points, point_value)
    max_contracts = calculate_max_contracts(risk_dollars, contract_risk)

    print(f"\nSymbol: {symbol}")
    print(f"Maximum risk per trade: ${risk_dollars:.2f}")
    print(f"Risk per contract: ${contract_risk:.2f}")
    print(f"Theoretical maximum contracts: {max_contracts:.2f}")


main()