blockchain = []

open_transactions = []

def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(sender, recipient, amount=1.0):
    """"Append a new value as well as the last blockchain value to the blockchain
    
    Arguments:
        :sender: The sender of coinds.
        :recipient: The recipient of coinds.
        :amount: The amount of coins sent with the transaction (default = 1.0)
    """
    


def mine_block():
    pass

def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float"""
    return float(input('Your transaction amount please: '))


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print("-" * 20)

def verify_chain():
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:            
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
    return is_valid
    # for block in blockchain:        
    #     if block_index == 0:
    #         block_index += 1
    #         continue        
    #     elif block[0] == blockchain[block_index - 1]:
    #         print(f"block[0] : {block[0]}", f"blockchain[block_index - 1] : {blockchain[block_index - 1]}")
    #         is_valid = True
    #     else:
    #         is_valid = False
    #         break
    #     block_index += 1
    

# tx_amount = get_transaction_value()
# add_transaction(tx_amount)

waiting_for_input = True


while waiting_for_input:
    print('Please choose:')
    print('Enter 1 form adding new transaction:')
    print('Enter 2 to return blockchain:')
    print('Enter h to Manipulate blockchain:')
    print('Enter q to quit:')
    user_choice = get_user_choice()

    if user_choice == "1":        
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == "2":
            
        print_blockchain_elements()
    elif user_choice == "h":
        if len(blockchain) > 0:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else: 
        print("invalid choice. Please pick from list.")
    if not verify_chain():
        print_blockchain_elements()
        print("invalid loop")
        break
else:
    print('User left!')
    
    print("Choice registered")
    