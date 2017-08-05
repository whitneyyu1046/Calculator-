#Do or die?
#Whitney
print "You're walking down a path and you suddenly spot some money on the floor. Do you pick it up or leave it there?"
print
print "1) Pick it up"
print "2) Leave it"

#Sydney
userInput = input("Enter:  ")
if userInput == 1:
    print "You pick up the money, but congrats! You've been abducted. A white van has kidnapped you."
    print "What will you do to escape?"
#Sheira
    print
    print "1) You scream"
    print "2) You perform self defense"
    userInput = input("Enter: ")
    if userInput == 1:
        print "You screamed too hard that your lungs collapsed."
        print "Congrats, you're dead!"
        print "You wake up and find yourself in a fiery enferno."
        print "A suave man walks up to you."
        print "He introduces himself. He's Danny the Devil."
        print "He's both captured you and your heart. He asks if you want to stay in the underworld with him and conquer the world together."
        print "1) Stay with YOUR man"
        print "2) Betray him with your coldhearted self"
        userInput = input("Enter: ")
        while userInput ==1:
            print
            print "Congratulations. You and your man spend an eternity happy together."
            print "Being abducted was worth it in the end"
            break
        while userInput== 2:
            print "Congratulations. He's the Devil. Did you really think you had a choice?"
            print "You get to stay in the underworld."
            break
    elif userInput == 2:
        print "Your raging kicks and punches were no match for the man in the rusty white van."
        print "He's a black belt in karate, but you didn't know that!"
        print "Congrats, you're dead!"
#Whitney
        print "You wake up and find yourself in a fiery enferno."
        print "A suave man walks up to you."
        print "He introduces himself. He's Danny the Devil."
        print "He's both captured you and your heart. He asks if you want to stay in the underworld with him and conquer the world together."
        print
        print "1) Stay with YOUR man"
        print "2) Betray him with your coldhearted self"
        userInput = input("Enter: ")
        while userInput ==1:
            print "Congratulations. You and your man spend an eternity happy together."
            break
        while userInput== 2:
            print "Congratulations. He's the Devil. Did you really think you had a choice?"
            print "You get to stay in the underworld."
            break
    else:
        print "That wasn't an option. For rebelling, the captor shoots you."
        print "Bam, you're dead"



    #elisha
elif userInput == 2:
    print "An old woman has given you $1,000,000"
    print "Do you spend it on yourself or others?"
    print "1) Spend it on yourself"
    print "2_ Spend it on others"
    userInput = input("Enter: ")
    while userInput== 1:
        print
        print "You amass a great amount of debt."
        print "You never learned how to manage your finances."
        print "Loans sharks come after year and you narrowly escape their first attack"
        print "You flee to Cabo but he knows you're there. In fact, this was all a part of his plan"
        print "He finds you one night. Congrats, you're dead"

    #Mia
        print "You wake up. You find yourself in heaven"
        print "God comes up to you and offers his hand. Do you shake God's hand?"
        print "1) Shake God's hand"
        print "2) You don't like germs, even from God, so you don't shake his hand"
        userInput = input("Enter: ")
        while userInput == 1:
            print "God tells you that you'll be transformed into an angel and stay in Heaven"
            print "Just kidding!"
            print "There's no such thing as Heaven."
            print "It was all a lie -- a dark void."
            break
    #Sydney
    while userInput== 2:
        print
        print "You spent all your money on others and have none left for yourself"
        print "You die of hunger"
        print "You wake up and find yourself in the clouds. It's HEAVEN. Some man comes up to you and tries to shake your hand. You decline. It turns out he's GOD."
        print "Since you didn't shake God's hand, you've been reincarnated."
        print "You come back to Earth."
        print "You find yourself in a white van driving down a suburban neighborhood in Seattle"
        print "You hear screams from the back of the van, your hand gripped around a handle of a knife"
        print "You are the abductor. Congrats!"
        break
    #break
