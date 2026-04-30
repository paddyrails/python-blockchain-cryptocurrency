MINING_REWARD = 10
genesis_block = {
        'previous_hash': '', 
        'index': 0,
        'transactions': []
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'
participants = {'Max'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block ])

def get_balance(participant):
    tx_sender = [
        [tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain
    ]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)


    amount_sent = 0
    for tx in tx_sender:
        if(len(tx) > 0):
            amount_sent += tx[0]
    
    tx_recipient = [
        [tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain
    ]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]        
    
    return amount_received - amount_sent

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transaction(recipient, sender=owner, amount=1.0):
    """"Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
        :sender: The sender of coinds.
        :recipient: The recipient of coins.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
    }
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    return False
    


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    print(f"hashed_block : {hashed_block}")        
    reward_transaction = {
        "sender": "MINING",
        'recipient': owner,
        'amount': MINING_REWARD
    }
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain),
        'transactions': copied_transactions
    }
    blockchain.append(block)
    return True

def get_transaction_value(): # returns tuple
    """ Returns the input of the user (a new transaction amount) as a float"""
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount # tuple


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print("-" * 20)
    # for block in open_transactions:
    #     print('Outputting Block')
    #     print(block)
    # else:
    #     print("-" * 20)

def verify_chain():
    """Verify the current blockchain and return True if it's valid, False otherwise"""
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])
    # is_valid = True
    # for tx in open_transactions:
    #     if verify_transaction(tx):
    #         is_valid = True
    #     else:
    #         is_valid = False
    # return is_valid


# tx_amount = get_transaction_value()
# add_transaction(tx_amount)

waiting_for_input = True


while waiting_for_input:
    print('Please choose:')
    print('Enter 1 form adding new transaction:')
    print('Enter 2 to mine blocks:')
    print('Enter 3 to return blockchain:')
    print('Enter 4 to output participants:')
    print('Enter 5 to check transaction validity:')
    print('Enter h to Manipulate blockchain:')
    print('Enter q to quit:')
    user_choice = get_user_choice()

    if user_choice == "1":        
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print("Transaction failed!")
    elif user_choice == "2":
        if mine_block():
            open_transactions = []
    elif user_choice == "3":        
        print_blockchain_elements()
    elif user_choice == "4":        
        print(participants)
    elif user_choice == "5":        
        if verify_transactions():
            print("All transactions are valid")
        else:
            print("there are invalid transactions")
    elif user_choice == "h":
        if len(blockchain) > 0:
            blockchain[0] = {
                'previous_hash': '', 
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 10}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else: 
        print("invalid choice. Please pick from list.")
    if not verify_chain():
        print_blockchain_elements()
        print("invalid loop")
        break
    print(f"get_balance('Max') : {get_balance('Max')}")
else:
    print('User left!')
    
    print("Choice registered")
    