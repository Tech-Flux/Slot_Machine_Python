import random

MAX_LINES = 3
MIN_BET = 100
MAX_BET = 1000

ROWS = 3
COLS = 3

symbol_count = {
    "🙂": 2,
    "👿": 4,
    "🌍": 6,
    "🎃": 8
}

winning_count = {
    "🙂": 3,
    "👿": 4,
    "🌍": 6,
    "🎃": 2
}

def __check_winnings__(columns, lines, bets, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
            else:
                winnings += values[symbol] * bets
                winning_lines.append(line + 1)
    return winnings, winning_lines

def get_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], "|", end=" ")
            else:
                print(column[row])
    print()

def deposit(balance):
    while True:
        money = input('Enter Amount to deposit\nKsh: ')
        if money.isdigit():
            money = int(money)
            if money >= 100:
                balance += money
                break
            else:
                print('Deposit must be more than Ksh. 100')
        else:
            print('Invalid Amount!')
    return balance

def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES) + '): ')
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print('Enter a valid Number!')
        else:
            print('Invalid Input!')
    return lines

def get_amount_of_bet():
    while True:
        bet = input('How much do you want to bet on each line (100-' + str(MAX_BET) + '): ')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f'Amount must be between Ksh{MIN_BET} - Ksh{MAX_BET}')
        else:
            print('Enter a valid Amount!')
    return bet

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bets = get_amount_of_bet()
        total_bets = bets * lines
        if total_bets <= balance:
            print(f'You are betting {bets} for {lines} lines: Total Amount is Ksh: {total_bets}')
            break
        else:
            print(f'You have insufficient Balance to Bet😕, Your balance is {balance}.')
    slots = get_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = __check_winnings__(slots, lines, bets, winning_count)
    print(f'You won {winnings}')
    print(f'You won on lines:', *winning_lines)
    balance += winnings - total_bets
    return balance

def main():
    balance = 0
    while True:
        print(f'Total Balance is {balance}')
        game = input('Press enter to play or 1 to Quit.')
        if game == "1":
            break
        if balance < MIN_BET:
            balance = deposit(balance)
        balance = spin(balance)
    print(f'You Gave up with {balance}')


main()
