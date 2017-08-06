import journal
def run_event_loop():
    """
        doc of menthod
    """
    print("what do you want to do with your journal?")
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = journal_load(journal_name)

    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd and entry. E[x]it: ')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we dont't understand '{}'.".format(cmd))
    
    print('Done, goodbye.')
    journal.save(journal_name, journal_data)

def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print('* [{}] {}'.format(idx + 1, entry))

def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    journal.add_entry(text, data)



def main():
    pass

if __name__ == "__main__":
    main()
