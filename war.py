from random import randint

def main():
    record = []
    answer = 'y'
    while answer == 'y':
        player= randint(1,13)
        comp = randint(1,13)
        print("You draw a "+output(player))
        print("The computer draws a "+output(comp))
        if player > comp:
            print("Win")
            record.append('W')
        elif comp > player:
            print("Lost")
            record.append('L')
        else:
            print("Tie")
            record.append('T')
        answer = input("Again? ")
    stats(record)


    
def stats(r):
    totalwins = totalloss = totaltie = 0
    for i in range(len(r)):
        if r[i] == 'W':
            totalwins += 1
        elif r[i] == 'L':
            totalloss += 1
        else:
            totaltie += 1
    print("Total Wins:",totalwins)
    print("Total Losses:",totalloss)
    print("Total Ties:",totaltie)
            
def output(o):
    if o == 1:
        return "Ace"
    elif o == 11:
        return "Jack"
    elif o == 12:
        return "Queen"
    elif o == 13:
        return "King"
    else:
        return str(o)
main()
