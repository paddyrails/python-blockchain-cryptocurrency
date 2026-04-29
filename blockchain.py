genesis_block = {
        'previous_hash': '', 
        'index': 0,
        'transactions': []
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'Max'

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """"Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
        :sender: The sender of coinds.
        :recipient: The recipient of coinds.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    transaction = {
        'sender': sender, 
        'recipient': recipient, 
        'amount': amount
    }
    open_transactions.append(transaction)
    


def mine_block():

    last_block = blockchain[-1]
    hashed_block = '-'.join([str(last_block[key]) for key in last_block ])
    print(f"hashed_block : {hashed_block}")        

    block = {
        'previous_hash': hashed_block, 
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)

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

    

# tx_amount = get_transaction_value()
# add_transaction(tx_amount)

waiting_for_input = True


while waiting_for_input:
    print('Please choose:')
    print('Enter 1 form adding new transaction:')
    print('Enter 2 to mine blocks:')
    print('Enter 3 to return blockchain:')
    print('Enter h to Manipulate blockchain:')
    print('Enter q to quit:')
    user_choice = get_user_choice()

    if user_choice == "1":        
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        add_transaction(recipient, amount=amount)
    elif user_choice == "2":
        mine_block()
    elif user_choice == "3":        
        print_blockchain_elements()
    # elif user_choice == "h":
    #     if len(blockchain) > 0:
    #         blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else: 
        print("invalid choice. Please pick from list.")
    # if not verify_chain():
    #     print_blockchain_elements()
    #     print("invalid loop")
    #     break
else:
    print('User left!')
    
    print("Choice registered")
    